"""Plot helpers shared across labs.

Two jobs:

1. **Consistency** — every chart in the course looks like it belongs to the same course,
   and every axis is labelled. An unlabelled axis is a bug.
2. **Arabic safety** — matplotlib cannot shape Arabic text without extra fonts and a
   bidi library, and when it fails it fails *silently*, rendering disconnected letters
   backwards. So: **plot labels are English.** The Arabic explanation goes in the
   markdown cell above the chart. See docs/Bilingual_Style_Guide.md §8.
"""

from __future__ import annotations

from typing import Any, Sequence

__all__ = [
    "use_course_style",
    "PALETTE",
    "plot_confusion_matrix",
    "plot_training_curves",
    "plot_grid",
    "savefig",
]

#: Colour-blind-safe categorical palette. Used course-wide so "class 0" is the same
#: colour in week 2 and in week 8.
PALETTE = [
    "#1f77b4",  # blue
    "#ff7f0e",  # orange
    "#2ca02c",  # green
    "#d62728",  # red
    "#9467bd",  # purple
    "#8c564b",  # brown
    "#17becf",  # cyan
]


def use_course_style() -> None:
    """Apply the course-wide matplotlib defaults. Safe to call more than once."""
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    plt.rcParams.update(
        {
            "figure.figsize": (7, 4.5),
            "figure.dpi": 110,
            "savefig.dpi": 150,
            "savefig.bbox": "tight",
            "axes.grid": True,
            "grid.alpha": 0.25,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.titlesize": 12,
            "axes.labelsize": 10,
            "legend.frameon": False,
            "font.size": 10,
            "axes.prop_cycle": mpl.cycler(color=PALETTE),
        }
    )


def plot_confusion_matrix(
    y_true: Sequence,
    y_pred: Sequence,
    labels: Sequence[str] | None = None,
    *,
    normalize: bool = False,
    title: str = "Confusion matrix",
    ax: Any = None,
):
    """Confusion matrix with the counts written into the cells.

    The numbers in the cells matter more than the colour — week 2's whole lesson is
    reading the four cells, so they are always annotated.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(y_true, y_pred)
    display = cm.astype(float) / cm.sum(axis=1, keepdims=True) if normalize else cm

    if ax is None:
        _, ax = plt.subplots(figsize=(4.5, 4))

    image = ax.imshow(display, cmap="Blues")
    ticks = np.arange(cm.shape[0])
    names = list(labels) if labels is not None else [str(i) for i in ticks]

    ax.set_xticks(ticks, names, rotation=45, ha="right")
    ax.set_yticks(ticks, names)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title(title)
    ax.grid(False)

    threshold = display.max() / 2
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            text = f"{display[i, j]:.2f}" if normalize else f"{cm[i, j]:d}"
            ax.text(
                j, i, text,
                ha="center", va="center",
                color="white" if display[i, j] > threshold else "black",
            )

    ax.figure.colorbar(image, ax=ax, fraction=0.046)
    return ax


def plot_training_curves(
    history: dict[str, Sequence[float]],
    *,
    title: str = "Training curves",
    ax: Any = None,
):
    """Plot loss/metric curves from a ``{"train_loss": [...], "val_loss": [...]}`` dict.

    Validation series (any key containing "val") are dashed, so the train/validation gap
    — the thing students are meant to read — is visible without checking the legend.
    """
    import matplotlib.pyplot as plt

    if ax is None:
        _, ax = plt.subplots()

    for name, values in history.items():
        ax.plot(
            range(1, len(values) + 1),
            values,
            label=name,
            linestyle="--" if "val" in name.lower() else "-",
        )

    ax.set_xlabel("Epoch")
    ax.set_ylabel("Value")
    ax.set_title(title)
    ax.legend()
    return ax


def plot_grid(
    images: Sequence,
    labels: Sequence | None = None,
    *,
    n_cols: int = 8,
    title: str | None = None,
    cmap: str = "gray",
):
    """Grid of images, for MNIST-style samples, augmentation before/after, and filters."""
    import matplotlib.pyplot as plt
    import numpy as np

    n = len(images)
    n_cols = min(n_cols, n)
    n_rows = int(np.ceil(n / n_cols))

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 1.4, n_rows * 1.6))
    axes = np.atleast_1d(axes).ravel()

    for i, ax in enumerate(axes):
        ax.axis("off")
        if i >= n:
            continue
        img = np.asarray(images[i])
        if img.ndim == 3 and img.shape[0] in (1, 3):  # torch CHW → HWC
            img = img.transpose(1, 2, 0)
        img = img.squeeze()
        ax.imshow(img, cmap=cmap if img.ndim == 2 else None)
        if labels is not None:
            ax.set_title(str(labels[i]), fontsize=8)

    if title:
        fig.suptitle(title)
    fig.tight_layout()
    return fig


def savefig(fig, filename: str):
    """Save a figure into this notebook's ``artefacts/`` and return the path."""
    from .paths import artefact_dir

    path = artefact_dir() / filename
    fig.savefig(path)
    print(f"🖼️  Saved {path}")
    return path
