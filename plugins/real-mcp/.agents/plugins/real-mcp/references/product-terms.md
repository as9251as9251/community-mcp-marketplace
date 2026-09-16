# Product terms (zh-TW) — REAL

Prefer these customer-facing words:

| Prefer | Avoid leading with |
|---|---|
| 專案 | workspace_id（除非使用者要 ID） |
| 聯絡人／客人 | contact row / schema |
| 收件匣／訊息中心 | inbox activity list as “全庫普查” |
| 待核准提案 | “已送出給客人” without approval |
| 群發草稿 | “已群發完成” when status is draft |
| 旅程／自動化 | inventing create/start MCP tools |
| 預約 | reservation entity |
| 派工／派工單 | dispatch job payload |
| 知識庫／FAQ／價目／店規 | knowledge_search raw hits only |
| 記憶（內部） | memory_upsert internals |
| 轉真人 | escalate payload |
| 需後台核准 | “已寫入完成” without evidence |
| MCP 呼叫次數 | credits／錢包／扣款 |

## Dashboard label ↔ MCP tools

| 後台說法 | MCP |
|---|---|
| 訊息中心／收件匣 | `inbox_list`, `conversation_get` |
| 搜訊息／查關鍵字 | `messages_search` |
| 私訊客人 | `message_preview` → `message_send` |
| 群發 | `broadcast_list`, `broadcast_audience_preview`, `broadcast_create` |
| 標籤 | `tags_list`, `contact_add_tag` |
| 旅程 | `flows_list`, `flow_get`, `flow_sessions_list`（唯讀） |
| 待核准 | `proposals_list` |
| 連線／用量 | `mcp_whoami`, `mcp_usage_summary` |

If the user asks for IDs or API fields, you may disclose non-sensitive mappings.
