"""mask 膨脹 helper 的 CPU 測試。"""

from __future__ import annotations

import numpy as np
from PIL import Image

from layer_restoration.masks import dilate_mask


def _white_count(mask: Image.Image) -> int:
    return int((np.asarray(mask.convert("L")) > 127).sum())


def _centered_square_mask(size: int = 100, block: int = 10) -> Image.Image:
    arr = np.zeros((size, size), dtype=np.uint8)
    lo = (size - block) // 2
    arr[lo : lo + block, lo : lo + block] = 255
    return Image.fromarray(arr, mode="L")


def test_dilate_mask_grows_white_region():
    mask = _centered_square_mask()
    before = _white_count(mask)
    dilated = dilate_mask(mask, 0.05)
    after = _white_count(dilated)
    assert after > before


def test_dilate_mask_keeps_original_white_pixels():
    mask = _centered_square_mask()
    original = np.asarray(mask) > 127
    dilated = np.asarray(dilate_mask(mask, 0.05).convert("L")) > 127
    # 膨脹只增不減：原本白的地方仍然是白的。
    assert bool((dilated & original).sum() == original.sum())


def test_dilate_mask_ratio_zero_is_noop():
    mask = _centered_square_mask()
    assert _white_count(dilate_mask(mask, 0.0)) == _white_count(mask)


def test_dilate_mask_larger_ratio_grows_more():
    mask = _centered_square_mask()
    small = _white_count(dilate_mask(mask, 0.03))
    large = _white_count(dilate_mask(mask, 0.08))
    assert large > small


def test_dilate_mask_returns_L_mode():
    mask = _centered_square_mask().convert("1")
    assert dilate_mask(mask, 0.05).mode == "L"
