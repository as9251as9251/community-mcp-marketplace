---
name: real-knowledge
description: Search REAL shop knowledge base FAQ / price / policy via knowledge_search.
---

# Skill: real-knowledge

**Prerequisite:** `real-universal-workflow`.

## MCP tools

- `knowledge_search` — `q` keyword, `limit` 1–10 (default 5). Read-only.

## Workflow

1. Call with the user's question as `q`.
2. Summarize answers in plain language; cite snippets when helpful.
3. If nothing useful returns, say the knowledge base may not cover it — do not invent shop facts.
