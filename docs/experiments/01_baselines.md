# Prompt 與模型 baseline

## 研究動機

前景移除與部件還原是兩個不同要求：模型可能消除遮擋物，卻改寫後景的形狀或細節。研究起點是建立相同輸入下的基準，分開觀察前景殘留、指定部件補全與非編輯區域變動，再決定需要哪一類控制。

## 實驗設計

比較 FLUX.2、Qwen Image Edit 2508／2511 的 prompt-only 與 class-word 設定。Synthetic V2 固定 27 張合成圖、9 個類別與 inference seeds 0–4；class-word 設定使用已知目標類別文字，因此屬於 oracle input。

輸入為 composite RGB 與文字，部分比較另加入 BBox 或已知遮罩。輸出以黑底 RGB 表示部件，作為補全研究的替代表示（RGB surrogate），尚需另外驗證 RGBA 完整圖層的可用性。模型版本與輸入資訊量分開記錄，跨模型比較不當成單一機制消融。

## 結果

V2 已完成生成並保存逐 seed 自動分數。以下為其中不含 class words 的 prompt-only 基準，直接摘自既有 9-class macro，供閱讀各模型起點：

| 設定 | LPIPS ↓ | PSNR ↑ | SSIM ↑ |
|---|---:|---:|---:|
| FLUX.2 prompt-only | 0.306 | 16.47 | 0.681 |
| Qwen Image Edit 2508 prompt-only | 0.373 | 14.10 | 0.553 |
| Qwen Image Edit 2511 prompt-only | 0.224 | 20.04 | 0.752 |

[戒指案例的完整 seed 圖](../qualitative_results.md#foreground-residue)呈現 prompt-only 可能保留前景的問題。早期 Synthetic V1 的設定身分與來源紀錄不完整，留作歷史研究紀錄；現行量化入口使用 V2。

## 判讀

自動指標提供模型與提示詞的比較起點，人工評估僅完成部分，因此整體品質結論維持 **Inconclusive**。加入已知類別或遮罩會改變輸入資訊量，不能把跨輸入條件的排名解讀為公平的方法優劣；不同協定也不能直接比較。

模型替換本身不是新演算法。圖像檢視、指標與人工判讀各自回答不同問題，詳見 [評估方法](../evaluation.md)。

## 對後續研究的影響

這批 baseline 保留為歷史基準，讓後續能問更具體的問題：[BBox 是否能提供位置線索](02_region_guidance.md)、[NoiseMask 是否能限制無關變動](03_noise_mask.md)，以及複雜控制是否值得加入。後續比較固定對應 baseline、樣本與 seed，避免把多個變因的差異歸因於單一控制。

## 詳細證據

[完整 summary](../../assets/results/synthetic_v2/summary.json) · [逐 seed 分數](../../assets/results/synthetic_v2/scores.csv) · [protocol](../../assets/results/synthetic_v2/protocol.json) · [質化結果](../qualitative_results.md) · [V1 與其他歷史工作](09_historical_branches.md)

[返回研究時間軸](00_research_timeline.md)
