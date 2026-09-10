# VLM QA：辨識錯誤、挑選候選與重試

## 研究動機

圖像指標可能漏掉前景殘留、錯誤補全或部件破壞。這項研究評估 VLM 是否能提供候選品質判斷與風險提示，並進一步區分：**辨識單張結果是否可用**，以及**從多張結果中挑出較好的候選**。

## 實驗設計

比較 Completion QA V3–V7，固定同一批已生成像素進行 frozen candidate replay。Naming 與 removal 評估分開，避免把命名判斷變化混入補全品質比較；關鍵負例（sentinel rejects）另用於檢查錯誤接受風險。

輸入為 source、candidate 與區域提示，輸出 structured QA／selection。QA 本身不生成圖像或 RGBA 圖層。研究涵蓋合成資料與企業合作資料，後者只公開整體數字：

- Candidate-level detection：與人工標註比較單張候選的判斷。
- Stage-level selection：以所有 stage 為分母，檢查選出的候選是否通過；abstain 不算 pass。

## 結果

企業合作資料的 frozen replay 包含 342 個人工標註候選、114 個 stage。完整 V3–V7 比較見 [整體量化結果](../industry_aggregate_results.md)；其中 V3 與 V7 摘要如下：

| 指標 | V3 | V7 |
|---|---:|---:|
| Accuracy | 81.3% | 77.4% |
| Balanced accuracy | 63.4% | 75.1% |
| Pass recall | 92.0% | 78.8% |
| Reject detection | 34.9% | 71.4% |
| Strict stage pass | 79.8% | 86.8% |

V7 的 strict stage pass 相對 V3 增加 7.0 percentage points，原報告近似 95% CI 為 +2.3 至 +11.7。但關鍵負例檢查仍未通過，未滿足預先設定的替換條件。比較固定相同生成候選，以隔離 QA 版本差異。

## 判讀

**替換決策維持 Negative，選圖收益維持 Diagnostic Only。** V7 部分指標較好，但仍未解決關鍵誤判，不能僅憑選圖收益推論 QA 已可靠。

Binary classification 排除 human-uncertain；VLM unavailable 另計，不能直接當成人工 fail。Classification accuracy 也不是生成可用率。V6 的 selector 數字來自 lowest-index automatic-pass simulation，與實際新一輪生成或重試效果不同；V4 遇同分可 abstain，且沒有預先設定的替換標準。

## 對後續研究的影響

整合流程**保留 V3；V7 未採用**。後續 QA 需同時考慮錯誤辨識與候選挑選，而重試策略需要另驗證是否真的改善結果。

產品操作允許使用者檢視帶有風險提示的候選；研究的人工品質判定仍獨立保留。早期 closed-loop 與 retry 矩陣中的人工評估缺口，見 [歷史分支](09_historical_branches.md)。

## 詳細證據

[完整 V3–V7 數表、分母與 CI](../industry_aggregate_results.md) · [評估方法](../evaluation.md)

基於合作資料保密限制，本頁僅公開 aggregate results。

[返回研究時間軸](00_research_timeline.md)
