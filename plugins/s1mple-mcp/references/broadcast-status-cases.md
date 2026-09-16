# Broadcast status cases (s1mple)

Fields from `broadcast_list`: `status`, `target_count`, `sent_count`, `failed_count`, `scheduled_at`, `sent_at`.

**Audience size:** trust `broadcast_audience_preview.eligible_count` only.  
`tags_list` counts ≠ deliverable audience.

## Golden cases

| Observation | What you may say | Must not |
|---|---|---|
| `status=draft` (typical after MCP `broadcast_create` approve) | 草稿已建立；須到群發頁按發送 | 宣稱客人已收到 |
| `status` shows scheduled + future `scheduled_at` | 已排程至該時間（若後台支援） | 改排程／取消（無對應 MCP） |
| `scheduled_at` in the past but still not sent | 排程時間已過、目前狀態仍為… | 自動再 `broadcast_create` 當重送 |
| `sent` / completed + `failed_count=0` | 已送出；成功數用 `sent_count` | 發明開啟率／點擊率 |
| `failed_count>0` | 成功 `sent_count`、失敗 `failed_count`；根因不明就說不明 | 自動重送失敗名單 |
| User wants retry after failure | 重新 `broadcast_audience_preview` + 確認 + 新草稿提案 | 靜默重複同一提案 |

## After create

Approval of `broadcast_create` creates a **draft** only. Sending remains a dashboard action.
