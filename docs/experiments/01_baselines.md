# Prompt 與模型 baseline

| 維度 | 狀態 |
|---|---|
| Execution Status | Generation Completed |
| Evidence Status | Automatic Metrics; partial Human QA |
| Conclusion | Inconclusive |
| Adoption Status | Historical |

## 問題與 Hypothesis

建立相同輸入下的移除／補全基準，分開觀察前景殘留與特定後景部件恢復。 Hypothesis 是研究問題，不是已證明結論。

## 方法與 baseline

FLUX.2、Qwen Image Edit 2508／2511 的 prompt-only 與 class-word arms。class words 來自 GT，必須另標 oracle。

## 變因與資料

固定 Synth V2 的 27 張合成圖與 inference seeds 0–4。模型版本改變屬跨模型比較，不是單一機制消融。

資料性質：Synthetic Benchmark。

Input／output：Composite RGB、文字；依 arm 加 BBox／oracle mask。輸出為黑底 RGB research surrogate，未因此達成 RGBA layer。

## Evaluation 與 Observation

已保存 automatic scores。早期 Synth V1 有 method identity／provenance 缺口，僅保留歷史問題，現行數表使用 V2。

Automatic metrics、qualitative inspection、human QA、operator QA 分別記錄；[評估契約](../evaluation.md)說明各層級。

## 解釋、採用與限制

不能把模型替換寫成新演算法，也不能把不同 input privilege 的排名當作公平比較。

Verified Cause：本頁未額外提出已驗證機制原因。跨協定結果為 **Not directly comparable**。

## 可閱覽證據

[Synthetic V2 完整數表](../../assets/results/synthetic_v2/summary.json) · [逐 seed 分數](../../assets/results/synthetic_v2/scores.csv) · [圖像索引](../qualitative_results.md)

[返回實驗索引](00_research_timeline.md)
