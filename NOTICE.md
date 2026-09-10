# 來源與使用範圍

本 repository 公開研究敘事、實驗結果，以及通用 mask／evaluation utilities 與測試。

Synthetic V1／V2／V3 素材由研究者自行生成。合成 GT 是已知來源部件經合成變換後的參考像素，並非 artist-authored ground truth。

## 重用條件

除另有註明之第三方內容外，本 repository 目前未提供統一的開源授權；不應推定所有內容均可依 MIT／Apache-2.0 等條款重用。

NumPy、Pillow、scikit-image、PyTorch、LPIPS 為外部相依，依各自授權使用。第三方模型與方法依原始來源引用，相關實作與授權由各來源說明。

## 圖像、影片與企業合作資料

Layer Lab Demo 使用 Qwen-Image-Layered 官方公開示例及研究衍生結果，原始插圖依上游來源標註。素材來源、衍生內容與授權副本見 [Demo artwork](docs/public_sources.md#demo-artwork)。

Standalone UI 圖使用簡單漸層測試素材。

企業合作資料 / Private Industry Dataset 基於保密限制，僅公開整體量化結果，個例與可識別資訊不公開。
