---
name: s1mple-ops
description: s1mple project overview via workspace_summary, and router to domain skills for contacts/reservations/dispatch/knowledge/memory.
---

# Skill: s1mple-ops

**Prerequisite:** `s1mple-universal-workflow`.

## Primary tool

- `workspace_summary` — contacts / reservations / dispatch counts (read-only)

## When to route elsewhere

| Need | Skill |
|---|---|
| 聯絡人 | `s1mple-contacts` |
| 收件匣／對話 | `s1mple-inbox` |
| 搜訊息 | `s1mple-investigate` |
| 發私訊 | `s1mple-messaging` |
| 群發 | `s1mple-broadcast` |
| 預約 | `s1mple-reservations` |
| 派工／轉真人 | `s1mple-dispatch` |
| FAQ／價目 | `s1mple-knowledge` |
| 內部記憶 | `s1mple-memory` |

Cross-cutting write proposals may still be done here **only if** the user already confirmed
and `references/write-lifecycle.md` is followed — otherwise prefer the domain skill.
