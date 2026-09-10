"""Mask dilation utility: expand the white editable region before inference.

Expansion is a conditioning parameter, not a guarantee of successful removal.
"""

from __future__ import annotations

from PIL import Image, ImageFilter


def dilate_mask(mask: Image.Image, ratio: float) -> Image.Image:
    """把遮罩的白色（待編輯）區域按短邊比例往外膨脹。

    Args:
        mask: 任意 mode 的遮罩，白色 = 待編輯區域。
        ratio: 膨脹半徑相對於短邊的比例（例如 0.03 = 短邊的 3%）。<=0 時不處理。

    Returns:
        膨脹後的 ``L`` mode 遮罩；只增不減原本的白色像素。
    """
    m = mask.convert("L")
    if ratio <= 0:
        return m

    radius = round(min(m.size) * ratio)
    if radius < 1:
        return m

    # 以 3x3 MaxFilter 反覆膨脹，避免大 kernel rank filter 在大圖上過慢。
    for _ in range(radius):
        m = m.filter(ImageFilter.MaxFilter(3))
    return m
