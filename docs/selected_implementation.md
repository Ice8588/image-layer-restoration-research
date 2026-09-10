# Selected Implementation

以下通用工具用於研究中的遮罩處理與結果評估。

| 模組 | 功能 |
|---|---|
| [masks.py](../src/layer_restoration/masks.py) | 依短邊比例膨脹編輯區域 |
| [metrics.py](../src/layer_restoration/metrics.py) | ROI normalization、PSNR、兩種 SSIM 與 optional LPIPS |
| [tests](../tests/test_synth_layer_object_metrics.py) | 檢查 ROI 邊界、位置不變性、SSIM 與 mask 處理行為 |

## 執行方式

```bash
python -m pip install -e '.[test]'
python -m pytest
PYTHONPATH=src python examples/evaluate_pair.py reference.png candidate.png
```

測試可在 CPU 執行。歷史分析環境與評分設定見 [protocol](../assets/results/synthetic_v2/protocol.json)。

## 指標與輸入定義

`ssim_standard` 為 RGB windowed SSIM；`ssim` 是歷史 global grayscale 計算，兩者定義不同。Object-centric 與歷史 region scope 也應分開比較。

Legacy region metrics 對空 mask 回傳理想值，使用前應確認區域非空；`bbox_from_mask` 會拒絕空 mask。LPIPS 需額外相依與權重。
