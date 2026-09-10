# BBox 與區域資訊

| 維度 | 狀態 |
|---|---|
| Execution Status | Generation Completed |
| Evidence Status | Automatic Metrics |
| Conclusion | Negative under tested metric conditions |
| Adoption Status | Not Adopted |

## 問題與 Hypothesis

文字可能無法精確指定要移除的物件；測試視覺 BBox 能否提供位置線索。 Hypothesis 是研究問題，不是已證明結論。

## 方法與 baseline

綠框 overlay 與線寬 3 px／1%／2% 比較；另有 GT visible-mask guidance，兩者不是同一種輸入。

## 變因與資料

同模型、同合成樣本、同 seed；線寬比較使用對應 class-word prompt arms。

資料性質：Synthetic Benchmark。

Input／output：Composite RGB、文字；依 arm 加 BBox／oracle mask。輸出為黑底 RGB research surrogate，未因此達成 RGBA layer。

## Evaluation 與 Observation

canonical report 中較粗 BBox 的 macro 指標較弱；FLUX.2 BBox arms 也弱於 class-word prompt。此為本次設定下的負結果。

Automatic metrics、qualitative inspection、human QA、operator QA 分別記錄；[評估契約](../evaluation.md)說明各層級。

## 解釋、採用與限制

綠框可能被當成圖像內容是可能解釋，尚非已驗證原因；保留負例供區域指示設計參考。

Verified Cause：本頁未額外提出已驗證機制原因。跨協定結果為 **Not directly comparable**。

## 可閱覽證據

[Synthetic V2 完整數表](../../assets/results/synthetic_v2/summary.json) · [逐 seed 分數](../../assets/results/synthetic_v2/scores.csv) · [圖像索引](../qualitative_results.md)

[返回實驗索引](00_research_timeline.md)
