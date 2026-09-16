---
name: infinity-labs-inbox
description: Browse INFINITY LABS Unified Inbox threads (inbox_list, conversation_get). Read-only message-center triage — not period corpus search.
---

# Skill: infinity-labs-inbox

**Prerequisite:** `infinity-labs-universal-workflow`. Auth issues → `infinity-labs-session`.

## MCP tools

- `inbox_list` — recent **activity** threads. Params: optional `folder` (`open|pending|done`), `platform`, `q`, `limit` 1–50.
- `conversation_get` — one contact summary + **recent** messages. Required `contact_id`; optional `limit` 1–50 (default 30).

## Use when / Do not use when

| Use when | Do not use when |
|---|---|
| 誰最近找過、收件匣分流 | 情緒占比／期間主題統計 → `infinity-labs-investigate` |
| 打開某一線近期對話 | 把 list 當「全專案歷史普查」 |
| 確認某人目前資料夾／平台 | 無關鍵字的全庫搜訊（我們沒有這種工具） |

## Workflow

1. Triage with `inbox_list` (folder/platform/name as needed).
2. Open a thread with `conversation_get`.
3. For keyword / period evidence across the project, hand off to `infinity-labs-investigate` (`messages_search`).

## Guardrails

- Read-only. Sending → `infinity-labs-messaging` (preview → propose → approve).
- `inbox_list` ≠ message `createdAt` corpus; it is activity-oriented.
