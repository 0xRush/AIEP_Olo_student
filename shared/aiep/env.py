"""Environment setup: install what's missing, seed everything, find the device.

Used by every lab's setup cell. The goal is that the same three lines work on a conda
laptop, a bare pip install, and a fresh Colab runtime.
"""

from __future__ import annotations

import importlib.util
import os
import random
import subprocess
import sys

__all__ = ["ensure", "seed_everything", "device", "require_key", "versions", "SEED"]

#: Course-wide random seed. Labs do not change this without saying why in the markdown.
SEED = 42

# pip name → import name, for the cases where they differ. Extend as labs need it.
_PIP_TO_IMPORT = {
    "scikit-learn": "sklearn",
    "sentence-transformers": "sentence_transformers",
    "faiss-cpu": "faiss",
    "python-dotenv": "dotenv",
    "opencv-python": "cv2",
    "pillow": "PIL",
    "python-graphviz": "graphviz",
    "imbalanced-learn": "imblearn",
    "rank-bm25": "rank_bm25",
    "python-multipart": "multipart",
    "pyyaml": "yaml",
}


def ensure(*packages: str, quiet: bool = True) -> None:
    """Pip-install any of `packages` that isn't importable. Idempotent and cheap.

    Pass the **pip** name (``"scikit-learn"``, not ``"sklearn"``). On a properly built
    conda env this does nothing at all; on Colab it installs the two or three things
    that runtime is missing.

    Deliberately not a full dependency manager — it exists so a notebook opened cold in
    Colab runs without the student reading an install guide.
    """
    missing = [
        pkg
        for pkg in packages
        if importlib.util.find_spec(_PIP_TO_IMPORT.get(pkg, pkg.replace("-", "_"))) is None
    ]
    if not missing:
        return

    print(f"📦 Installing: {', '.join(missing)}")
    cmd = [sys.executable, "-m", "pip", "install", *(["-q"] if quiet else []), *missing]
    subprocess.check_call(cmd)


def seed_everything(seed: int = SEED) -> int:
    """Seed Python, NumPy, and (if installed) PyTorch. Returns the seed.

    This makes a run reproducible on the same machine. It does **not** make results
    identical across machines or library versions — GPU kernels and BLAS threading
    differ. Say that to students the first time a classmate gets 0.871 and they get
    0.869: reproducible does not mean universal.
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)

    try:
        import numpy as np

        np.random.seed(seed)
    except ImportError:
        pass

    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass

    return seed


def device() -> str:
    """Return the best available torch device as a string: 'cuda', 'mps', or 'cpu'.

    Every lab must complete on 'cpu' inside the slot. This is here so a student with a
    GPU or an Apple-silicon Mac gets the speed-up without editing anything.
    """
    try:
        import torch
    except ImportError:
        return "cpu"

    if torch.cuda.is_available():
        return "cuda"
    if getattr(torch.backends, "mps", None) is not None and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def require_key(name: str = "OPENROUTER_API_KEY") -> str:
    """Return an API key from the environment, or raise a readable bilingual error.

    Loads a local ``.env`` first if python-dotenv is available. Never prints the key —
    notebook outputs get committed and shared.
    """
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass

    value = os.environ.get(name)
    if value:
        return value

    raise RuntimeError(
        f"\n"
        f"Missing API key: {name}\n"
        f"مفتاح الواجهة البرمجية غير موجود: {name}\n"
        f"\n"
        f"  1. Get a free key at https://openrouter.ai/keys (no payment method needed).\n"
        f"     احصل على مفتاح مجاني من https://openrouter.ai/keys (بدون وسيلة دفع).\n"
        f"  2. Create a .env file next to this notebook containing:\n"
        f"     أنشئ ملف .env بجوار هذا الدفتر يحتوي على:\n"
        f"         {name}=your-key-here\n"
        f"  3. Re-run this cell. / أعد تشغيل الخلية.\n"
        f"\n"
        f"  On Colab, use the key manager in the left sidebar (🔑) instead of a .env file.\n"
        f"  على Colab استخدم مدير المفاتيح في الشريط الجانبي (🔑) بدلًا من ملف .env.\n"
    )


def versions() -> str:
    """One-line version summary. Paste this into a bug report before asking for help."""
    parts = [f"python {sys.version.split()[0]}"]
    for module_name, label in [
        ("numpy", "numpy"),
        ("pandas", "pandas"),
        ("sklearn", "scikit-learn"),
        ("torch", "torch"),
        ("transformers", "transformers"),
    ]:
        try:
            module = __import__(module_name)
            parts.append(f"{label} {module.__version__}")
        except Exception:
            pass
    return " | ".join(parts)
