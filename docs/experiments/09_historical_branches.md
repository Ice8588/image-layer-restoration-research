# 其他歷史分支與未完成工作

這些分支保留研究問題與終止／缺證原因；不併入 30-method Synthetic V2 表作直接排名。下列紀錄截至各原始研究報告，再由本次本機核對補充；缺少新的 terminal artifact 不推定有新結果。

| 分支 | Execution Status | Evidence Status | Conclusion | Adoption Status |
|---|---|---|---|---|
| ConceptAttention localization | Partially Run | Partial Evidence；舊參數結論失效 | Inconclusive | Not Adopted |
| Synthetic V1 FLUX／Qwen | Partially Run | Logs／eval；method identity 與 provenance 缺口 | Not Comparable | Replaced by V2 |
| KV-Edit benchmark／recipe／crop | Partially Run | 部分 artifacts；單樣本 diagnostic | Inconclusive / Diagnostic Only | Historical |
| Visible-target native-inpaint | Partially Run | Aggregate eval 存在但 raw predictions 缺失 | Inconclusive | Not Adopted |
| Local Klein design | Designed | Missing Required Evidence | Inconclusive | Not Adopted |
| NoiseMask follow-up parent | Partially Run | Partial／skipped／stopped | Inconclusive | Not Adopted as full matrix |
| VLM capability evaluation | Generation Completed | Bounded capability evidence | Diagnostic Only | Historical |
| VLM closed-loop matrix | Generation Completed | Human QA missing | Inconclusive | Pending Decision |
| Mask-grounded API-first | Generation Completed | Human fields pending；raw lineage 後來取代 | Inconclusive | Replaced |
| Attentive Eraser reference attention | Generation Completed | Automatic guard failed；judgments blank | Inconclusive for quality | Not Adopted |
| Qwen public-input multilayer masks | Implemented | Predicted masks；operator pending | Diagnostic Only | Experimental |
| Live2D renderer／semantic census | Implemented | Renderer／ownership evidence；operator pending | Diagnostic Only | Experimental |

## KV-Edit 的重要邊界

官方 FLUX.1 執行核心與 FLUX.2 experimental port 是不同 substrate。不同 inversion／denoising steps、guidance 和移除 prompt 不能寫成 equal-setting comparison。早期 smoke 曾出現區域內彩色碎點，屬 Observation；不能只憑該現象宣稱是 prompt 或 attention 的已驗證失敗原因。第三方核心沒有搬入精選實作。

## 停止的矩陣

早期 NoiseMask／prompt parent 規劃 12 arms × 135，實際 terminal predictions 為 1407/1620；其中 generic 10% 為 57/135，generic 20% 為 0 且跳過。單一 class-word NoiseMask 3% arm 的 operator QA 為 112/135 pass、23/135 fail，僅支持這個歷史 arm；它不同於後來 Prompt V2 matched pair，不能混用分母或抹去 parent incomplete。

## 資料型態與 input／output

早期 synthetic completion arms 以 composite／broken-layer RGB 搭配文字或 oracle guidance，輸出 RGB research surrogate。VLM capability 的輸出是判斷；Live2D 的輸出是 renderer states／semantic masks；Qwen public-input 的輸出是 predicted masks。這些都不能一律稱為 RGBA 完整層成果。

[公開資料來源評估](../public_sources.md) · [返回時間軸](00_research_timeline.md)
