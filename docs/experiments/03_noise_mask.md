# NoiseMask 與輸入消融

| 維度 | 狀態 |
|---|---|
| Execution Status | Generation Completed; parent matrix Partially Run |
| Evidence Status | Automatic Metrics; matched Human QA pending |
| Conclusion | Positive under tested automatic metrics |
| Adoption Status | Current for Qwen class-word V2 contract |

## 問題與 Hypothesis

保留非編輯區域的 latent，測試能否降低無關 drift，同時補回遮擋部件。 Hypothesis 是研究問題，不是已證明結論。

## 方法與 baseline

Prompt V2 baseline 與同提示詞 Lab NoiseMask 3% matched comparison；另保留 FLUX.2 expansion ladder。

## 變因與資料

V2：27 samples × 5 seeds／arm。class-word 與 mask 都是 oracle。不同 backbone 的 mask semantics 不預設等價。

資料性質：Synthetic Benchmark。

Input／output：Composite RGB、文字；依 arm 加 BBox／oracle mask。輸出為黑底 RGB research surrogate，未因此達成 RGBA layer。

## Evaluation 與 Observation

9-class macro LPIPS 由 0.070 至 0.055；20/27 sample aggregates 較低。這是 automatic evidence，270 個新增 QA tuples 仍待判。

Automatic metrics、qualitative inspection、human QA、operator QA 分別記錄；[評估契約](../evaluation.md)說明各層級。

## 解釋、採用與限制

Qwen V2 contract 已被採用不等於每張圖品質通過。早期 parent matrix 部分停止；不得以完成的單一 arm 補稱整個 parent 完成。

Verified Cause：本頁未額外提出已驗證機制原因。跨協定結果為 **Not directly comparable**。

## 可閱覽證據

[Synthetic V2 完整數表](../../assets/results/synthetic_v2/summary.json) · [逐 seed 分數](../../assets/results/synthetic_v2/scores.csv) · [圖像索引](../qualitative_results.md)

[返回實驗索引](00_research_timeline.md)
