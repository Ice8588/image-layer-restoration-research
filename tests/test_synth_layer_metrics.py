from __future__ import annotations

import importlib
import sys

import numpy as np

from layer_restoration.metrics import fid, psnr, ssim


def test_psnr_identical_is_inf():
    img = np.full((8, 8, 3), 100, dtype=np.uint8)
    assert psnr(img, img) == float("inf")


def test_psnr_decreases_with_error():
    a = np.zeros((8, 8, 3), dtype=np.uint8)
    b = np.full((8, 8, 3), 50, dtype=np.uint8)
    c = np.full((8, 8, 3), 100, dtype=np.uint8)
    assert psnr(a, b) > psnr(a, c)


def test_ssim_identical_is_one():
    img = np.random.default_rng(0).integers(0, 255, (16, 16, 3), dtype=np.uint8)
    assert abs(ssim(img, img) - 1.0) < 1e-6


def test_ssim_in_region_only():
    a = np.zeros((8, 8, 3), dtype=np.uint8)
    b = a.copy()
    b[0:4, 0:4] = 255
    region = np.zeros((8, 8), dtype=np.uint8)
    region[4:8, 4:8] = 255
    assert abs(ssim(a, b, region=region) - 1.0) < 1e-6


def test_metrics_module_has_no_top_level_lpips_or_torch_imports(monkeypatch):
    # 用 monkeypatch.delitem（測後自動復原）而非永久 pop：真 torch 一旦被踢出
    # sys.modules，之後的測試重新 import torch 會觸發 triton namespace 重複註冊而崩潰。
    monkeypatch.delitem(sys.modules, "layer_restoration.metrics", raising=False)
    monkeypatch.delitem(sys.modules, "lpips", raising=False)
    monkeypatch.delitem(sys.modules, "torch", raising=False)
    importlib.import_module("layer_restoration.metrics")
    assert "lpips" not in sys.modules
    assert "torch" not in sys.modules


def test_fid_placeholder_for_v0():
    import pytest

    with pytest.raises(NotImplementedError):
        fid("pred", "target")
