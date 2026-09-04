"""Bilingual sanity checks for the end of every lab.

Not an autograder. The point is that a student — and a TA walking the room — can see at
a glance whether the lab worked, and read *why* it didn't in their own language.

    from aiep.checks import check, report

    check(0.80 < acc <= 1.0,
          f"accuracy should be above 0.80, got {acc:.3f}",
          f"يجب أن تتجاوز الدقة ٠٫٨٠، والقيمة الحالية {acc:.3f}")

    report()

``check`` records the result and keeps going, so a student sees every failure at once
instead of fixing them one exception at a time. ``report`` prints the table and raises
if anything failed.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

__all__ = ["check", "check_close", "check_shape", "report", "reset", "results"]


@dataclass
class _Result:
    passed: bool
    message_en: str
    message_ar: str
    error: str | None = None


#: Module-level so a notebook can call check() across several cells before report().
_RESULTS: list[_Result] = []


def reset() -> None:
    """Clear recorded results. Called automatically by ``report``."""
    _RESULTS.clear()


def results() -> list[_Result]:
    """The results recorded since the last reset. Mostly useful in tests."""
    return list(_RESULTS)


def check(condition: Any, message_en: str, message_ar: str) -> bool:
    """Record one check. Returns whether it passed; never raises.

    Args:
        condition: anything truthy. Evaluating it must not raise — if it might,
            compute it on the line above.
        message_en: what is wrong, in English. **Include the actual value.**
        message_ar: the same, in Arabic.

    A good message names the value: ``f"accuracy should exceed 0.80, got {acc:.3f}"``.
    A message like "check failed" tells the student nothing.
    """
    try:
        passed = bool(condition)
        error = None
    except Exception as exc:  # a check that explodes is a failed check, not a crash
        passed = False
        error = f"{type(exc).__name__}: {exc}"

    _RESULTS.append(_Result(passed, message_en, message_ar, error))
    return passed


def check_close(
    actual: float,
    expected: float,
    message_en: str,
    message_ar: str,
    *,
    tol: float = 1e-6,
) -> bool:
    """Float comparison with a tolerance. Never compare floats with ``==``."""
    try:
        ok = math.isclose(float(actual), float(expected), abs_tol=tol, rel_tol=tol)
    except Exception:
        ok = False
    detail = f" (expected ≈{expected}, got {actual})"
    return check(ok, message_en + detail, message_ar + detail)


def check_shape(obj: Any, expected: tuple, message_en: str, message_ar: str) -> bool:
    """Shape check for a NumPy array, torch tensor, or pandas DataFrame.

    ``None`` in `expected` means "any size on this axis":

        check_shape(X_train, (None, 12), "X_train should have 12 columns", "…")
    """
    shape = getattr(obj, "shape", None)
    if shape is None:
        return check(False, f"{message_en} (object has no .shape)", f"{message_ar} (لا يملك .shape)")

    ok = len(shape) == len(expected) and all(
        e is None or int(a) == int(e) for a, e in zip(shape, expected)
    )
    want = "×".join("*" if e is None else str(e) for e in expected)
    got = "×".join(str(s) for s in shape)
    detail = f" (expected {want}, got {got})"
    return check(ok, message_en + detail, message_ar + detail)


def report(*, raise_on_failure: bool = True) -> bool:
    """Print the results table and clear them. Returns True if everything passed.

    Raises AssertionError on failure by default, so a notebook run headlessly (in
    ``tools/verify_notebooks.py`` or nbconvert) fails loudly rather than printing a
    sad face into a cell nobody reads.
    """
    if not _RESULTS:
        print("⚠️  No checks were recorded. Did you call check() before report()?")
        print("⚠️  لم تُسجَّل أي فحوصات. هل استدعيت check() قبل report()؟")
        return True

    passed = [r for r in _RESULTS if r.passed]
    failed = [r for r in _RESULTS if not r.passed]

    line = "─" * 66
    print(line)
    for result in _RESULTS:
        if result.passed:
            print(f"  ✓  {result.message_en}")
        else:
            print(f"  ✗  {result.message_en}")
            print(f"     {result.message_ar}")
            if result.error:
                print(f"     → {result.error}")
    print(line)

    total = len(_RESULTS)
    if failed:
        print(f"  {len(passed)}/{total} checks passed — {len(failed)} still to fix.")
        print(f"  اجتاز {len(passed)} من {total} — بقي {len(failed)} للإصلاح.")
    else:
        print(f"  ✅ All {total} checks passed. / اجتزت جميع الفحوصات ({total}).")
    print(line)

    ok = not failed
    reset()

    if failed and raise_on_failure:
        raise AssertionError(
            f"{len(failed)} sanity check(s) failed — see the output above. "
            f"فشل {len(failed)} من الفحوصات، راجع المخرجات أعلاه."
        )
    return ok
