# Layer Lab 操作展示

從一張插圖與既有遮罩出發，逐層補全被遮擋內容，再檢視與組合圖層。

https://github.com/user-attachments/assets/5b7b9321-4069-4f06-bf7e-644f1d1b779f

約 1 分 28 秒。[下載 MP4](../assets/prototype/Layer_Lab_DEMO.mp4)

## 1. 匯入素材

匯入原圖，在工作區檢視待拆解的插圖。

## 2. 設定遮罩

加入各部件的 masks，指定圖層範圍。勾選遮罩並調整顯示透明度，確認遮罩與原圖的對應位置。

## 3. 逐層生成與補全

選擇品質或快速模式後開始生成，系統依序處理各圖層並補全被遮擋的內容。影片中的生成等待段已加速。

## 4. 檢視與組合圖層

單獨顯示物件或人物，檢查透明背景上的補全結果；切換背景及其他圖層，預覽不同組合的合成效果。

## 5. 回看補全紀錄

開啟各圖層的紀錄，回看生成候選，對照目前顯示的結果。

影片素材與衍生內容的來源見 [Demo artwork](public_sources.md#demo-artwork)。補全品質的實驗比較與失敗案例見 [Qualitative Results](qualitative_results.md)。

## 與完整 Layer Lab 的關係

本 Demo 主要展示 provided-mask 的補全與圖層操作流程。完整 Layer Lab 另整合團隊的自動分層模組，形成從輸入圖像到還原圖層的完整流程。

自動分層由組員主要負責；我的主要工作是生成／補全研究、VLM QA 與生成側整合。團隊整合與個人研究的分工見 [個人貢獻](contributions.md)，方法選擇與待解問題見 [目前研究理解](research_summary.md)。
