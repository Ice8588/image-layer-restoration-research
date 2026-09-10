# Flow guidance 與 FlowEdit transport

| 維度 | 狀態 |
|---|---|
| Execution Status | Generation Completed for step-window; RQ1 Implemented |
| Evidence Status | Operator QA for bounded pilot; RQ1 Missing Required Evidence |
| Conclusion | Negative for tested step-window; Inconclusive for RQ1 |
| Adoption Status | Not Adopted / Experimental |

## 問題與 Hypothesis

測試推論過程的方向組合與時間窗；另以 FlowEdit transport 作獨立機制候選。 Hypothesis 是研究問題，不是已證明結論。

## 方法與 baseline

Step-window pilot、signed/extreme sweep、RQ1 transport 是不同分支，不混稱為同一個方法。

## 變因與資料

Step-window 使用 fresh baseline 與 matched pass/fail；RQ1 需要自己的 mechanical gate、paired pixels 與 operator review。

資料性質：Synthetic Benchmark；部分研究另使用 Private Industry Dataset（本候選不公開其量化數值與個例）。

Input／output：Composite RGB、文字；依 arm 加 BBox／oracle mask。輸出為黑底 RGB research surrogate，未因此達成 RGBA layer。

## Evaluation 與 Observation

歷史 step-window pilot 未支持替換 baseline；signed/extreme 只有 automatic evidence。RQ1 formal terminal evidence 尚缺。企業資料的數值與個例不在此公開。

Automatic metrics、qualitative inspection、human QA、operator QA 分別記錄；[評估契約](../evaluation.md)說明各層級。

## 解釋、採用與限制

不能外推成所有 flow 方法無效。時間窗搜尋本身是校準；公式、退化邊界與 component ablation 才能支撐方法主張。

Verified Cause：本頁未額外提出已驗證機制原因。跨協定結果為 **Not directly comparable**。

## 可閱覽證據

本頁為經去識別化的研究紀錄摘要；完整原始 audit 留在非公開工作區。缺失證據不以敘事補齊。

[返回實驗索引](00_research_timeline.md)
