# 多 Agent 平台适配指南（v2.2.0）‌‌‌‌‌‌‌

本技能包为**纯 markdown + 无依赖**结构，`skill/script-studio/` 目录可被任何支持
"自定义技能 / 知识库 / 系统提示词"的 Agent 平台直接加载。以下按平台给出适配方式。

## 适配矩阵

| Agent 平台 | 加载方式 | 触发词示例 |
|---|---|---|
| **Hermes Agent** | 拷入 skills 目录（`scripts/install.sh` / `install.bat`），自动技能路由 | "原创剧本""审核剧本" |
| **Claude Code** | 将 `skill/script-studio/` 拷入项目 `.claude/skills/`；或在 `CLAUDE.md` 中引用 `SKILL.md` 路径 | 同上 |
| **Cursor** | 将 `SKILL.md` 全文放入项目 `.cursor/rules/script-studio.mdc`（或 `.cursorrules`）；references/ 按需 @ 引用 | 同上 |
| **DeepSeek（智能体/ Harness）** | 将 `SKILL.md` 全文粘贴为智能体"人设与回复逻辑"；`references/*.md` 上传为知识库文件 | 同上 |
| **豆包（智能体）** | 创建智能体 → 自定义知识库上传 `skill/script-studio/` 全部 md 文件；`SKILL.md` 作为人设提示词 | 同上 |
| **腾讯元宝（智能体）** | 创建智能体 → 上传知识库文件（`SKILL.md` + `references/*.md`），`SKILL.md` 作为系统指令 | 同上 |
| **WorkBuddy** | 若支持自定义技能目录：整拷 `skill/script-studio/`；若仅支持知识库/提示词：同 DeepSeek 方式 | 同上 |
| **OpenClaw** | 将 `skill/script-studio/` 放入其技能/插件目录（markdown 技能约定）；否则按知识库方式上传 | 同上 |
| **自建 RAG / 其他** | 将 `references/*.md` 切块入向量库，`SKILL.md` 作为 system prompt | 自定义 |

## 通用最小集（任何平台）

最低只需要 2 个文件即可运行核心流程：

1. `skill/script-studio/SKILL.md` — 主流程（S级标准/集前四问/节奏/红线/署名规范）
2. `skill/script-studio/references/01-format-rhythm.md` — 格式基线

增强件（按平台知识库容量取舍）：

| 文件 | 作用 | 建议 |
|---|---|---|
| `references/02-original-writing.md` | 原创写作方法论 | 必带 |
| `references/03~06` | 公式/钩子/闭环/节奏 | 推荐 |
| `references/07-ai-drama-screenwriting-guide` / `08-close-reading-methodology` | 深度方法论（约 250KB） | 容量允许时全带 |

## 加载验证（各平台通用）

加载后向 Agent 提问："写一部短剧第1集，先给出集前四问和场景规划"。
合格回答应包含：**集前四问四题 + 本集唯一情绪 + 5 场景规划 + 前100字钩子设计**，
且成品含"创作工具声明"。缺项说明 references 未完整加载。

## 注意事项

- 各平台对知识库文件大小/数量上限不同：`08-close-reading-methodology.md` 约 207KB，
  若超限可拆分（按章节切成 3~4 段）再传。
- 不同平台渲染 markdown 注释（`<!-- -->`）行为不同，不影响正文使用。
- 技能内的验收清单（SKILL.md 十二章 / Verification）为平台无关文本，可直接抄入各平台规则区。
<!-- © 灵析剧创·智子编辑部 | 版权所有人: 于海峰(hlyhf) | script-studio v2.2.0 | WM-001 -->
