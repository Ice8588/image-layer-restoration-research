# Matched structure reference

| 維度 | 狀態 |
|---|---|
| Execution Status | Implemented; formal Not Run in audited evidence |
| Evidence Status | CPU geometry viability only |
| Conclusion | Inconclusive |
| Adoption Status | Experimental |

## 問題與 Hypothesis

測試可見幾何延伸成 guide 後，是否提供比 neutral reference 更多的特定部件結構資訊。 Hypothesis 是研究問題，不是已證明結論。

## 方法與 baseline

RQ2 structure vs matched neutral reference；先進行 frozen geometry applicability。

## 變因與資料

已凍結比較契約；geometry proposal 與生成品質分別驗證。

資料性質：Synthetic Benchmark；部分研究另使用 Private Industry Dataset（僅公開經篩選的 aggregate quantitative results，個例與 metadata 不公開）。

Input／output：輸入 visible geometry 與區域條件；目前驗證輸出為 deterministic guide，未驗證完整補全圖像。

## Evaluation 與 Observation

現有 audit 記錄 guide viability 通過，但 quality_assessed=false；沒有 paired formal pixels 與完整 operator rows。

Automatic metrics、qualitative inspection、human QA、operator QA 分別記錄；[評估契約](../evaluation.md)說明各層級。

## 解釋、採用與限制

能產生 guide 不等於 guide 有效；未執行的品質比較既不是成功，也不是負結果。

Verified Cause：本頁未額外提出已驗證機制原因。跨協定結果為 **Not directly comparable**。

## 可閱覽證據

本頁為經去識別化的研究紀錄摘要；完整原始 audit 留在非公開工作區。缺失證據不以敘事補齊。

[返回實驗索引](00_research_timeline.md)
