# Community MCP Marketplace（公開外殼）

給 **Cursor／Claude／Codex／Agents** 用的**公開薄包**：固定 MCP URL、OAuth Authenticate、domain skills／commands／references。

**不含**後台原始碼、資料庫、金鑰、商家資料。真正能力在各站伺服器（REAL／s1mple／INFINITY LABS）。

版本 **1.2.0**。

## 與產品的關係

| 本 repo（可公開） | 產品站（保持私有） |
|---|---|
| `mcp.json` → `…/api/mcp/v1/jsonrpc` | FastAPI、DB、儀表板 |
| Skills／references 教 Agent 怎麼用工具 | OAuth／工具實作 |
| Commands 當快捷驗證／查詢 | 核准佇列、計費、稽核 |

## 本機結構

```text
community-mcp-marketplace/
├── .cursor-plugin/marketplace.json
├── .claude-plugin/marketplace.json
├── plugins/
│   ├── real-mcp/
│   │   ├── skills/       connect · session · policy · contacts ·
│   │   │                 reservations · dispatch · knowledge · memory · ops
│   │   ├── references/   write-lifecycle · brand-isolation ·
│   │   │                 product-terms · error-recovery
│   │   ├── commands/     validate · contacts · summary · reservations ·
│   │   │                 dispatch · knowledge · escalate
│   │   └── host manifests (Cursor / Claude / Codex / Agents)
│   ├── s1mple-mcp/
│   └── infinity-labs-mcp/
├── LICENSE · SECURITY.md · CHANGELOG.md · PUBLISH.md · README.md
└── regen_plugins.py
```

## 使用者流程（安裝 → 授權 → 驗證 → 撤銷）

1. **安裝**對應站 plugin  
2. **Authenticate**（瀏覽器登入 → 選專案 → 允許）  
3. **驗證** `validate-<brand>-setup`  
4. **日常** 聯絡人／預約／派工／知識庫 commands 或口語  
5. **撤銷** 後台 MCP／已授權應用（卸載 plugin ≠ 撤銷 grant）— 見 [SECURITY.md](./SECURITY.md)

## Skills ↔ 真實 MCP 工具

| Skill | Tools |
|---|---|
| session / ops | `workspace_summary` |
| contacts | `contacts_list`, `contact_get` |
| reservations | `reservations_list`, `reservation_*` |
| dispatch | `dispatch_list`, `dispatch_create`, `escalate_to_human` |
| knowledge | `knowledge_search` |
| memory | `memory_list`, `memory_upsert` |

寫入前必須確認意圖（`references/write-lifecycle.md`）。

## 維護

三站外殼同步：`python regen_plugins.py`  
發布步驟：[PUBLISH.md](./PUBLISH.md)
