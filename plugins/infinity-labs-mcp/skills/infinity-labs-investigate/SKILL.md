---
name: infinity-labs-investigate
description: Search INFINITY LABS inbox message bodies with messages_search (read-only, max 30-day window). Load investigate-playbook for sample/FAQ rules.
---

# Skill: infinity-labs-investigate

**Prerequisite:** `infinity-labs-universal-workflow` + `references/error-recovery.md`.  
**On demand:** `references/investigate-playbook.md`, `references/timezone-policy.md`.

## MCP tools

- `messages_search` — required `q`; optional `contact_id`, `days` (1–30, default 14), `limit` 1–50.

## Use when / Do not use when

| Use when | Do not use when |
|---|---|
| 關鍵字／客訴主題／FAQ 草稿證據 | 「誰找過」→ `infinity-labs-inbox` |
| 明確期間（轉成 `days`≤30） | 把 `conversation_get` 當整月語料 |
| 需可追溯引用的訊息片段 | 無 `q` 的空搜尋（API 必填關鍵字） |

## Workflow

1. Load `references/investigate-playbook.md` for caps and honesty labels.
2. Always pass a real keyword in `q`. Prefer concrete nouns over vague verbs.
3. If the user names a period, set `days` explicitly (cap 30). Report returned `since` / `count`.
4. Cite message ids / contact names from the result; do not invent quotes.
5. After a hit, optional `infinity-labs-inbox` → `conversation_get` for recent context.
6. Reply drafting → `infinity-labs-messaging`. FAQ draft → playbook thin path + optional `knowledge_search`.

## Guardrails

- Read-only. Prefer ≤5 searches per ask before summarizing.
- Hard max **30 days** — split longer asks; label coverage as 樣本／部分 when limited.
