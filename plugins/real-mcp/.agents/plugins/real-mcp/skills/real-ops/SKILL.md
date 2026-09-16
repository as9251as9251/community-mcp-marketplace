---
name: real-ops
description: REAL project overview via workspace_summary, and router to domain skills for contacts/reservations/dispatch/knowledge/memory.
---

# Skill: real-ops

**Prerequisite:** `real-universal-workflow`.

## Primary tool

- `workspace_summary` — contacts / reservations / dispatch counts (read-only)

## When to route elsewhere

| Need | Skill |
|---|---|
| 聯絡人 | `real-contacts` |
| 收件匣／對話 | `real-inbox` |
| 搜訊息 | `real-investigate` |
| 預約 | `real-reservations` |
| 派工／轉真人 | `real-dispatch` |
| FAQ／價目 | `real-knowledge` |
| 內部記憶 | `real-memory` |

Cross-cutting write proposals may still be done here **only if** the user already confirmed
and `references/write-lifecycle.md` is followed — otherwise prefer the domain skill.
