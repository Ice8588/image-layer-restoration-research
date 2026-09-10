"""Image metrics for synth_layer evaluation."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity


def bbox_from_mask(mask: np.ndarray) -> tuple[int, int, int, int]:
    """Return the max-exclusive bounding box of a non-empty binary mask."""
    if mask.ndim != 2:
        raise ValueError("mask must be a 2D array")
    ys, xs = np.nonzero(mask >= 128)
    if xs.size == 0:
        raise ValueError("object mask is empty")
    return int(xs.min()), int(ys.min()), int(xs.max() + 1), int(ys.max() + 1)


def normalize_object_roi(
    image: np.ndarray,
    mask: np.ndarray,
    *,
    output_size: int = 256,
    padding_ratio: float = 0.05,
    min_padding: int = 8,
    max_padding: int = 64,
) -> np.ndarray:
    """Crop a padded object ROI and letterbox it onto a black square canvas."""
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("image must be RGB")
    if mask.ndim != 2:
        raise ValueError("mask must be a 2D array")
    if image.shape[:2] != mask.shape:
        raise ValueError("image and mask spatial shapes must match")

    x0, y0, x1, y1 = bbox_from_mask(mask)
    width, height = x1 - x0, y1 - y0
    padding = round(max(width, height) * padding_ratio)
    padding = max(min_padding, min(max_padding, padding))

    requested_x0, requested_y0 = x0 - padding, y0 - padding
    requested_x1, requested_y1 = x1 + padding, y1 + padding
    crop_width = requested_x1 - requested_x0
    crop_height = requested_y1 - requested_y0
    crop = np.zeros((crop_height, crop_width, 3), dtype=np.uint8)

    source_x0 = max(0, requested_x0)
    source_y0 = max(0, requested_y0)
    source_x1 = min(image.shape[1], requested_x1)
    source_y1 = min(image.shape[0], requested_y1)
    dest_x0 = source_x0 - requested_x0
    dest_y0 = source_y0 - requested_y0
    crop[
        dest_y0 : dest_y0 + (source_y1 - source_y0),
        dest_x0 : dest_x0 + (source_x1 - source_x0),
    ] = image[source_y0:source_y1, source_x0:source_x1]

    scale = min(output_size / crop_width, output_size / crop_height)
    resized_width = max(1, round(crop_width * scale))
    resized_height = max(1, round(crop_height * scale))
    resized = Image.fromarray(crop).resize(
        (resized_width, resized_height),
        Image.Resampling.LANCZOS,
    )
    canvas = Image.new("RGB", (output_size, output_size), color="black")
    canvas.paste(
        resized,
        ((output_size - resized_width) // 2, (output_size - resized_height) // 2),
    )
    return np.asarray(canvas)


def ssim_standard(pred: np.ndarray, target: np.ndarray) -> float:
    """Compute standard RGB SSIM with fixed benchmark parameters."""
    if pred.shape != target.shape:
        raise ValueError("pred and target shapes must match")
    if pred.ndim != 3 or pred.shape[2] != 3:
        raise ValueError("pred and target must be RGB")
    return float(
        structural_similarity(
            pred,
            target,
            data_range=255,
            channel_axis=2,
            gaussian_weights=True,
            sigma=1.5,
            use_sample_covariance=False,
        )
    )


def _region_values(a: np.ndarray, b: np.ndarray, region: np.ndarray | None) -> tuple[np.ndarray, np.ndarray]:
    if region is None:
        return a.reshape(-1), b.reshape(-1)
    mask = region >= 128
    if a.ndim == 3:
        mask = np.repeat(mask[..., None], a.shape[2], axis=2)
    return a[mask], b[mask]


def psnr(pred: np.ndarray, target: np.ndarray, *, region: np.ndarray | None = None) -> float:
    pred_values, target_values = _region_values(
        pred.astype(np.float64),
        target.astype(np.float64),
        region,
    )
    mse = float(np.mean((pred_values - target_values) ** 2)) if pred_values.size else 0.0
    if mse == 0.0:
        return float("inf")
    return float(10.0 * np.log10((255.0**2) / mse))


def _gray_float(image: np.ndarray) -> np.ndarray:
    values = image.astype(np.float64)
    if values.ndim == 3:
        values = values.mean(axis=2)
    return values


def ssim(pred: np.ndarray, target: np.ndarray, *, region: np.ndarray | None = None) -> float:
    x = _gray_float(pred)
    y = _gray_float(target)
    if region is None:
        x = x.reshape(-1)
        y = y.reshape(-1)
    else:
        mask = region >= 128
        x = x[mask]
        y = y[mask]
    if x.size == 0:
        return 1.0

    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2
    mean_x = float(x.mean())
    mean_y = float(y.mean())
    var_x = float(x.var())
    var_y = float(y.var())
    cov_xy = float(np.mean((x - mean_x) * (y - mean_y)))
    numerator = (2 * mean_x * mean_y + c1) * (2 * cov_xy + c2)
    denominator = (mean_x**2 + mean_y**2 + c1) * (var_x + var_y + c2)
    return float(numerator / denominator)


def lpips_distance(
    pred: np.ndarray,
    target: np.ndarray,
    *,
    region: np.ndarray | None = None,
    net: str = "alex",
) -> float:
    import lpips  # noqa: PLC0415
    import torch  # noqa: PLC0415

    pred_rgb = pred.astype(np.float32, copy=True)
    target_rgb = target.astype(np.float32, copy=True)
    if region is not None:
        mask = region >= 128
        pred_rgb[~mask] = 0.0
        target_rgb[~mask] = 0.0

    def to_tensor(image: np.ndarray):
        return torch.from_numpy(image).permute(2, 0, 1).unsqueeze(0) / 127.5 - 1.0

    model = lpips.LPIPS(net=net)
    with torch.no_grad():
        value = model(to_tensor(pred_rgb), to_tensor(target_rgb))
    return float(value.item())


def lpips_region_scorer(net: str = "alex"):
    """回傳 occluded-region LPIPS 計分函式，LPIPS 模型只載一次（批量評分避免逐張重建權重）。

    回傳的 score(pred, target, region=None) 語意與 lpips_distance 相同（region 外歸零）。
    """
    import lpips  # noqa: PLC0415
    import torch  # noqa: PLC0415

    model = lpips.LPIPS(net=net)

    def _to_tensor(image: np.ndarray):
        return torch.from_numpy(image).permute(2, 0, 1).unsqueeze(0) / 127.5 - 1.0

    def score(pred: np.ndarray, target: np.ndarray, region: np.ndarray | None = None) -> float:
        pred_rgb = pred.astype(np.float32, copy=True)
        target_rgb = target.astype(np.float32, copy=True)
        if region is not None:
            mask = region >= 128
            pred_rgb[~mask] = 0.0
            target_rgb[~mask] = 0.0
        with torch.no_grad():
            return float(model(_to_tensor(pred_rgb), _to_tensor(target_rgb)).item())

    return score


def fid(pred_dir: str | Path, target_dir: str | Path) -> float:
    raise NotImplementedError("fid is planned for v1 and is not implemented in the CPU v0 core")
