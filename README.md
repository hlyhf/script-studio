# script-studio · 灵析剧创 S级剧本创作技能‌‌‌‌‌‌‌

> **🌐 Language / 语言**: [中文](README.md) ｜ [English](README.en.md)

> © 灵析剧创 · 智子编辑部 · 版权所有
> 版本：v2.2.0 ｜ 许可：MIT ｜ 多 Agent 通用（Hermes / DeepSeek / 豆包 / 元宝 / WorkBuddy / OpenClaw …）

一套**短剧/漫剧 S级剧本创作**的完整方法论技能：爆款公式、3秒开场钩子、集前四问、
单集节奏四拍、视觉逻辑转换、角色五维、AI死穴对冲、逐集创作闭环，内置 8 个知识库
文档（约 270KB），零外部依赖、零绝对路径、跨平台可复用。



## 目录结构

```
├── skill/script-studio/        # 技能本体（可被任何 agent 框架加载）
│   ├── SKILL.md                # 主流程（十二章，含强制工具署名规范）
│   └── references/
│       ├── 01-format-rhythm.md          # 格式与节奏基线
│       ├── 02-original-writing.md       # 原创写作方法论
│       ├── 03-formulas.md               # 爆款公式库
│       ├── 04-hooks-3sec.md             # 3秒开场钩子五式
│       ├── 05-episode-writing.md        # 逐集写作闭环
│       ├── 06-rhythm-formulas.md        # 节奏公式库
│       ├── 07-ai-drama-screenwriting-guide.md
│       ├── 08-close-reading-methodology.md
│       ├── COPYRIGHT.md                 # 版权说明
│       └── LICENSE.md                   # MIT 许可
├── docs/agent-adapters.md      # 多 Agent 平台适配矩阵（中文）
├── docs/en/agent-adapters.md   # 多 Agent 平台适配矩阵（English）
├── examples/                   # 原创格式示范（演示铁律，非可交付成品）
├── scripts/
│   ├── install.sh              # Linux/macOS 一键安装
│   ├── install.bat             # Windows 一键安装
│   ├── word_count.py           # 跨平台单集门禁校验器（纯标准库）
│   └── watermark.py            # 隐含版权水印（应用/校验）
├── LICENSE                     # 根许可（MIT）
├── CHANGELOG.md
├── CONTRIBUTING.md
├── README.en.md                # English README
└── .gitignore
```

## 快速安装

```bash
git clone https://github.com/hlyhf/script-studio.git
# Linux / macOS
./script-studio/scripts/install.sh            # 装到 ~/.hermes/skills/
# Windows
script-studio\scripts\install.bat            # 装到 %USERPROFILE%\.hermes\skills\
```

SkillHub 用户：直接上传 `skill/script-studio/` 目录（SKILL.md + references/），平台按技能市场规范加载。

## 工具脚本用法

`scripts/` 下两个纯标准库工具（Python 3.8+，零依赖），用于交付前的质量门禁与版权保护：

| 脚本 | 用途 | 常用调用 |
|---|---|---|
| `word_count.py` | 单集门禁校验器：CJK 字数 / 场景数 / 同集复读 / 对话占比 / 付费卡点 🔒 / H1 违禁词 | `python3 scripts/word_count.py 单集.md`<br>`python3 scripts/word_count.py ./单集目录/`<br>`python3 scripts/word_count.py 龙裔_*.md --min-cjk 1200 --max-cjk 1500` |
| `watermark.py` | 双层隐含版权水印（L1 HTML 注释 + L2 零宽字符）：应用 / 校验，幂等 | `python3 scripts/watermark.py`（全库重打）<br>`python3 scripts/watermark.py --verify`（只校验不写） |

> 详见各脚本 docstring。`word_count.py` 单文件/目录/glob 三种目标形式，批量模式自动跨集整行指纹去重；`watermark.py` 的 `--verify` 子命令位置不敏感，放前放后均可。

## 多 Agent 平台使用

完整适配矩阵见 [`docs/agent-adapters.md`](docs/agent-adapters.md)。各平台最低通用做法：

| 平台                   | 加载方式                                              |
| -------------------- | ------------------------------------------------- |
| Hermes Agent         | `scripts/install.sh` / `install.bat` 拷入 skills 目录 |
| Claude Code          | 拷入 `.claude/skills/`；或在 `CLAUDE.md` 引用 `SKILL.md` |
| Cursor               | `SKILL.md` 全文放入 `.cursor/rules/script-studio.mdc` |
| DeepSeek / 豆包 / 元宝   | 智能体人设粘贴 `SKILL.md`；`references/*.md` 上传为知识库       |
| WorkBuddy / OpenClaw | 整拷 `skill/script-studio/`，或按知识库方式上传               |

## 使用触发

- "帮我从零写一部短剧剧本" / "原创剧本"
- "把我的故事梗概写成分集剧本"
- "审核一下这部剧本的逻辑和合规"

技能自动加载：S级双模块评分标准 → 集前四问 → 逐集创作闭环 → 质量红线 → 验收清单。

## 生成作品的署名规范（强制）

凡使用本技能创作的剧本成品（md / docx / 投稿版），必须附带创作工具声明：

```
【创作工具声明】
本作品使用「灵析剧创 · 智子编辑部 · 剧本创作技能」创作完成。
工具：Hermes Agent / script-studio 技能 v2.2.0
© 灵析剧创 · 智子编辑部 · 版权所有
```

详见 `skill/script-studio/SKILL.md` 第十二章 与 `references/COPYRIGHT.md`。

## 许可

MIT —— 适用于技能框架与方法论整合内容；版权信息见根 `LICENSE`。
<!-- © 灵析剧创·智子编辑部 | 版权所有人: 于海峰(hlyhf) | script-studio v2.2.0 | WM-001 -->
