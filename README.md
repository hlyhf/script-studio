# script-studio · 灵析剧创 S级剧本创作技能

> © 灵析剧创 · 智子编辑部 · 版权所有
> 版本：v2.1.0 ｜ 许可：MIT ｜ Hermes Agent 技能（skill）

一套**短剧/漫剧 S级剧本创作**的完整方法论技能：爆款公式、3秒开场钩子、集前四问、
单集节奏四拍、视觉逻辑转换、角色五维、AI死穴对冲、逐集创作闭环，内置 8 个知识库
文档（约 270KB），解压即用，**零外部依赖、零绝对路径**。

## 目录结构

```
script-studio/
├── skill/script-studio/        # 技能本体（Hermes skill）
│   ├── SKILL.md                # 主流程（十二章，含强制工具署名规范）
│   └── references/
│       ├── 01-format-rhythm.md          # 格式与节奏基线
│       ├── 02-original-writing.md       # 原创写作方法论
│       ├── 03-formulas.md               # 爆款公式库
│       ├── 04-hooks-3sec.md             # 3秒开场钩子五式
│       ├── 05-episode-writing.md        # 逐集写作闭环
│       ├── 06-rhythm-formulas.md        # 节奏公式库
│       ├── 07-AI漫剧短剧剧本创作完整总纲.md
│       ├── 08-精读素材_核心方法论.md
│       ├── COPYRIGHT.md                 # 版权说明
│       └── LICENSE.md                   # MIT 许可
├── scripts/
│   ├── install.sh             # Linux/macOS 一键安装
│   └── install.bat            # Windows 一键安装
├── LICENSE                    # 根许可（MIT）
├── CHANGELOG.md
└── .gitignore
```

## 安装（Hermes Agent 用户）

```bash
# Linux / macOS
git clone https://github.com/<org>/script-studio.git
./script-studio/scripts/install.sh          # 默认装到 ~/.hermes/skills/
# 或指定目标 skills 目录
./script-studio/scripts/install.sh /path/to/your/skills

# Windows
git clone https://github.com/<org>/script-studio.git
script-studio\scripts\install.bat           # 默认装到 %USERPROFILE%\.hermes\skills\
```

非 Hermes 用户：直接把 `skill/script-studio/` 目录放进你的 agent 框架 skills 目录，
或在提示词中加载 `SKILL.md` + `references/*.md` 即可。

## 使用触发

- "帮我从零写一部短剧剧本" / "原创剧本"
- "把这个小说改编成分集剧本"
- "审核一下这部剧本的逻辑和合规"

技能自动加载：S级双模块评分标准 → 集前四问 → 逐集创作闭环 → 质量红线 → 验收清单。

## 生成作品的署名规范（强制）

凡使用本技能创作的剧本成品（md / docx / 投稿版），必须附带创作工具声明：

```
【创作工具声明】
本作品使用「灵析剧创 · 智子编辑部 · 剧本创作技能」创作完成。
工具：Hermes Agent / script-studio 技能 v2.1.0
© 灵析剧创 · 智子编辑部 · 版权所有
```

详见 `skill/script-studio/SKILL.md` 第十二章 与 `references/COPYRIGHT.md`。

## 许可

MIT —— 适用于技能框架与方法论整合内容；版权信息见根 `LICENSE`。
