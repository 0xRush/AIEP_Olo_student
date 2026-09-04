"""aiep — helper package for the Olo Academy AI Engineering Bootcamp.

Every lab's setup cell imports from here, so that the same notebook file runs unchanged
on a conda laptop, a bare pip install, and a fresh Google Colab runtime.

    from aiep.env import ensure, seed_everything, device
    from aiep.data import get_dataset
    from aiep.paths import ARTEFACT_DIR
    from aiep.checks import check, report

Submodules are imported lazily: importing ``aiep`` itself pulls in nothing heavy, so the
install-and-import step at the top of a Colab notebook stays fast.
"""

from __future__ import annotations

import importlib
import warnings
from typing import TYPE_CHECKING

__version__ = "1.0.0"

# NumPy wheels built against Apple's Accelerate framework raise spurious floating-point
# flags inside `matmul`, which surface as three RuntimeWarnings per iteration on every
# scikit-learn fit that reaches a dense matrix product — LogisticRegression and KMeans
# among them. The results are unaffected: the same fit under liblinear, which avoids that
# code path, returns coefficients identical to four decimal places.
#
# Every student on an Apple-silicon Mac would otherwise see a wall of red on a cell that
# worked. The filter is scoped to scikit-learn's own frames and to this one message, so a
# genuine overflow in a student's own NumPy code still warns.
warnings.filterwarnings(
    "ignore",
    message=".*encountered in matmul",
    category=RuntimeWarning,
    module=r"sklearn\..*",
)

_SUBMODULES = ("paths", "data", "env", "checks", "viz")

__all__ = [*_SUBMODULES, "__version__"]

if TYPE_CHECKING:  # for editors and type checkers only
    from . import checks, data, env, paths, viz  # noqa: F401


def __getattr__(name: str):
    if name in _SUBMODULES:
        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(__all__)
