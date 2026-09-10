# Public-source datasets：來源與公開性評估

評估日期：2026-09-10。公開下載來源與企業合作資料分開分類；可下載不等於任意再散布，標註來源也不會自動取得額外權利。

## Qwen-Image-Layered

來源：[官方 repository](https://github.com/QwenLM/Qwen-Image-Layered)。使用的 input snapshot 為 `54c4fe47e76d745775e03fc66ee38457280ed9ea`，下載入口為 [官方 test_images](https://github.com/QwenLM/Qwen-Image-Layered/tree/54c4fe47e76d745775e03fc66ee38457280ed9ea/assets/test_images)。

官方 README 與 [LICENSE](https://github.com/QwenLM/Qwen-Image-Layered/blob/54c4fe47e76d745775e03fc66ee38457280ed9ea/LICENSE) 標示 Apache-2.0。本作品集保留來源與授權文字，展示下述 Demo；沒有另外打包原始 input PNG、衍生 mask dataset 或模型權重。公開來源素材不分類為企業機密。

本機研究使用 13 張官方 input PNG，其中 12 張進入 mask-authoring，形成 64 個 semantic removal units 與 76 張 visible ownership masks。這些是公開輸入的研究衍生標註，並非官方 training corpus、PSD 或 hidden-region exact GT。正式 layer GT 與 completion target 均為 0，operator decisions 仍 pending。Predicted amodal masks 不能當成 artist-authored GT。

## Demo Artwork

[Layer Lab Demo](../assets/prototype/Layer_Lab_DEMO.mp4)中的紅色城市、人物、資料夾、相機與白鴿圖像，下載來源為 QwenLM 的 [Qwen-Image-Layered 官方 test_images/1.png](https://github.com/QwenLM/Qwen-Image-Layered/blob/54c4fe47e76d745775e03fc66ee38457280ed9ea/assets/test_images/1.png)，使用上列固定 snapshot；底層 illustration 不宣稱為本研究者原創。

影片展示研究衍生的 masks、移除／補全結果、圖層合成與 UI 操作；這些衍生內容不是官方提供的 artist-authored layer GT。影片另有剪輯、字幕與生成段加速。附 [上游 Apache-2.0 授權文字](../assets/prototype/QWEN_SOURCE_LICENSE.txt)，此來源授權不表示整個研究 repository 或所有媒體均採同一授權。

## Live2D sample models

來源：[Live2D 官方 sample download](https://www.live2d.com/en/learn/sample/)。適用 [Free Material License Agreement](https://www.live2d.com/eula/live2d-free-material-license-agreement_en.html) 與 [各角色使用條款](https://www.live2d.com/en/learn/sample/model-terms/)。

條款依使用者類別、角色與呈現形式區分；原始 archives／models／textures 的再散布和 renderer 衍生展示不能混為一談。Miara 與 Hiyori Momose 另限制角色設計變更。個人／學生展示可能有可用範圍，但仍需確認申請人身分、指定 copyright notice 與輸出是否符合個別條款。本候選保留來源和研究說明，暫不打包原始資料或衍生 GT。

研究已建立 renderer／ownership／direct-reveal 診斷：Drawable 聯集不必然是美術上獨立部件，renderer correctness 不等於 component benchmark admission。Fixed-pose census 和 predicted semantic groups 仍須 operator QA；不是經驗證的 amodal-completion 效能 benchmark。

## 本版選擇

Synthetic 圖像使用研究者已確認權利的自行生成素材；Qwen 公開示例透過上述 Demo 展示並標註來源，Live2D 媒體仍未選編。保留兩者的研究歷程與效度限制，不把公開來源素材誤標為企業私有資料。
