# Selected Implementation

這是研究使用過的通用工具切片，保留既有可驗證行為，不包含完整生成服務或模型內部新方法。

| 模組 | 內容 | 邊界 |
|---|---|---|
| [masks.py](../src/layer_restoration/masks.py) | 按短邊比例膨脹白色編輯區域 | 可重現的 conditioning helper；不保證補全成功 |
| [metrics.py](../src/layer_restoration/metrics.py) | ROI normalization、PSNR、兩種 SSIM、optional LPIPS | object-centric 與 legacy region scope 不能混比 |
| [tests](../tests/test_synth_layer_object_metrics.py) | ROI 邊界、位置不變性、SSIM 與 mask regressions | CPU contract validation，不是 GPU 品質驗證 |

```bash
python -m pip install -e '.[test]'
python -m pytest
PYTHONPATH=src python examples/evaluate_pair.py reference.png candidate.png
```

測試不需要 GPU；本次未安裝新相依。依照 [protocol](../assets/results/synthetic_v2/protocol.json) 對照歷史分析環境；pyproject 的相依不是完整重現鎖定檔。

`ssim_standard` 為 RGB windowed SSIM；`ssim` 是歷史 global grayscale 計算，不能互換。Legacy region metrics 對空 mask 回傳理想值，使用者應先驗證非空區域；`bbox_from_mask` 會拒絕空 mask。`fid` 是明確未實作的歷史 placeholder，不列為已提供評估能力。LPIPS 路徑需額外相依與權重，本次不下載或重新計分。
