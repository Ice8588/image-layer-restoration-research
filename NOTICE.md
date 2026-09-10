# 來源與使用範圍

本候選內容由研究工作區選編；研究者已確認 Synthetic V1／V2／V3 為自行生成且無版權疑慮，並允許公開通用 mask／evaluation utilities。圖像不是 artist-authored ground truth；合成 GT 是已知來源部件經合成變換後的參考像素。

精選 utilities 與測試來自本研究程式；只調整套件 import 與移除無充分證據的因果敘述。這些工具不是新的生成演算法，也不代表整個研究系統開源。未授予整個 repository 統一的開源授權；重用條款仍待研究者決定，不能推定為 MIT。

NumPy、Pillow、scikit-image、PyTorch、LPIPS 為外部相依，依各自授權使用；本 repository 不封裝其程式或模型權重。Attentive Eraser、KV-Edit、ConceptAttention、ComfyUI 與模型內部移植程式均未搬入。其研究名稱只用於實驗識別，不表示本研究者原創。

完整原始來源對照與權利審核留在非公開工作區；本頁不含內部路徑與個別企業案例。

企業合作資料 / Private Industry Dataset 只刊登經篩選的 aggregate quantitative results，不含原圖、result image、mask、crop、個別 case、內部 metadata 或企業真名。Standalone UI 圖取自既有介面測試，使用簡單漸層 fixture，不是企業素材或模型生成成果。

Layer Lab Demo 使用 Qwen-Image-Layered 官方公開示例及研究衍生結果，來源、修改說明與上游授權副本見 [Demo artwork](docs/public_sources.md#demo-artwork)。底層 illustration 不列為個人原創；影片也不構成 artist-authored GT 或正式 operator QA 通過的證據。
