# Attention Control：生成干預與機制觀察

## 研究動機

區域控制除了指定哪裡可改，也可以嘗試調整模型如何使用來源資訊。本分支探討兩個問題：干預 attention 是否能改善補全，以及 attention trace 是否能幫助描述模型關注的位置。

## 實驗設計

研究包含多個分支，各自使用對應 baseline、輸入與停止條件：

| 分支 | 比較內容 |
|---|---|
| Multi-mask、DOE 與 factorial screens | 不同區域 attention 控制組合 |
| Attentive Eraser | visible-mask expansion ladder |
| Reference attention | 對照來源 attention 的設定 |
| RQ3 | Gaussian visible-target attention |
| Attention trace | 觀察 source attention 的空間分布 |

部分研究使用 Synthetic Benchmark，部分使用企業合作資料；後者僅公開核准的整體量化結果。生成比較輸入 composite RGB、文字與各設定的區域條件，涉及已知遮罩時屬於 oracle input；輸出仍以 RGB surrogate 評估。各分支不是同一個配對實驗，不能合併排名。

## 結果

歷史 screens 已完成各自測試，並在預定停止條件下結束，保留限定測試範圍的負結果。Reference-attention 未通過自動指標檢查；RQ3 已實作，但尚缺完整配對生成與品質評估，因此沒有足以形成正式品質結論的結果。

![Attentive Eraser：硬幣移除後寶箱中央仍缺失，保留所有 seeds](../../assets/results/all_seeds/attentive_eraser_visible_mask_0pct_coin_x_chest_cov70.png)

這個 visible-mask 0% 的公開例子中，硬幣所在區域大多成為黑色缺口，寶箱中央沒有補回。它呈現的是補全不完整；單靠這張圖還無法確定造成缺口的機制。

## 判讀

三類證據分開保留：

- **Negative**：已測試 screens 的限定範圍結果，未支持納入主要流程。
- **Diagnostic Only**：attention trace 的機制觀察。Attention mass、邊界集中或熱圖亮度只能描述注意力分布，無法直接判定美術品質或證明失敗原因。
- **Inconclusive**：RQ3 缺完整品質比較；reference-attention 雖未通過自動檢查，仍缺人工判讀，品質結論保留未定論。

不同 screen 的輸入、指標與停止條件不同，不能以某個分支的結果替其他分支下結論。

## 對後續研究的影響

已停止的控制設定未採用（**Not Adopted**）；RQ3 與診斷工具維持探索性研究（**Experimental**）。後續要分別驗證「模型關注了哪裡」與「干預是否改善指定部件」，不能把熱圖變化當成品質增益。

## 詳細證據

[Attentive Eraser 等 Synthetic V2 完整 summary](../../assets/results/synthetic_v2/summary.json) · [逐 seed 分數](../../assets/results/synthetic_v2/scores.csv) · [protocol](../../assets/results/synthetic_v2/protocol.json) · [歷史分支](09_historical_branches.md) · [評估方法](../evaluation.md)

上述公開數據涵蓋其中的合成資料設定。

[返回研究時間軸](00_research_timeline.md)
