# BBox Guidance：位置資訊是否有助於補全？

## 研究動機

文字指令可能不足以精確指定要移除的物件。這項實驗在輸入圖上加入綠色 BBox，希望以位置線索減少模型找錯物件的情形，並檢查線寬是否影響生成。

## 實驗設計

在 Synthetic V2 中固定同模型、合成樣本與 seeds 0–4，比較對應的 class-word prompt 與綠框設定，線寬包括 3 px、1% 與 2%。類別文字取自已知標註，屬於 oracle input。

BBox 是畫在 composite RGB 上的視覺標記；另一組 GT visible-mask guidance 則提供已知遮罩。兩者帶入模型的資訊形式不同，分開分析。生成輸出仍為黑底 RGB surrogate。

## 結果

既有 9-class macro 顯示，FLUX.2 綠框設定弱於對應的 class-word baseline；Qwen 的較粗線寬也沒有帶來預期改善：

| 模型與設定 | LPIPS ↓ | PSNR ↑ | SSIM ↑ |
|---|---:|---:|---:|
| FLUX.2 class-word baseline | 0.085 | 23.88 | 0.888 |
| FLUX.2 + 綠框 3 px | 0.459 | 11.45 | 0.541 |
| FLUX.2 + 綠框 1% | 0.460 | 11.36 | 0.540 |
| FLUX.2 + 綠框 2% | 0.468 | 11.18 | 0.534 |
| Qwen 2511 class-word baseline | 0.068 | 26.02 | 0.898 |
| Qwen 2511 + 綠框 3 px | 0.075 | 26.24 | 0.890 |
| Qwen 2511 + 綠框 1% | 0.080 | 26.01 | 0.885 |
| Qwen 2511 + 綠框 2% | 0.098 | 25.53 | 0.867 |

這裡的 Qwen baseline 是早期 class-word prompt，與後來的 Prompt V2 分開比較。

## 判讀

結論保留為 **Negative under tested metric conditions**：本設定下未觀察到整體改善。Qwen 3 px 的 PSNR 略高，但 LPIPS 與 SSIM 未改善，因此整體未呈現一致收益。

一個可能解釋是綠框被模型當成要生成或保留的圖像內容；現有結果尚未驗證這個原因。這項負結果針對測試過的視覺框形式與輸入條件，不外推至所有區域引導。自動指標與人工美術品質仍需分開判讀。

## 對後續研究的影響

BBox 沒有納入主要流程（**Not Adopted**）。研究保留此負結果，並把「提供位置資訊」與「實際限制修改範圍」分開考慮，進一步比較 [NoiseMask](03_noise_mask.md)。已知遮罩帶來額外輸入資訊，因此不能與純文字或綠框設定直接作輸入公平的排名。

## 詳細證據

[完整 summary 與配對比較](../../assets/results/synthetic_v2/summary.json) · [逐 seed 分數](../../assets/results/synthetic_v2/scores.csv) · [protocol](../../assets/results/synthetic_v2/protocol.json) · [評估方法](../evaluation.md)

[返回研究時間軸](00_research_timeline.md)
