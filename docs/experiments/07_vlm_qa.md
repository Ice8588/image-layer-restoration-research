# VLM QA、selection 與 retry

| 維度 | 狀態 |
|---|---|
| Execution Status | Generation Completed for frozen replay |
| Evidence Status | Operator labels and matched diagnostic comparison |
| Conclusion | Negative for replacement decision; Diagnostic Only for selector gains |
| Adoption Status | Retain V3; V7 Not Adopted |

## 問題與 Hypothesis

高自動分數可能漏掉殘留或破壞；評估 QA 是否能支援候選挑選與風險提示。 Hypothesis 是研究問題，不是已證明結論。

## 方法與 baseline

歷史 V3–V7、frozen candidate replay、sentinel rejects，以及 naming／removal 分離。

## 變因與資料

固定同一批候選像素再比較 QA，區分 candidate-level detection 與 stage-level selection。

資料性質：Synthetic Benchmark；部分研究另使用 Private Industry Dataset（僅公開經篩選的 aggregate quantitative results，個例與 metadata 不公開）。

Input／output：輸入 source／candidate 與區域提示；輸出 structured QA／selection，不直接產生 RGBA layer。

## Evaluation 與 Observation

後續 matched diagnostic 有 selector 收益，但沒有消除 sentinel failure；目前保留 V3。企業資料原圖與逐筆標籤不公開；經篩選的整體分母與量化比較見 [企業 aggregate](../industry_aggregate_results.md)。

Automatic metrics、qualitative inspection、human QA、operator QA 分別記錄；[評估契約](../evaluation.md)說明各層級。

## 解釋、採用與限制

Selector 選到較好候選不代表可靠判定 pass；研究 gate 與產品 best-available 行為必須分開。

Verified Cause：本頁未額外提出已驗證機制原因。跨協定結果為 **Not directly comparable**。

## 可閱覽證據

本頁為經去識別化的研究紀錄摘要；完整原始 audit 留在非公開工作區。缺失證據不以敘事補齊。

[返回實驗索引](00_research_timeline.md)
