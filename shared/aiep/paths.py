"""Path resolution that works identically on a laptop, on Windows, and on Google Colab.

Nothing else in the course hard-codes a path. Notebooks import from here (usually
indirectly, via ``aiep.data``) so the same notebook file runs unchanged everywhere.

Key idea: there are two "roots" and they are not the same thing.

* ``repo_root()``   — where the course repo lives, if we can find it. May be None on Colab.
* ``cache_dir()``   — where datasets live. Falls back to a Colab/temp directory when there
                      is no repo, which is exactly the case when a student opens a notebook
                      straight from GitHub in Colab.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

__all__ = [
    "in_colab",
    "repo_root",
    "cache_dir",
    "solutions_cache_dir",
    "notebook_dir",
    "artefact_dir",
    "ARTEFACT_DIR",
    "describe",
]

# Marker files that identify the repo root. `datasets.yaml` is the one that actually
# matters to us; the others make the search robust if the layout is ever reorganised.
_ROOT_MARKERS = ("shared/datasets.yaml", "environment.yml", ".git")

# Where datasets go on Colab, where there is no repo checkout.
_COLAB_DATA_DIR = Path("/content/aiep_data")


def in_colab() -> bool:
    """True when running inside a Google Colab runtime."""
    return "google.colab" in sys.modules or os.environ.get("COLAB_RELEASE_TAG") is not None


def _search_upwards(start: Path) -> Path | None:
    """Walk up from `start` looking for a directory containing a root marker."""
    for candidate in (start, *start.parents):
        for marker in _ROOT_MARKERS:
            if (candidate / marker).exists():
                return candidate
    return None


def repo_root() -> Path | None:
    """Locate the course repo root, or None if we're not inside a checkout.

    Search order:
      1. ``AIEP_REPO_ROOT`` environment variable (an escape hatch for odd setups).
      2. Upwards from the current working directory — the normal case, since Jupyter
         starts the kernel in the notebook's own directory.
      3. Upwards from this file — covers ``pip install -e shared/`` from a clone.

    Returns None on Colab-from-GitHub, where no checkout exists. Callers must handle
    that; it is not an error.
    """
    override = os.environ.get("AIEP_REPO_ROOT")
    if override:
        p = Path(override).expanduser().resolve()
        if p.exists():
            return p

    found = _search_upwards(Path.cwd().resolve())
    if found is not None:
        return found

    # `pip install -e` leaves the package inside the checkout, so this works there.
    # A non-editable install puts it in site-packages and this correctly finds nothing.
    return _search_upwards(Path(__file__).resolve().parent)


def cache_dir() -> Path:
    """Directory holding downloaded datasets. Created if missing.

    * Inside a checkout → ``<repo>/shared/data_cache``
    * On Colab with no checkout → ``/content/aiep_data``
    * Anywhere else → ``~/.aiep/data_cache``

    Override with the ``AIEP_DATA_DIR`` environment variable.
    """
    override = os.environ.get("AIEP_DATA_DIR")
    if override:
        d = Path(override).expanduser()
    else:
        root = repo_root()
        if root is not None:
            d = root / "shared" / "data_cache"
        elif in_colab():
            d = _COLAB_DATA_DIR
        else:
            d = Path.home() / ".aiep" / "data_cache"
    d.mkdir(parents=True, exist_ok=True)
    return d


def solutions_cache_dir() -> Path:
    """Reference artefacts, so a student who missed a day is not blocked tomorrow.

    See ``aiep.data.load_artefact`` — it falls back here when a lab-local artefact is
    missing. On Colab without a checkout this points at the same place as ``cache_dir``,
    since that is where a downloaded reference copy would land.
    """
    root = repo_root()
    if root is not None:
        d = root / "shared" / "solutions_cache"
        d.mkdir(parents=True, exist_ok=True)
        return d
    return cache_dir()


def notebook_dir() -> Path:
    """Directory of the running notebook.

    Jupyter sets the working directory to the notebook's own folder, so cwd is right
    in practice. Colab uses ``/content`` regardless of where the notebook came from,
    which is also the right place to write there.
    """
    return Path.cwd()


def artefact_dir() -> Path:
    """Lab-local ``artefacts/`` directory, created if missing.

    Everything a lab produces goes here: parquet, fitted models, metrics json, charts.
    It is gitignored — students regenerate it by running the lab.
    """
    d = notebook_dir() / "artefacts"
    d.mkdir(parents=True, exist_ok=True)
    return d


def describe() -> str:
    """One-line summary of where everything resolved to. Useful when a student is lost."""
    root = repo_root()
    return (
        f"colab={in_colab()} | repo={root or '(none)'} | "
        f"cache={cache_dir()} | artefacts={artefact_dir()}"
    )


def __getattr__(name: str):
    """Lazily expose ARTEFACT_DIR so importing this module never creates a directory.

    ``from aiep.paths import ARTEFACT_DIR`` is the ergonomic form used in every lab's
    setup cell, but evaluating it at import time would create ``artefacts/`` wherever
    the module happens to be imported — including during tooling runs. Deferring it to
    attribute access means the directory is created only when a notebook asks for it.
    """
    if name == "ARTEFACT_DIR":
        return artefact_dir()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
