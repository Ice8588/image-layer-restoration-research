# 從研究到整合系統

```mermaid
flowchart LR
 R[Research experiments] --> L[Legacy Research Prototype]
 L --> M[Function migration / system evolution]
 M --> S[Standalone Layer Lab]
 S --> T[Team end-to-end integration]
```

## Legacy Research Prototype

早期 Layer Lab 承載生成、補全、QA 與結果檢視；目前只作歷史、rollback 與研究參考，不是現行主要版本。其存在證明功能曾被接入操作流程，不等於研究品質問題已解決。

## Standalone Layer Lab

目前獨立專案具有自己的 API、UI、workflow、dependencies 與測試。現行 README 明確標為 **Pre-release Integrated Prototype**，尚非 production-ready 或 final product。此頁依本機 checkout 的 README、實作、近期變更與 migration 紀錄核對，不代表此次重新驗收了部署。

研究者的生成／補全／研究功能，與組員的自動分層模組、團隊整合，共同形成 end-to-end 系統；不能只用有沒有自動分層來描述兩版差異。

## Product / Layer Lab Workflow

```mermaid
flowchart TD
 I[Source image] --> R[Recognition: object + BBox]
 R --> S[SAM3 segmentation]
 S --> N[Naming]
 N --> G[Qwen repaint candidates]
 G --> Q[Structured Completion QA V3]
 Q --> P{Passing candidate available?}
 P -->|Yes| A[Prefer passing candidate]
 P -->|No| B[Best-evidenced available candidate + fail / uncertain warning]
 A --> O[Adopt artifact / continue]
 B --> O
 O --> H[User review / intervention / regenerate]
 G -->|No usable artifact| X[Blocking stop]
 S -->|Empty or effectively full mask| X
```

產品可繼續使用不等於研究 quality gate passed。Transport／parse failures 和品質 warnings 依實際可用 artifact 分開處理；中斷可從已採用圖層恢復。

## Demo

已搜尋歷史與現行錄影；完整候選清冊和安全審查保存在非公開工作區。未通過圖像及畫面資訊審查的 Demo 不加入本 repository；本次未重錄。

## Legacy UI 靜態畫面

![Legacy edit UI](../assets/prototype/legacy_edit_ui.png)

取自 2026-08-22 歷史錄影的空白編輯介面；沒有企業圖像或真實部署資訊。只展示操作介面，不代表本次完成生成。
