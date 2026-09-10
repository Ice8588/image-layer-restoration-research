# 其他歷史分支與未完成工作

這些分支保留曾經提出的研究問題、停止原因與尚未完成的驗證。它們各自使用不同協定，不併入 Synthetic V2 的 30 experimental configurations 作直接排名；以下狀態依既有研究紀錄整理。

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

官方 FLUX.1 執行核心與 FLUX.2 experimental port 使用不同模型基礎與執行核心。不同 inversion／denoising steps、guidance 和移除 prompt 不能寫成 equal-setting comparison。早期 smoke 曾出現區域內彩色碎點，屬於已觀察現象；不能只憑該現象宣稱是 prompt 或 attention 的已驗證失敗原因。

## 停止的矩陣

早期 NoiseMask／prompt parent 規劃 12 arms × 135，已完成的 predictions 為 1407/1620；其中 generic 10% 為 57/135，generic 20% 為 0 且跳過。單一 class-word NoiseMask 3% arm 的 operator QA 為 112/135 pass、23/135 fail，僅支持這個歷史 arm；它不同於後來 Prompt V2 matched pair，不能混用分母或抹去 parent incomplete。

## 資料型態與 input／output

早期 synthetic completion arms 以 composite／broken-layer RGB 搭配文字或 oracle guidance，輸出 RGB research surrogate。VLM capability 的輸出是判斷；Live2D 的輸出是 renderer states／semantic masks；Qwen public-input 的輸出是 predicted masks。這些都不能一律稱為 RGBA 完整層成果。

[公開資料來源評估](../public_sources.md) · [返回時間軸](00_research_timeline.md)

## 公開素材的 Benchmark 探索

Qwen-Image-Layered 探索使用 13 張官方 input PNG，其中 12 張進入 mask-authoring，形成 64 個 semantic removal units 與 76 張 visible ownership masks。這些研究衍生標註屬於 predicted masks；正式 layer GT 與 completion target 均為 0，人工判讀尚未完成。它們不是官方 training corpus、PSD 或 artist-authored hidden-region GT，研究狀態維持 Diagnostic Only／Experimental。[素材來源](../public_sources.md#qwen-image-layered)

Live2D 分支曾探索以 renderer、ownership 與 direct-reveal 建立部件級 benchmark；fixed-pose 與 semantic groups 仍待人工評估，尚未納入目前補全品質評估，保留為 Diagnostic Only／Experimental。

## 主要實驗的詳細狀態

<details>
<summary>展開 01–08 的執行、證據與採用紀錄</summary>

下表保留各狀態的區別；研究敘事與後續決策見各實驗頁。

| Experiment | Execution | Evidence | Conclusion | Adoption |
|---|---|---|---|---|
| [Prompt 與模型 baseline](01_baselines.md) | Generation Completed | Automatic Metrics; partial Human QA | Inconclusive | Historical |
| [BBox 與區域資訊](02_region_guidance.md) | Generation Completed | Automatic Metrics | Negative under tested metric conditions | Not Adopted |
| [NoiseMask 與輸入消融](03_noise_mask.md) | Generation Completed; parent matrix Partially Run | Automatic Metrics; matched Human QA pending | Positive under tested automatic metrics | Current for Qwen class-word V2 contract |
| [Attention 干預與診斷](04_attention_control.md) | Generation Completed for screens; RQ3 Implemented | Partial Evidence; Automatic Metrics; diagnostic traces | Negative for bounded screens; Diagnostic Only for traces; Inconclusive for RQ3 | Not Adopted / Experimental |
| [Matched structure reference](05_structure_guidance.md) | Implemented; formal Not Run | CPU geometry viability only | Inconclusive | Experimental |
| [Flow guidance 與 FlowEdit transport](06_flow_editing.md) | Generation Completed for step-window; RQ1 Implemented | Operator QA for bounded pilot; RQ1 Missing Required Evidence | Negative for tested step-window; Inconclusive for RQ1 | Not Adopted / Experimental |
| [VLM QA、selection 與 retry](07_vlm_qa.md) | Generation Completed for frozen replay | Operator labels and matched diagnostic comparison | Negative for replacement decision; Diagnostic Only for selector gains | Retain V3; V7 Not Adopted |
| [Benchmark、chained evaluation 與 steps](08_evaluation.md) | Generation Completed for chained and steps | Automatic Metrics; incomplete stage-level QA | Inconclusive | Current evaluation practice; quality pending |

</details>
