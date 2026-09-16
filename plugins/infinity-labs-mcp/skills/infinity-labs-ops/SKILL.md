---
name: infinity-labs-ops
description: INFINITY LABS project overview via workspace_summary, and router to domain skills for contacts/reservations/dispatch/knowledge/memory.
---

# Skill: infinity-labs-ops

**Prerequisite:** `infinity-labs-universal-workflow`.

## Primary tool

- `workspace_summary` — contacts / reservations / dispatch counts (read-only)

## When to route elsewhere

| Need | Skill |
|---|---|
| 聯絡人 | `infinity-labs-contacts` |
| 收件匣／對話 | `infinity-labs-inbox` |
| 搜訊息 | `infinity-labs-investigate` |
| 發私訊 | `infinity-labs-messaging` |
| 群發 | `infinity-labs-broadcast` |
| 預約 | `infinity-labs-reservations` |
| 派工／轉真人 | `infinity-labs-dispatch` |
| FAQ／價目 | `infinity-labs-knowledge` |
| 內部記憶 | `infinity-labs-memory` |

Cross-cutting write proposals may still be done here **only if** the user already confirmed
and `references/write-lifecycle.md` is followed — otherwise prefer the domain skill.
