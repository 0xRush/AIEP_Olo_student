"""patchify, as written in W6D1. Imported by W6D3 and W6D4."""

import numpy as np


def patchify(image, patch_size):
    """Cut an (H, W, C) image into non-overlapping patches in reading order.

    Returns (n_patches, patch_size * patch_size * C). Used by W6D3 and W6D4.
    """
    # @todo en: Reshape into the five-axis grid, move the two patch-index axes to the front, and
    # @todo en: flatten. Raise a readable error when the size is not divisible by the patch size.
    # @todo ar: أعِد التشكيل إلى الشبكة ذات المحاور الخمسة، وقدّم محورَي فهرس الرقعة، ثم اطوِ.
    # @todo ar: وارفع خطأً مفهومًا حين لا يقبل المقاس القسمة على مقاس الرقعة.
    # @strip:start
    array = np.asarray(image)
    if array.ndim == 2:
        array = array[:, :, None]
    height, width, channels = array.shape
    if height % patch_size or width % patch_size:
        raise ValueError(f"{height}x{width} does not divide by patch size {patch_size} — "
                         f"a ViT needs an exact grid, so resize before you patchify")

    rows, cols = height // patch_size, width // patch_size
    grid = array.reshape(rows, patch_size, cols, patch_size, channels)
    grid = grid.transpose(0, 2, 1, 3, 4)          # (rows, cols, p, p, C) — reading order
    return grid.reshape(rows * cols, patch_size * patch_size * channels)
    # @strip:end
