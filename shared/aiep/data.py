"""Dataset and artefact resolution.

Two public functions carry the whole course:

* ``get_dataset(name)``   — returns a Path to the dataset file, fetching it if needed.
* ``load_artefact(name)`` — returns a Path to something a previous lab produced, falling
  back to an instructor-provided reference copy so a missed day never blocks a student.

Notebooks never contain a file path. See ``docs/Data_Guide.md``.
"""

from __future__ import annotations

import hashlib
import os
import shutil
from pathlib import Path
from typing import Any

from .paths import cache_dir, in_colab, notebook_dir, repo_root, solutions_cache_dir

__all__ = [
    "registry",
    "dataset_info",
    "get_dataset",
    "load_artefact",
    "save_artefact",
    "describe_dataset",
    "sha256_of",
]

_REGISTRY_CACHE: dict[str, Any] | None = None

# Where the registry is published for Colab, which has no repo checkout to read it from.
_REGISTRY_URL = os.environ.get(
    "AIEP_REGISTRY_URL",
    "https://raw.githubusercontent.com/0xRush/AIEP_Olo_student/main/shared/datasets.yaml",
)


# --------------------------------------------------------------------------- registry


def registry(refresh: bool = False) -> dict[str, Any]:
    """Load ``shared/datasets.yaml``, from the local checkout or over the network."""
    global _REGISTRY_CACHE
    if _REGISTRY_CACHE is not None and not refresh:
        return _REGISTRY_CACHE

    import yaml

    root = repo_root()
    local = root / "shared" / "datasets.yaml" if root else None

    if local and local.exists():
        text = local.read_text(encoding="utf-8")
    else:
        # Colab-from-GitHub: no checkout, so fetch the registry itself.
        import requests

        response = requests.get(_REGISTRY_URL, timeout=30)
        response.raise_for_status()
        text = response.text

    _REGISTRY_CACHE = yaml.safe_load(text) or {}
    return _REGISTRY_CACHE


def dataset_info(name: str) -> dict[str, Any]:
    """Registry entry for `name`, with a helpful error listing valid names."""
    reg = registry()
    if name not in reg:
        known = ", ".join(sorted(reg)) or "(registry is empty)"
        raise KeyError(
            f"Unknown dataset {name!r}.\n"
            f"Known datasets: {known}\n"
            f"Add it to shared/datasets.yaml — see docs/Data_Guide.md."
        )
    return reg[name]


# ----------------------------------------------------------------------------- hashing


def sha256_of(path: Path) -> str:
    """Streaming sha256 so a large file doesn't have to fit in memory."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def _verify(path: Path, expected: str | None, *, strict: bool = False) -> bool:
    """Check a file's hash. Returns True when it matches or there is nothing to check."""
    if not expected:
        return True
    actual = sha256_of(path)
    if actual == expected:
        return True
    message = (
        f"Checksum mismatch for {path.name}\n"
        f"  expected: {expected}\n"
        f"  actual:   {actual}\n"
        f"The file may be corrupt or the registry may be out of date."
    )
    if strict:
        raise ValueError(message)
    print(f"⚠️  {message}")
    return False


# --------------------------------------------------------------------------- fetching


def _download(url: str, target: Path, size_mb: float | None = None) -> None:
    """Stream a download to `target`, via a temp file so a failure leaves no half-file."""
    import requests

    hint = f" ({size_mb} MB)" if size_mb else ""
    print(f"⬇️  Downloading {target.name}{hint} …")

    tmp = target.with_suffix(target.suffix + ".part")
    try:
        with requests.get(url, stream=True, timeout=120) as response:
            response.raise_for_status()
            with open(tmp, "wb") as fh:
                for chunk in response.iter_content(chunk_size=1024 * 256):
                    fh.write(chunk)
        tmp.replace(target)
    finally:
        tmp.unlink(missing_ok=True)


def _prompt_upload(filename: str, target_dir: Path) -> Path | None:
    """Last resort: ask the human for the file.

    On Colab this opens the file picker. Locally it prints where to put the file and
    gives up — a local user can just copy it in and re-run the cell.
    """
    print(
        "\n"
        "──────────────────────────────────────────────────────────────\n"
        f"  Could not find or download:  {filename}\n"
        f"  لم يتم العثور على الملف أو تنزيله:  {filename}\n"
        "\n"
        f"  Put it here and re-run this cell:\n"
        f"  ضع الملف في هذا المسار ثم أعد تشغيل الخلية:\n"
        f"      {target_dir}\n"
        "──────────────────────────────────────────────────────────────\n"
    )

    if not in_colab():
        return None

    try:
        from google.colab import files  # type: ignore[import-not-found]
    except ImportError:
        return None

    print("  Or upload it now / أو ارفعه الآن:")
    uploaded = files.upload()
    if filename in uploaded:
        target = target_dir / filename
        target_dir.mkdir(parents=True, exist_ok=True)
        Path(filename).replace(target)
        print(f"✅ Saved to {target}")
        return target

    # They uploaded something with a different name — take it if there's exactly one.
    if len(uploaded) == 1:
        actual = next(iter(uploaded))
        target = target_dir / filename
        Path(actual).replace(target)
        print(f"✅ Saved {actual} as {target}")
        return target

    return None


def get_dataset(name: str, *, verify: bool = True) -> Path:
    """Return a Path to the dataset registered as `name`, fetching it if necessary.

    Resolution order — the first hit wins:

      1. ``shared/data_cache/<file>`` in a local checkout.
      2. The Colab session directory.
      3. Download from the registry's pinned URL, then verify its sha256.
      4. Ask the user to upload it.

    Prints one line saying which route it took, so a confused student can see where
    their data came from.

    Args:
        name: key in ``shared/datasets.yaml``.
        verify: check the sha256 after a download. Leave this on.

    Returns:
        Path to a file that exists.

    Raises:
        KeyError: `name` is not in the registry.
        FileNotFoundError: every route failed.
    """
    info = dataset_info(name)

    loader = info.get("loader")
    if loader == "torchvision":
        raise ValueError(
            f"{name!r} is a torchvision dataset — load it with torchvision.datasets, "
            f"not get_dataset(). The registry entry exists only to document it."
        )
    if loader == "manual":
        raise FileNotFoundError(
            f"{name!r} must be downloaded by hand (its licence forbids redistribution).\n"
            f"Source: {info.get('source', '(not recorded)')}\n"
            f"Save it as {info['file']} in {cache_dir()}"
        )

    filename = info["file"]
    expected = info.get("sha256")
    destination = cache_dir()

    # 1 & 2 — already on disk somewhere we know about.
    for candidate in (destination / filename, Path("/content/aiep_data") / filename):
        if candidate.exists():
            _verify(candidate, expected if verify else None)
            print(f"📁 {name}: using cached file at {candidate}")
            return candidate

    # 3 — download.
    url = info.get("url")
    if url:
        try:
            target = destination / filename
            _download(url, target, info.get("size_mb"))
            if verify and not _verify(target, expected):
                target.unlink(missing_ok=True)
                raise ValueError("checksum mismatch")
            print(f"✅ {name}: downloaded to {target}")
            return target
        except Exception as exc:  # network down, 404, bad checksum
            print(f"⚠️  Download failed for {name}: {exc}")

    # 4 — ask the human.
    uploaded = _prompt_upload(filename, destination)
    if uploaded is not None:
        return uploaded

    raise FileNotFoundError(
        f"Could not obtain dataset {name!r} ({filename}).\n"
        f"Expected it in {destination}, or downloadable from {url or '(no url registered)'}."
    )


# --------------------------------------------------------------------------- artefacts


def load_artefact(filename: str) -> Path:
    """Return a Path to an artefact a previous lab produced.

    Looks in this notebook's ``artefacts/`` first, then in ``shared/solutions_cache/``.
    The fallback is what stops a student who missed yesterday from being stuck today —
    providing that reference copy is mandatory for any artefact a later lab consumes.
    """
    local = notebook_dir() / "artefacts" / filename
    if local.exists():
        return local

    fallback = solutions_cache_dir() / filename
    if fallback.exists():
        print(
            f"ℹ️  Using the reference copy of {filename} from solutions_cache "
            f"(you don't have a local one yet).\n"
            f"   نستخدم النسخة المرجعية من {filename} لعدم وجود نسخة محلية لديك."
        )
        return fallback

    raise FileNotFoundError(
        f"Artefact {filename!r} not found.\n"
        f"  looked in: {local}\n"
        f"         and: {fallback}\n"
        f"Run the lab that produces it, or ask your instructor for the reference copy."
    )


def save_artefact(source: Path | str, filename: str | None = None) -> Path:
    """Copy a file into this notebook's ``artefacts/`` directory and return the new path.

    Most labs write straight to ``ARTEFACT_DIR``; this helper is for the case where a
    library insisted on writing somewhere else first.
    """
    source = Path(source)
    target = notebook_dir() / "artefacts" / (filename or source.name)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return target


# ------------------------------------------------------------------------ description


def describe_dataset(name: str) -> str:
    """Bilingual description of a dataset, for the lab's 'About the data' section.

    Includes the ``gotcha`` field — the known problem with the data. That field is
    mandatory in the registry precisely so it ends up in front of students.
    """
    info = dataset_info(name)
    lines = [
        f"{name}  ({info.get('rows', '?')} rows, {info.get('size_mb', '?')} MB)",
        f"  Source:  {info.get('source', '(not recorded)')}",
        f"  Licence: {info.get('licence', '(not recorded)')}",
        f"  Target:  {info.get('target', '(none)')}",
        "",
        f"  EN: {(info.get('description_en') or '').strip()}",
        f"  AR: {(info.get('description_ar') or '').strip()}",
    ]
    if info.get("gotcha_en"):
        lines += [
            "",
            f"  ⚠️  Watch out: {info['gotcha_en'].strip()}",
            f"  ⚠️  انتبه: {(info.get('gotcha_ar') or '').strip()}",
        ]
    return "\n".join(lines)
