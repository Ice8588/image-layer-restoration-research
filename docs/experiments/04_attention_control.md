# Attention 干預與診斷

| 維度 | 狀態 |
|---|---|
| Execution Status | Generation Completed for screens; RQ3 Implemented |
| Evidence Status | Partial Evidence; Automatic Metrics; diagnostic traces |
| Conclusion | Negative for bounded screens; Diagnostic Only for traces; Inconclusive for RQ3 |
| Adoption Status | Not Adopted / Experimental |

## 問題與 Hypothesis

測試區域 attention 控制是否改善補全；另觀察模型把 source attention 分配到哪裡。 Hypothesis 是研究問題，不是已證明結論。

## 方法與 baseline

Multi-mask、DOE、factorial screens；Attentive Eraser mask ladder；reference-attention comparison；Gaussian visible-target attention RQ3。

## 變因與資料

各 screen 有各自 baseline、gate 與輸入。不可把它們視為同一個 matched experiment。

資料性質：Synthetic Benchmark；部分研究另使用 Private Industry Dataset（僅公開經篩選的 aggregate quantitative results，個例與 metadata 不公開）。

Input／output：Composite RGB、文字；依 arm 加 BBox／oracle mask。輸出為黑底 RGB research surrogate，未因此達成 RGBA layer。

## Evaluation 與 Observation

歷史 screens 停於預定 gate，保留 bounded negative；reference-attention automatic guard 未通過。RQ3 有實作但未找到新的完整 terminal quality evidence。

Automatic metrics、qualitative inspection、human QA、operator QA 分別記錄；[評估契約](../evaluation.md)說明各層級。

## 解釋、採用與限制

Attention trace 只支援機制觀察。Attention mass、邊界集中或熱圖亮度均不能直接證明美術品質或失敗原因。

Verified Cause：本頁未額外提出已驗證機制原因。跨協定結果為 **Not directly comparable**。

## 可閱覽證據

[Synthetic V2 完整數表](../../assets/results/synthetic_v2/summary.json) · [逐 seed 分數](../../assets/results/synthetic_v2/scores.csv) · [圖像索引](../qualitative_results.md)

[返回實驗索引](00_research_timeline.md)
