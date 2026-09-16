# 如何公開到 GitHub／Cursor Marketplace

本目錄已是可獨立推上 GitHub 的內容。**不要**把 `REAL/`、`s1mple/`、`INFINITY-LABS/` 整包推進這個公開 repo。

## A. 建立公開 GitHub repo（必做）

1. 在 GitHub 新建**空的 public** repo，例如 `community-mcp-marketplace`  
2. 只推送**本資料夾**根目錄內容：

```bash
cd community-mcp-marketplace
git init
git add .
git commit -m "Initial public MCP marketplace shell (URLs + skills only)"
git branch -M main
git remote add origin https://github.com/YOUR_ORG/community-mcp-marketplace.git
git push -u origin main
```

3. 確認 repo 裡**沒有** `.env`、後端 `src/`、資料庫、金鑰。

## B. 團隊內先用（不必送官方市集）

Cursor → **Dashboard → Plugins → Import from Repo** → 貼上公開（或團隊可讀）repo URL。  
適合先給自己人測 Authenticate。

## C. 送 Cursor 官方 Marketplace（選做）

1. 對照 [Plugins reference](https://cursor.com/docs/reference/plugins) 檢查清單  
2. 到 [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish) 提交 repo  
3. 等人工審核（可能要改 `author.email`、logo、說明文案）

送審前請改：

- `.cursor-plugin/marketplace.json` 的 `owner`
- 各 `plugins/*/.cursor-plugin/plugin.json` 的 `author`
- （建議）換上正式 logo SVG

## D. 多 host 清單

各 `plugins/*` 已含 `.cursor-plugin`、`.claude-plugin`、`.codex-plugin`、`.agents`。  
根目錄另有 `.claude-plugin/marketplace.json`（三站並列）。送審時以目標 host 文件為準；Cursor 仍以根目錄 `.cursor-plugin/marketplace.json` 為主。

維護三站 skills／commands 時可跑 `python regen_plugins.py`（會覆寫各 plugin 外殼；勿把產品後端拷進來）。

## E. 本包開了什麼、沒開什麼

| 開源（MIT） | 不開源 |
|---|---|
| MCP URL、Skill 文案、plugin 清單 | 自動脆／三站後端與前端產品碼 |
| 「怎麼連線」 | 「怎麼實作工具與計費」 |

使用者授權後，資料仍只打到你們自己的網域；公開 repo 無法取代登入與權限。
