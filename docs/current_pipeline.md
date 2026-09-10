# Current Research Understanding / Current Integrated Pipeline

目前可支持的理解是：輸入身份與區域資訊會影響補全，但更複雜的 guidance 不保證更好；automatic metrics 與逐層可用性必須分開驗證。

Qwen class-word Prompt V2 + Lab NoiseMask 3% 是 synthetic oracle 條件下採用的研究契約；它不能直接取代 standalone 系統的 repaint 契約。Standalone 使用目前的通用移除提示詞與 structured Completion QA V3，產品 workflow 保留 warnings。

Flow step-window 的 bounded negative、attention screens 的 gate failure 與 RQ pilots 的 inconclusive 都保留。新增 trace 是 diagnosis，不是方法有效性證據。Frozen QA 的 selector 改善沒有直接導致替換現行 QA。

長期目標是可獨立使用的 RGBA 完整部件層。Synth V2 等歷史實驗輸出通常為黑底 RGB research surrogate；結構 viability 只輸出 guide，VLM QA 只輸出評估。Standalone 有部件輸出流程，但每層 alpha、identity 與可用性仍須獨立驗證。

[研究與產品流程](system_evolution.md) · [評估契約](evaluation.md)
