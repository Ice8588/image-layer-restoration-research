# 企業合作資料 / Private Industry Dataset

企業合作資料用來補充合成實驗，觀察 QA 選圖、推論步數與 Flow scale 在實際資料上的表現。基於合作資料保密限制，本頁僅呈現允許公開的 aggregate quantitative results。

## 主要觀察

| 實驗 | 主要結果 | 研究判讀 |
|---|---|---|
| VLM QA | V7 strict stage pass 86.8%，V3 為 79.8%；V7 未通過關鍵負例檢查 | 選圖收益為 Diagnostic Only，替換決策為 Negative，保留 V3 |
| Inference steps | 20／30／40 steps 平均推論時間為 36.69／54.66／66.48 秒；三個品質指標沒有一致排序 | 較少 steps 在當次環境較快；品質仍待人工評估，維持 Inconclusive |
| Flow scale | +8 的 LPIPS CI 跨 0；+32、−2、−4 等設定呈現指標退化 | 極端 scale 未呈現穩定增益；屬於 pseudo-GT 診斷，維持 Diagnostic Only |

以下各表使用不同評估協定：QA 分類與選圖、圖像品質、推論時間分開判讀，也不與 Synthetic V2／V3 跨表排名。

## Frozen QA replay — Diagnostic Only

同一批 342 個既有生成候選，由人工完成標註；binary classification 排除 human-uncertain，VLM unavailable 不直接當作 human fail。下表保留各版本整體表現，不能拿 classification accuracy 當生成可用率。

| QA version | Accuracy | Balanced accuracy | Pass recall | Reject detection | Unavailable |
|---|---:|---:|---:|---:|---:|
| V3 | 81.3% | 63.4% | 92.0% | 34.9% | 0 |
| V4 | 64.9% | 72.4% | 60.3% | 84.5% | 33 |
| V5 | 67.4% | 71.4% | 65.2% | 77.6% | 13 |
| V6 | 83.1% | 63.9% | 94.5% | 33.3% | 0 |
| V7 | 77.4% | 75.1% | 78.8% | 71.4% | 1 |

First-round selector 的 strict stage pass 以所有 114 個 stage 為分母，abstain 不算 pass：

| QA version | Strict stage pass |
|---|---:|
| V3 | 79.8% |
| V4 | 7.0% |
| V5 | 12.3% |
| V6 — simulated selector | 79.8% |
| V7 | 86.8% |

V7 相對 V3 為 +7.0 percentage points（原報告近似 95% CI：+2.3 至 +11.7）。但預先設定的關鍵負例檢查（sentinel admission）未通過，選圖收益仍僅作診斷；V6 selector 僅為 lowest-index automatic-pass simulation。V4 unique ordinal selection 遇 tie 可 abstain，且沒有預先設定的替換標準。**保留 V3；替換決策維持 Negative，選圖收益維持 Diagnostic Only。** 比較固定相同生成候選，以隔離 QA 版本差異。

## Inference-step comparison — Inconclusive

Qwen Image Edit 2511 NoiseMask 固定輸入協定，每個設定 38 個 removal samples × 5 seeds = 190 outputs。下表先在 sample 內平均 seeds，再取 sample macro；PSNR、SSIM、LPIPS 都量測 direct-reveal 區域。這個局部可見參考不是完整 hidden-region artist-authored GT，不能據此判定完整 amodal completion。其量測範圍不同於 Synthetic V2 object-centric normalization，不能跨表直接排名。

| Steps | PSNR ↑ | SSIM ↑ | LPIPS ↓ | Mean server inference time ↓ |
|---|---:|---:|---:|---:|
| 20 | 19.7555 | 0.6775 | 0.0245 | 36.69 s |
| 30 | 19.5645 | 0.6742 | 0.0239 | 54.66 s |
| 40 | 19.5006 | 0.6658 | 0.0244 | 66.48 s |

時間僅為當次環境的 server inference，非 end-to-end latency，未含完整分層、傳輸與 QA。正式人工評估尚未完成，品質結論維持 Inconclusive。

## Signed / extreme Flow scale — Diagnostic Only

此分析涵蓋 912 筆 metric rows，定位為探索性 pseudo-GT calibration，不用於正式採用決策，人工評估仍待完成。下表為 treatment minus scale 0；先平均 sample 內 seeds，再平均來源群內 samples，最後各來源群等權。下表呈現全體 macro。

| Scale | LPIPS Δ ↓ | 95% CI | PSNR Δ dB ↑ | SSIM Δ ↑ |
|---|---:|---|---:|---:|
| +8 | -0.000501 | [-0.006278, +0.004954] | -0.6692 | -0.025458 |
| +16 | +0.005224 | [-0.001661, +0.012080] | -2.7367 | -0.069748 |
| +32 | +0.014663 | [+0.006355, +0.025521] | -5.4273 | -0.193842 |
| -0.5 | +0.001244 | [+0.000227, +0.002480] | -0.1322 | -0.001232 |
| -1 | +0.009744 | [+0.003246, +0.017640] | -0.9026 | -0.020316 |
| -2 | +0.071691 | [+0.048086, +0.101065] | -12.0015 | -0.564771 |
| -4 | +0.083358 | [+0.057467, +0.114360] | -14.3019 | -0.681353 |

上述代理指標供探索性診斷，實際美術可用性仍待人工確認。Step-window 在已測條件下的 Negative，以及尚缺配對品質證據的 FlowEdit transport Inconclusive，分別保留在 [完整 Flow 實驗頁](experiments/06_flow_editing.md)。

完整研究脈絡見 [研究時間軸](experiments/00_research_timeline.md)。
