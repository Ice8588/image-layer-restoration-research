# Flow Guidance 與 FlowEdit：三個不同層次的比較

## 研究動機

除了提示詞與空間區域，生成過程的方向組合及作用時間也可能影響移除與補全。本研究先比較 step-window 與 scale，再將 FlowEdit transport 作為獨立的機制分支，避免把參數搜尋與方法驗證混為一談。

## 實驗設計

| 分支 | 設計 | 評估方式 |
|---|---|---|
| Step-window pilot | fresh baseline 與不同作用時間窗 | 配對生成結果與人工 pass／fail |
| Signed / extreme scale | 正負與極端 scale，相對 scale 0 | pseudo-GT 自動指標校準 |
| RQ1 FlowEdit transport | 獨立 transport 實作 | 需要基本行為檢查、配對生成與人工判讀 |

研究涵蓋 Synthetic Benchmark 與企業合作資料。生成設定使用 composite RGB、文字及各分支的區域條件；已知遮罩屬於 oracle input，輸出以 RGB surrogate 評估。這三個分支各有 baseline 與協定，不能串成同一組消融或共用結論。

## 結果

Step-window pilot 已完成生成與人工評估，在目前限定設定下未支持替換 baseline，保留 **Negative**。

Signed / extreme scale 保留 912 筆 metric rows 的整體比較。Scale +8 的 LPIPS 差值 CI 跨過 0；+32、−2、−4 等設定的指標呈現退化。完整七組 scale、CI 與聚合方式見 [企業合作資料結果](../industry_aggregate_results.md)。這部分仍缺人工評估，屬於 **Diagnostic Only**。

RQ1 FlowEdit transport 已完成實作，但缺完整配對生成與品質評估，目前沒有足以判斷補全收益的正式結果，維持 **Inconclusive**。

## 判讀

Step-window 的負結果只適用於已測條件，不能外推成所有 Flow 方法無效。Signed scale 是探索性校準：pseudo-GT 指標反映局部代理目標，尚不能判定特定後景部件是否真正還原。

時間窗與 scale 搜尋可用於校準，但方法主張還需要清楚的公式、退化回 baseline 的邊界，以及 component ablation。RQ1 必須用自己的實驗回答有效性，不能沿用其他 Flow 分支的數字。

## 對後續研究的影響

目前 step-window 設定未採用（**Not Adopted**）；RQ1 保持 **Experimental**，待配對品質驗證。這些結果讓後續比較優先回到明確 baseline 與部件品質，而非持續增加控制參數。

## 詳細證據

[Signed / extreme scale 完整 aggregate table](../industry_aggregate_results.md) · [評估方法](../evaluation.md) · [其他歷史分支](09_historical_branches.md)

[返回研究時間軸](00_research_timeline.md)
