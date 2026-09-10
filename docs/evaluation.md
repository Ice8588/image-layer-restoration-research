# 評估方法與 Benchmark 效度

研究目標是恢復特定後景部件的 identity、appearance、geometry、position 與 style consistency；不是任意看似合理的背景。

## 三個獨立品質問題

1. Foreground Removal：指定前景是否移除，有無殘渣或重新生成。
2. Amodal Completion：是否補回指定部件，而非錯誤部件、平坦填色或幻覺。
3. Region Preservation：非編輯區域、幾何與位置是否保持。不能只看被遮擋區。

Synthetic／AI-generated benchmark 可支持 smoke、controlled experiments、mechanism diagnosis、reproducibility、parameter comparison 與 baseline calibration，不能單獨支持對真實非寫實美術普遍有效。

已知合成層的像素可作該合成操作的精確參考，但不是 artist-authored exact GT；model-segmented／inpainted 資料只是 pseudo-label。正式真實美術主張仍需要權利清楚、artist-authored 的 component-level benchmark 與 operator QA。

## Synthetic V2 的量測範圍

固定 9 classes、27 samples、5 inference seeds，30 experimental configurations 的完整逐 seed scores 共 4,050 筆。這 30 個設定包括模型、prompt、mask 與 parameter variants，不是 30 個獨立研究方法。歷史資料中的 `method`／`methods` 欄位保留原 schema，應讀作 configuration identifiers。coverage 與 class 綁定，所以不能作覆蓋率的因果推論。模型／方法／guidance／oracle 分欄保存，跨 input privilege 不做 input-fair 排名。

公開 [protocol.json](../assets/results/synthetic_v2/protocol.json) 記錄 ROI、fallback、metrics、aggregation 與相依版本；[scores.csv](../assets/results/synthetic_v2/scores.csv) 保存逐 sample／seed 分數。[summary.json](../assets/results/synthetic_v2/summary.json) 保存分層與 paired summaries。

Object-centric normalization 可能淡化位置 drift；必須搭配 full-canvas inspection。ROI failure 也須保留，不能只平均成功定位的結果。歷史 exact-mask 與目前 object-centric 分數不直接互比。LPIPS 不是人類偏好，PSNR／SSIM 也不等同美術可用性。

## Research Evaluation Flow

```mermaid
flowchart TD
 C[Candidate + source + target evidence] --> M[Automatic metrics]
 M --> H[Human / operator review]
 H --> P[Pass: within this protocol]
 H --> F[Fail: record failure type]
 H --> U[Uncertain / missing evidence]
 F --> R[Retry if protocol permits]
 F --> S[Stop if predefined gate reached]
 U --> I[Inconclusive / human review]
```

Parameter、prompt、strength、step-window 或 seed search 是校準與消融，不能單獨宣稱 novel algorithmic contribution。新方法須說明改變的計算、適用範圍、baseline 退化邊界與 component ablation。

## Private Industry Dataset

企業合作資料僅納入經篩選的 [aggregate quantitative results](industry_aggregate_results.md)。原圖、result image、mask、crop、個別 case、內部 metadata 與合作企業名稱均不公開。可能由小群組、互補統計或外部資訊反推出個例的數字，不納入公開統計。

<a id="readme-figure-reading-note"></a>

## 質化與量化結果的判讀

Synthetic V2 使用已知類別與遮罩（oracle inputs），輸出為黑底 RGB research surrogate。評估聚焦部件內容與外觀；完整 RGBA 圖層可用性、真實美術泛化與人工品質需另外驗證。[案例分析與完整 all-seed 比較](qualitative_results.md#selected-improvements)同時呈現改善與仍存在的錯誤。

個別案例用來說明錯誤與改善，整體比較採 9-class macro。Object-centric metrics 的 ROI normalization 可能淡化位置 drift，需搭配 full-canvas inspection；其分數與 V3 reveal-region、企業 direct-reveal 指標分開判讀。自動指標、人工評估與實際圖層可用性分別提供不同層級的證據。
