# 非寫實 2D 圖像之前景移除與遮擋區域補全

Foreground Removal and Amodal Completion for Non-Photorealistic 2D Graphics

本研究探討如何移除遊戲 UI／插圖中的前景，補回被遮擋的特定部件，同時維持外觀、形狀與畫風，減少美術拆圖與修補工作。

以 Qwen Image Edit 為基礎，比較提示詞與區域引導設定，並以合成資料、逐層評估及失敗案例檢查補全效果。

<img src="assets/results/paired/qual_coin_x_chest_cov70.png" alt="寶箱補全：Prompt V2 與同提示詞加入 NoiseMask 3% 的比較" width="640">

*同一提示詞加入 NoiseMask 前後的補全比較。[圖像選取與評估限制](docs/evaluation.md#readme-figure-reading-note) · [更多結果與失敗案例](docs/qualitative_results.md)*

## 採用方法與主要結果

- **補全設定**：合成資料實驗採用 Qwen Image Edit 2511、class-word Prompt V2 與 Lab NoiseMask 3%，保留非編輯區域的 latent，降低無關區域變動。
- **評估方式**：分別檢查前景殘留、指定部件補全與非編輯區域保持；結合 LPIPS／PSNR／SSIM、逐 seed 比較與人工判讀。
- **候選品質檢查**：整合流程保留 Completion QA V3；後續 QA 版本的比較尚未支持替換。

Synthetic V2 包含 **30 experimental configurations × 27 samples × 5 seeds**，共 4,050 筆分數。以下為相同 Prompt V2 的配對比較（9-class macro）：

| 設定 | LPIPS ↓ | PSNR ↑ | SSIM ↑ |
|---|---:|---:|---:|
| Prompt V2 | 0.070 | 25.51 | 0.892 |
| Prompt V2 + NoiseMask 3% | 0.055 | 26.40 | 0.913 |

此結果限於使用已知類別與遮罩的合成資料條件；自動指標改善不等同人工品質通過。[NoiseMask 實驗](docs/experiments/03_noise_mask.md) · [完整數表](assets/results/paired/table.md) · [評估設定與限制](docs/evaluation.md)

其他研究涵蓋 BBox、attention、structure reference、FlowEdit、VLM QA 與多階段補全。完整實驗、負結果與未定論項目見 [實驗索引](docs/experiments/00_research_timeline.md)；企業合作資料的整體數據見 [Private Industry Dataset](docs/industry_aggregate_results.md)。

## Layer Lab Demo

[觀看 Demo（MP4，約 1 分 28 秒）](assets/prototype/Layer_Lab_DEMO.mp4)

影片示範從一張插圖建立獨立圖層的操作：

1. 匯入原圖，加入各部件的遮罩並預覽範圍。
2. 選擇生成模式，逐層補全被遮擋的內容。
3. 切換物件、人物與背景圖層，檢視補全結果並預覽組合效果。
4. 開啟各圖層的補全紀錄，回看生成候選。

生成等待段已加速。[操作說明](docs/system_evolution.md) · [影片素材來源](docs/public_sources.md#demo-artwork)

## 專案與實作

本研究專案由我獨立開發，涵蓋研究設計、程式實作、實驗執行與評估分析；與其他模組合併的系統成果位於 **Layer Lab** 專案。

[研究貢獻](docs/contributions.md) · [精選 mask／evaluation utilities 與執行方式](docs/selected_implementation.md) · [資料來源與授權](NOTICE.md)
