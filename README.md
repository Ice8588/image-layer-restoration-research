# 非寫實 2D 圖像之前景移除與遮擋區域補全

### Foreground Removal and Amodal Completion for Non-Photorealistic 2D Graphics

移除前景之後，如何補回原本被遮住的**特定後景部件**，並維持身份、外觀、幾何、位置與畫風？本研究以遊戲 UI／人物插圖等非寫實 2D 圖像為對象，建立 baseline、合成 benchmark、方法分支與逐層評估流程，並把研究功能整合到可操作的 Prototype。

本 repository 是研究歷程、實驗資料與精選實作的展示：保留正面、負面、無定論與 diagnostic evidence，不將所有實驗包裝成連續改善。

**Abstract.** This research studies foreground removal and identity-specific amodal completion for non-photorealistic 2D graphics. Controlled synthetic experiments examine conditioning, region preservation, and evaluation. Negative and inconclusive branches remain part of the record. Automatic metrics, human review, and system usability support distinct claims.

![Synthetic baseline and evaluated variant](assets/results/paired/qual_coin_x_chest_cov70.png)

**Baseline → Evaluated Variant**：Qwen Image Edit 2511 Prompt V2 與同提示詞 NoiseMask 3%。這是黑底 RGB synthetic research surrogate，使用 oracle class words／mask；非 RGBA 完整層驗收。圖保留三個樣本，seed 依既有 median-LPIPS 規則選取；不等於人工 pass。[全部配對與 all-seed 圖](docs/qualitative_results.md)

## 研究問題

Amodal completion 補的是原本被遮擋的特定部件，並非任意合理的背景。品質分別看前景是否真正移除、指定後景是否補對、非編輯區域是否維持。長期目標是可獨立使用的 RGBA 部件；歷史實驗的實際 input／output／proxy 在各頁記錄。

## 研究脈絡與 Current Research Understanding

Baseline 分出 BBox、NoiseMask、attention、structure、flow 與 QA 分支。部分 bounded screen 得到負結果，部分只有機制診斷，部分缺正式品質證據；NoiseMask 的較佳 automatic metrics 也不等於真實美術普遍有效。

[研究時間軸與分支圖](docs/experiments/00_research_timeline.md) · [Current Research Pipeline](docs/current_pipeline.md)

## 主要實驗

| Experiment | Execution | Evidence | Conclusion | Adoption |
|---|---|---|---|---|
| [Prompt 與模型 baseline](docs/experiments/01_baselines.md) | Generation Completed | Automatic Metrics; partial Human QA | Inconclusive | Historical |
| [BBox 與區域資訊](docs/experiments/02_region_guidance.md) | Generation Completed | Automatic Metrics | Negative under tested metric conditions | Not Adopted |
| [NoiseMask 與輸入消融](docs/experiments/03_noise_mask.md) | Generation Completed; parent matrix Partially Run | Automatic Metrics; matched Human QA pending | Positive under tested automatic metrics | Current for Qwen class-word V2 contract |
| [Attention 干預與診斷](docs/experiments/04_attention_control.md) | Generation Completed for screens; RQ3 Implemented | Partial Evidence; Automatic Metrics; diagnostic traces | Negative for bounded screens; Diagnostic Only for traces; Inconclusive for RQ3 | Not Adopted / Experimental |
| [Matched structure reference](docs/experiments/05_structure_guidance.md) | Implemented; formal Not Run in audited evidence | CPU geometry viability only | Inconclusive | Experimental |
| [Flow guidance 與 FlowEdit transport](docs/experiments/06_flow_editing.md) | Generation Completed for step-window; RQ1 Implemented | Operator QA for bounded pilot; RQ1 Missing Required Evidence | Negative for tested step-window; Inconclusive for RQ1 | Not Adopted / Experimental |
| [VLM QA、selection 與 retry](docs/experiments/07_vlm_qa.md) | Generation Completed for frozen replay | Operator labels and matched diagnostic comparison | Negative for replacement decision; Diagnostic Only for selector gains | Retain V3; V7 Not Adopted |
| [Benchmark、chained evaluation 與 steps](docs/experiments/08_evaluation.md) | Generation Completed for chained and steps | Automatic Metrics; incomplete stage-level QA | Inconclusive | Current evaluation practice; quality pending |

## Quantitative Evaluation

### Synthetic Benchmark

目前 Synth V2 公開整理包含 30 methods × 27 samples × 5 seeds 的 4,050 筆分數。下表只比較 matched Prompt V2 pair，使用 9-class macro，不能與其他資料／metric scope 直接排名。

| Qwen Image Edit 2511 / oracle inputs | LPIPS ↓ | PSNR ↑ | SSIM ↑ |
|---|---:|---:|---:|
| Class-word Prompt V2 | 0.070 | 25.51 | 0.892 |
| Same prompt + Lab NoiseMask 3% | 0.055 | 26.40 | 0.913 |

這是 automatic evidence；新增 paired QA tuples 仍 pending。[完整分層表](assets/results/paired/table.md) · [逐 seed 分數](assets/results/synthetic_v2/scores.csv) · [評估契約與限制](docs/evaluation.md)

另保存 [Synthetic V3 chained comparison](docs/experiments/08_evaluation.md)，獨立呈現 Stage 1／Stage 2 reveal-region 表，不與 V2 object-centric 指標混排。

### Private Industry Dataset

部分研究使用企業合作資料；本候選不公開任何原圖、個別案例或內部 metadata。整體量化數值仍待公開許可，本版不刊登。

## Legacy Research Prototype

早期 Layer Lab 承載生成／補全／QA／結果檢視，現為 **Legacy / Historical Prototype**，保留作歷史與 rollback 參考。

## Standalone Layer Lab

現行獨立專案為 **Pre-release Integrated Prototype**，有自己的 API、UI、workflow 與相依。生成／補全研究功能與組員自動分層模組、團隊整合形成 end-to-end 系統。產品流程優先採用 pass candidate，必要時保留 fail／uncertain warning 使用 best available；這不等於研究 quality gate passed。

[系統演進與兩種 QA 流程](docs/system_evolution.md)

## Demo

已搜尋錄影；未經完整安全確認的錄影不在此公開，私有 audit 保存版本與待處理項目。本次未重錄或上傳 Demo。

## 個人貢獻

以 Research Design、Implementation、Experiment Execution、Evaluation / Annotation、System Integration 分開整理。原始 QA 分工不等於後續實際貢獻；團隊與第三方工作不列為個人獨作。[貢獻對照與待確認項目](docs/contributions.md)

## Selected Implementation

提供研究使用的 mask dilation、ROI normalization、metrics 與 CPU regression tests。[用途、執行方式與已知限制](docs/selected_implementation.md)

## Limitations / Repository Scope

Synthetic benchmark 只能支持受控比較與校準，不能單獨證明真實美術適用性。Parameter search 不是獨立演算法新意；attention trace 不是因果證明；低 LPIPS 不是 human preference；可用 Prototype 不是 production system。

本候選採全新 Git 歷史；不含完整私有工作區、企業素材、部署設定、模型權重、第三方移植核心或私有 audit。公開範圍與授權仍由研究者最終審閱。[來源與使用範圍](NOTICE.md)

[其他歷史分支與停止矩陣](docs/experiments/09_historical_branches.md) · [Qwen／Live2D 公開來源與研究效度](docs/public_sources.md)
