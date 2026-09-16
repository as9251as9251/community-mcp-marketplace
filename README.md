# Community MCP Marketplace（公開外殼）

給 **Cursor／Claude／Codex／Agents** 用的**公開薄包**：固定 MCP URL、OAuth Authenticate、workflow skills／commands。

**不含**後台原始碼、資料庫、金鑰、商家資料。真正能力在各站伺服器（REAL／s1mple／INFINITY LABS）。

## 與產品的關係

| 本 repo（可公開） | 產品站（保持私有） |
|---|---|
| `mcp.json` → `…/api/mcp/v1/jsonrpc` | FastAPI、DB、儀表板 |
| Skills 教 Agent 何時呼叫哪個工具 | OAuth／工具實作 |
| Commands 當快捷驗證／查詢 | 核准佇列、計費、稽核 |

## 本機結構

```text
community-mcp-marketplace/
├── .cursor-plugin/marketplace.json
├── .claude-plugin/marketplace.json
├── plugins/
│   ├── real-mcp/
│   │   ├── .cursor-plugin/  .claude-plugin/  .codex-plugin/  .agents/
│   │   ├── skills/          (connect · session · policy · contacts · ops)
│   │   ├── commands/        (validate · list-contacts · project-summary)
│   │   ├── mcp.json  .mcp.json  codex.mcp.json
│   │   └── assets/
│   ├── s1mple-mcp/
│   └── infinity-labs-mcp/
├── LICENSE
├── SECURITY.md
├── CHANGELOG.md
├── PUBLISH.md
└── README.md
```

## 使用者流程（安裝 → 授權 → 驗證 → 撤銷）

1. **安裝**對應站的 plugin（Cursor Team Marketplace／Import from Repo，或其他 host 的 plugin 目錄）。
2. **Authenticate**：在 MCP 設定對該 server 按授權；瀏覽器登入該站 → 選專案 → 允許。無需手貼 Token。
3. **驗證**：執行命令 `validate-<brand>-setup`，或請 Agent 使用 `<brand>-session`（會打 `workspace_summary`）。
4. **日常**：`list-contacts`／`project-summary`，或口語「查聯絡人」「專案摘要」。
5. **撤銷**：到該站後台 MCP／已授權應用撤銷 grant（卸載 plugin **不會**自動撤銷伺服器端授權）。詳見 [SECURITY.md](./SECURITY.md)。

## Skills 對應的真實工具

唯讀：`workspace_summary`、`contacts_list`、`contact_get`、`reservations_list`、`dispatch_list`、`knowledge_search`、`memory_list`  
寫入（多為儀表板核准提案）：`memory_upsert`、`contact_add_tag`、`contact_append_note`、`reservation_*`、`dispatch_create`、`escalate_to_human`

寫入前 Agent 必須先確認意圖（見各站 `*-universal-workflow` skill）。

## 下一步

見 [PUBLISH.md](./PUBLISH.md)：建立公開 GitHub repo →（可選）送 Cursor Marketplace 審核。
