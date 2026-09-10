# 企業合作資料 / Private Industry Dataset

本頁只保存 aggregate quantitative results。原始圖像、result image、mask、crop、個別 case、內部 metadata、企業與人員名稱均不公開；不提供逐筆 records、影像 hash、來源時間線或可連回個例的分組鍵。底層證據與數值對照留在非公開 audit，因此外部讀者無法獨立重算本頁結果。

數字只代表各自固定協定。QA classifier、selector、影像品質與執行時間不能互相替代；公開 aggregate 不構成新的 promotion。

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

V7 相對 V3 為 +7.0 percentage points（原報告近似 95% CI：+2.3 至 +11.7）。但 preregistered sentinel admission 未通過，仍只是 diagnostic；V6 selector 僅為 lowest-index automatic-pass simulation。V4 unique ordinal selection 遇 tie 可 abstain，且沒有 preregistered replacement gate。**Retain V3；replacement decision 維持 Negative，selector gain 維持 Diagnostic Only。** 本比較沒有重跑 Naming 或生成，也不公開小型 sentinel／control subgroup 數字。

## Inference-step comparison — Inconclusive

Qwen Image Edit 2511 NoiseMask 固定輸入協定，每個設定 38 個 removal samples × 5 seeds = 190 outputs。下表先在 sample 內平均 seeds，再取 sample macro；PSNR、SSIM、LPIPS 都量測 direct-reveal 區域。這個局部可見參考不是完整 hidden-region artist-authored GT，不能據此判定完整 amodal completion。不同於 Synthetic V2 object-centric normalization，禁止跨表排名。

| Steps | PSNR ↑ | SSIM ↑ | LPIPS ↓ | Mean server inference time ↓ |
|---|---:|---:|---:|---:|
| 20 | 19.7555 | 0.6775 | 0.0245 | 36.69 s |
| 30 | 19.5645 | 0.6742 | 0.0239 | 54.66 s |
| 40 | 19.5006 | 0.6658 | 0.0244 | 66.48 s |

時間僅為當次環境的 server inference，非 end-to-end latency，未含完整分層、傳輸與 QA。正式 operator QA 仍 pending；較低成本不代表品質已通過，結論維持 Inconclusive。

## Signed / extreme Flow scale — Diagnostic Only

912 筆 metric rows 的探索性 pseudo-GT calibration，沒有預先定義 promotion gate，operator QA pending。下表為 treatment minus scale 0；先平均 sample 內 seeds，再平均來源群內 samples，最後各來源群等權。只保留全體 macro，不公開來源群數值或樣本勝負 records。

| Scale | LPIPS Δ ↓ | 95% CI | PSNR Δ dB ↑ | SSIM Δ ↑ |
|---|---:|---|---:|---:|
| +8 | -0.000501 | [-0.006278, +0.004954] | -0.6692 | -0.025458 |
| +16 | +0.005224 | [-0.001661, +0.012080] | -2.7367 | -0.069748 |
| +32 | +0.014663 | [+0.006355, +0.025521] | -5.4273 | -0.193842 |
| -0.5 | +0.001244 | [+0.000227, +0.002480] | -0.1322 | -0.001232 |
| -1 | +0.009744 | [+0.003246, +0.017640] | -0.9026 | -0.020316 |
| -2 | +0.071691 | [+0.048086, +0.101065] | -12.0015 | -0.564771 |
| -4 | +0.083358 | [+0.057467, +0.114360] | -14.3019 | -0.681353 |

這是 automatic diagnostic proxy，不能宣稱 operator usability。Step-window 的 bounded Negative 與尚缺證據的 FlowEdit transport Inconclusive 判定，繼續保留在 [完整 Flow 實驗頁](experiments/06_flow_editing.md)，不因加入本表而改變。

## 未納入數值

小型 targeted pilots、sentinel／positive controls、可與其他表互補反推的小群組、含個例標籤的 tables，以及已知協定失效的歷史比較，未納入公開數值。前者需逐項人工確認再識別風險；後者不能當成有效量化證據。完整實驗脈絡與負結果仍保留於 [experiment archive](experiments/00_research_timeline.md)。
