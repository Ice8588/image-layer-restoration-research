# NoiseMask：限制修改範圍的配對實驗

## 研究動機

Prompt-based editing 能執行物件移除，但非編輯區域可能跟著改變。這項實驗保留非編輯區域的 latent，測試是否能降低無關變動，同時補回被遮擋的部件。

## 實驗設計

以 Qwen Image Edit 2511 的 class-word Prompt V2 為 baseline，與**相同提示詞 + Lab NoiseMask 3%**配對比較。Synthetic V2 每個設定固定 27 samples × 5 seeds；已知 class words 與 mask 都是 oracle input。

輸入為 composite RGB、文字與指定區域，輸出為黑底 RGB surrogate。另一分支保留 FLUX.2 mask expansion ladder；不同 backbone 的 mask 處理方式不預設等價，也不把早期 prompt 的結果混入這組 Prompt V2 比較。

## 結果

| 設定 | LPIPS ↓ | PSNR ↑ | SSIM ↑ |
|---|---:|---:|---:|
| Prompt V2 | 0.070 | 25.51 | 0.892 |
| Prompt V2 + NoiseMask 3% | 0.055 | 26.40 | 0.913 |

以上為 9-class macro。先在每個 sample 內聚合 seeds 後，NoiseMask 的 LPIPS 在 20/27 個 sample 較低，baseline 在 7/27 個 sample 較低。原分析的配對 LPIPS 差值（baseline − NoiseMask）為 +0.015，95% CI 為 [+0.005, +0.026]。

![寶箱高遮擋案例：輸入、目標與兩個設定](../../assets/results/paired/qual_coin_x_chest_cov70.png)

圖中兩種設定都能移除硬幣，但鎖扣形狀與細節仍偏離目標。每列沿用原分析的 median-LPIPS seed 選取規則；這張圖展示差異，完整變化見 [所有 seed 與失敗案例](../qualitative_results.md)。

## 判讀

結論維持 **Positive under tested automatic metrics**。這支持在目前合成資料與已知輸入條件下保留 NoiseMask，但配對比較的 270 個新增 QA tuples 尚待人工判讀，不能將指標收益換算為人工通過率。

合成 GT 來自自行生成素材，尚不足以推論真實美術的普遍效果。Object-centric ROI normalization 可能淡化位置偏移，需搭配 full-canvas 檢視；RGB surrogate 也仍需另外驗證 RGBA 圖層可用性。細節見 [評估方法與圖像限制](../evaluation.md)。

## 對後續研究的影響

Qwen class-word Prompt V2 + Lab NoiseMask 3% 保留為目前合成資料研究採用設定（**Current**）。Layer Lab 使用的通用移除提示詞另有操作需求，不能直接以這個 oracle 實驗取代系統設定。

早期 NoiseMask follow-up parent matrix 僅部分執行，完整矩陣仍為未定論；單一設定的完成不補足其他停止或跳過的項目。[歷史分支](09_historical_branches.md)保留執行量、早期人工結果與其不同分母。

## 詳細證據

[配對完整表與 CI](../../assets/results/paired/table.md) · [summary](../../assets/results/synthetic_v2/summary.json) · [逐 seed 分數](../../assets/results/synthetic_v2/scores.csv) · [protocol](../../assets/results/synthetic_v2/protocol.json)

[返回研究時間軸](00_research_timeline.md)
