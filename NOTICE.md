# 來源與使用範圍

本 repository 為完整研究工作區的公開展示版本，僅收錄確認可公開的研究內容、合成資料結果與精選實作。Synthetic V1／V2／V3 素材由研究者自行生成，並已確認可公開；通用 mask／evaluation utilities 亦由研究者確認可公開。

合成 GT 是已知來源部件經合成變換後的參考像素，並非 artist-authored ground truth。研究的精選 utilities 與測試保留原有行為，選編時調整套件 import 並修正欠缺證據的因果敘述；這些工具屬於 mask 處理與評估，完整生成系統未在此開源。

## 重用條件

除另有註明之第三方內容外，本 repository 目前未提供統一的開源授權；不應推定所有內容均可依 MIT／Apache-2.0 等條款重用。

NumPy、Pillow、scikit-image、PyTorch、LPIPS 為外部相依，依各自授權使用；本 repository 不封裝其程式或模型權重。Attentive Eraser、KV-Edit、ConceptAttention、ComfyUI 與模型內部移植程式均未收錄；其名稱用於識別既有方法與實驗，不列為研究者原創。

## 圖像、影片與企業合作資料

Synthetic 圖像使用自行生成素材。既有 standalone UI 圖使用簡單漸層測試素材，呈現介面而非模型生成成果。

Layer Lab Demo 使用 Qwen-Image-Layered 官方公開示例及研究衍生結果。原始插圖作者身分不在此推定，也不將原圖列為個人原創；來源、衍生內容說明與上游授權副本見 [Demo artwork](docs/public_sources.md#demo-artwork)。影片展示圖層操作，正式補全品質另由研究評估說明。

企業合作資料 / Private Industry Dataset 僅刊登整體量化結果，不含原圖、生成圖、mask、crop、個別案例、內部 metadata 或企業真名。完整原始來源對照保留於非公開工作區。
