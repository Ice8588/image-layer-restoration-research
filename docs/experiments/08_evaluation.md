# Benchmark、chained evaluation 與 steps

| 維度 | 狀態 |
|---|---|
| Execution Status | Generation Completed for chained and steps |
| Evidence Status | Automatic Metrics; incomplete stage-level QA |
| Conclusion | Inconclusive |
| Adoption Status | Current evaluation practice; quality pending |

## 問題與 Hypothesis

建立可重現評分，同時避免合成圖與重建結果掩蓋單層失敗。 Hypothesis 是研究問題，不是已證明結論。

## 方法與 baseline

Synth V2 object-centric analysis、Synth V3 two-stage chained comparison、independent steps sweep。

## 變因與資料

區分 exact-mask、object-centric 與 chained scope；各自保留資料、seed、prompt、mask 和模型契約。

資料性質：Synthetic Benchmark；部分研究另使用 Private Industry Dataset（僅公開經篩選的 aggregate quantitative results，個例與 metadata 不公開）。

Input／output：Composite RGB、文字；依 arm 加 BBox／oracle mask。輸出為黑底 RGB research surrogate，未因此達成 RGBA layer。

## Evaluation 與 Observation

V3 已有兩模型 chained predictions，但歷史 Stage 2 QA 缺口仍在；steps 有自動指標與速度紀錄但缺人工判讀。

Automatic metrics、qualitative inspection、human QA、operator QA 分別記錄；[評估契約](../evaluation.md)說明各層級。

## 解釋、採用與限制

上層可能遮住下層缺陷，完整重建不能取代獨立部件可用性。速度也須分清 inference time 與端到端 latency。

Verified Cause：本頁未額外提出已驗證機制原因。跨協定結果為 **Not directly comparable**。

## 可閱覽證據

[Synthetic V2 完整數表](../../assets/results/synthetic_v2/summary.json) · [逐 seed 分數](../../assets/results/synthetic_v2/scores.csv) · [圖像索引](../qualitative_results.md)

[返回實驗索引](00_research_timeline.md)

## Chained Synthetic V3 證據

50 samples × 5 seeds × 2 stages，每模型 500 predictions。Stage 1 移除 F、目標 M+B；Stage 2 使用實際 Stage 1 prediction 再移除 M、目標 B。兩模型設定不同：FLUX.2-dev 30 steps、Qwen Image Edit 2511 40 steps，皆 guidance 4.0，非 equal-step comparison。

[獨立 V3 比較表](../../assets/results/synthetic_v3/table.md) · [FLUX summary](../../assets/results/synthetic_v3/flux2_summary.json) · [Qwen summary](../../assets/results/synthetic_v3/qwen2511_summary.json)

![Stage 1](../../assets/results/synthetic_v3/qual_key_x_padlock_x_chest_stage1.png)

![Stage 2 chained](../../assets/results/synthetic_v3/qual_key_x_padlock_x_chest_stage2_chained.png)

此表評估 reveal region，與 V2 object-centric 不直接比較。Lineage verified 是分析紀錄，不等於 operator pass；輸出仍是 RGB surrogate。圖保留原分析的種子選擇，並非品質改善證明。
