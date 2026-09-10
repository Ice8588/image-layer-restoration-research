# Structure Guidance：可見幾何能否引導遮擋補全？

## 研究動機

僅靠文字可能生成「合理但不是原本那個」部件。RQ2 嘗試從仍可見的幾何延伸出結構 guide，希望為被遮擋部位提供更具體的形狀資訊。

## 實驗設計

比較 structure reference 與 matched neutral reference，先固定比較方式，再檢查可見幾何能否穩定轉成 guide。將兩個問題分開處理：

1. **幾何可行性**：輸入 visible geometry 與區域條件，產生 deterministic guide。
2. **補全品質**：同條件下比較 structure 與 neutral reference 的實際生成圖像，再由人工判讀。

研究資料範圍涵蓋合成資料與企業合作資料；企業個例及中間產物不公開。幾何測試的輸出是 guide，尚不是補全圖像或 RGBA 圖層。

## 結果

Guide 建構已完成實作，CPU geometry viability 檢查通過。正式配對品質實驗尚未執行，現有紀錄為 `quality_assessed=false`，沒有配對的正式生成圖像與完整人工評估紀錄。

目前完成幾何可行性驗證，**補全品質仍待正式配對實驗評估**。

## 判讀

結論維持 **Inconclusive**，方法維持 **Experimental**。目前能說明的是幾何 guide 可以建構；是否比 neutral reference 更有助於恢復特定部件，仍需品質實驗回答。未執行的比較也不能列成負結果。

## 對後續研究的影響

保留 matched neutral reference 作為後續對照，先完成配對生成與人工判讀，再考慮是否納入主要流程。這個分支使研究更明確地區分「產生了結構資訊」與「結構資訊對補全有用」。

## 詳細證據

本頁整理研究設計與既有幾何驗證結果。

[評估方法與效度](../evaluation.md) · [目前研究理解](../research_summary.md) · [返回研究時間軸](00_research_timeline.md)
