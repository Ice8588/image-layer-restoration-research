from __future__ import annotations

import numpy as np
import pytest

from layer_restoration.metrics import (
    bbox_from_mask,
    normalize_object_roi,
    ssim_standard,
)


def test_bbox_from_mask_returns_max_exclusive_bounds() -> None:
    mask = np.zeros((20, 30), dtype=np.uint8)
    mask[3, 6] = 127
    mask[4:12, 7:19] = 128

    assert bbox_from_mask(mask) == (7, 4, 19, 12)


def test_bbox_from_mask_rejects_empty_mask() -> None:
    mask = np.zeros((20, 30), dtype=np.uint8)

    with pytest.raises(ValueError, match="^object mask is empty$"):
        bbox_from_mask(mask)


def test_normalize_object_roi_is_position_invariant() -> None:
    object_rgb = np.arange(12 * 18 * 3, dtype=np.uint8).reshape(12, 18, 3)
    image_a = np.zeros((64, 64, 3), dtype=np.uint8)
    image_b = np.zeros((64, 64, 3), dtype=np.uint8)
    mask_a = np.zeros((64, 64), dtype=np.uint8)
    mask_b = np.zeros((64, 64), dtype=np.uint8)
    image_a[0:12, 0:18] = object_rgb
    image_b[40:52, 36:54] = object_rgb
    mask_a[0:12, 0:18] = 255
    mask_b[40:52, 36:54] = 255

    normalized_a = normalize_object_roi(image_a, mask_a)
    normalized_b = normalize_object_roi(image_b, mask_b)

    assert normalized_a.shape == (256, 256, 3)
    np.testing.assert_array_equal(normalized_a, normalized_b)


def test_normalize_object_roi_preserves_aspect_ratio_and_centers_letterbox() -> None:
    image = np.zeros((64, 64, 3), dtype=np.uint8)
    mask = np.zeros((64, 64), dtype=np.uint8)
    image[20:30, 15:35] = (255, 64, 32)
    mask[20:30, 15:35] = 255

    normalized = normalize_object_roi(image, mask)
    object_pixels = normalized[..., 0] >= 128
    x0, y0, x1, y1 = bbox_from_mask(object_pixels.astype(np.uint8) * 255)
    object_width = x1 - x0
    object_height = y1 - y0

    assert object_width / object_height == pytest.approx(2.0, abs=0.03)
    assert abs(x0 - (256 - x1)) <= 1
    assert abs(y0 - (256 - y1)) <= 1
    assert np.all(normalized[0] == 0)
    assert np.all(normalized[-1] == 0)


def test_ssim_standard_returns_one_for_identical_rgb_images() -> None:
    rng = np.random.default_rng(7)
    image = rng.integers(0, 256, size=(256, 256, 3), dtype=np.uint8)

    assert ssim_standard(image, image) == pytest.approx(1.0)


def test_ssim_standard_rejects_shape_mismatch() -> None:
    pred = np.zeros((256, 256, 3), dtype=np.uint8)
    target = np.zeros((128, 256, 3), dtype=np.uint8)

    with pytest.raises(ValueError):
        ssim_standard(pred, target)
