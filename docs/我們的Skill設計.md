# 我們自己的 Skill 設計

> 這份文件是 **Community MCP** 的產品憲章，不是跟誰對齊的抄本。  
> 公開 repo 只放「怎麼連、怎麼問、怎麼提議」；「怎麼實作、怎麼計費、客人資料」永遠留在各站私有後端。

## 1. 該不該向外界學習？

**該學的是機制，不該學的是別人的業務目錄。**

| 值得學 | 不該照抄 |
|---|---|
| 薄外殼：市集只放 MCP URL＋Skill＋Command | 對方的群發／旅程／對話調查 skill 名稱與流程 |
| 先驗證 session，再做業務 | 把沒有實作的工具寫進 Skill，讓 Agent 瞎猜 |
| 政策 skill／references 分離 | 單一品牌假設（我們天生是多站） |
| 寫入前要使用者確認 | 暗示「一呼叫就已生效」 |

我們的產品真相是：

1. **多品牌**：REAL／s1mple／INFINITY LABS 資料與授權不得混用  
2. **OAuth 綁專案**：Agent 能動的範圍＝使用者同意當下選的專案  
3. **提案式寫入**：多數寫入工具是「提議」，後台核准後才生效  
4. **Allowlist**：專案可關掉工具；Skill 不可發明工具名  

所以 Skill 包的目標不是「功能看起來比較多」，而是 **Agent 在對的邊界內做對的事**。

## 2. 設計原則（憲章）

### P0 — 安全與邊界

1. **一 plugin＝一品牌＝一網域＝一 MCP server id**  
2. **不向使用者索取 Token／密碼／OTP**；只引導 Authenticate／重新授權  
3. **卸載 plugin ≠ 撤銷伺服器授權**；撤銷必須走後台  
4. **工具不在 `tools/list`＝此專案停用**；說明即可，禁止替代瞎喊  

### P1 — 對使用者說話的方式

1. 先講 **聯絡人／預約／派工／知識庫／記憶／轉真人**，再視需要補 ID  
2. 中文商家語境優先；使用者改講技術詞時再跟  
3. 失敗時給可執行下一步（重新 Authenticate／稍後再試／去後台開工具），不丟堆疊給客人  

### P2 — 讀寫不對稱

1. **預設先讀**：摘要、列表、搜尋  
2. **任何寫入／提議**：先一句話重述意圖 → 等人說可以 → 再呼叫工具  
3. **呼叫成功 ≠ 已上線**：必須說「可能還要後台核准」，除非結果明確寫已生效  

### P3 — 只描述真實能力

Skill／Command 只能對應後端 **已上線** 的 MCP 工具。  
後端沒有的能力（例如完整行銷自動化），**不要**先寫 Skill 佔位——那是在教 Agent 說謊。

## 3. Skill 分層（我們的形狀）

```text
連接層     *-mcp-connect     安裝／Authenticate 說明
驗證層     *-session         workspace_summary＋錯誤復原
憲章層     *-universal-workflow + references/*
路由層     *-ops             專案總覽，並指到領域 skill
領域層     contacts / reservations / dispatch / knowledge / memory
```

| 層 | 職責 | 不負責 |
|---|---|---|
| 連接 | 告訴人怎麼授權 | 查資料 |
| 驗證 | 證明連線可用 | 改資料 |
| 憲章 | 用語、寫入、隔離、錯誤 | 直接打業務工具 |
| 路由 | 摘要＋分流 | 取代領域 skill |
| 領域 | 單一主題的讀／提議 | 跨品牌、發明 API |

### References（憲章附件）

| 檔案 | 用途 |
|---|---|
| `product-terms.md` | 對商家怎麼講 |
| `write-lifecycle.md` | 確認 → 提議 → 核准 |
| `brand-isolation.md` | 網域／server 硬邊界 |
| `error-recovery.md` | 401／429／缺工具／5xx |

## 4. Command 怎麼設計

Command 是 **一句話快捷鍵**，不是第二套業務系統。

原則：

- 一個 command 只做一件事  
- 文案直接點名要用哪個 skill  
- 會寫入的 command（例如轉真人）必須內建「先確認」  

目前一組：

`validate-*-setup` · `list-contacts` · `project-summary` · `list-reservations` · `list-dispatch` · `search-knowledge` · `escalate-human`

## 5. 與後端的契約

公開包承諾：

- MCP URL 形狀：`https://{domain}/api/mcp/v1/jsonrpc`  
- OAuth Authenticate（使用者無需手貼長效金鑰）  
- 工具名與參數以各站 `tools/list` 為準  

公開包 **不** 承諾：

- 工具永遠全開（allowlist 可變）  
- 提議寫入立即生效  
- 跨專案／跨品牌查詢  

後端若新增工具：先上線 → 再改 `regen_plugins.py` 長出 skill／command → 發版。順序不可反。

## 6. 多 Host

同一套 skills／commands，分別掛：

- Cursor（`.cursor-plugin`）  
- Claude（`.claude-plugin`）  
- Codex（`.codex-plugin`）  
- Agents（`.agents/plugins`）  

Host 差異只在「怎麼點 Authenticate」；業務憲章相同。見各站 `references/error-recovery.md`。

## 7. 明確不做

- 不在公開 repo 放後端、DB schema、金鑰、商家資料  
- 不為了「看起來齊全」預寫沒有工具的 skill  
- 不把三站外殼合併成單一 MCP（會破壞隔離）  
- 不以競品功能清單當 roadmap；以商家實際 MCP 工具為 roadmap  

## 8. 演進規則

1. 改工具 → 先後端，再 `python regen_plugins.py`，再 bump `CHANGELOG`  
2. 改憲章 → 先改本文件與 `references/`，再讓領域 skill 引用  
3. 發版 → 只推 `community-mcp-marketplace/` 獨立倉庫，永不夾帶 `REAL/`／`s1mple/`／`INFINITY-LABS/`  

---

**一句話：**  
別人示範了「市集薄包怎麼賣連線」；我們自己要賣的是「多品牌商家、授權綁專案、先讀後提議、核准才生效」的 Agent 行為。
