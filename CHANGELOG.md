# Changelog‌‌‌‌‌‌‌

本仓库遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/) 规范。

## [2.2.0] - 2026-09-14

### Added
- **多 Agent 平台通用化**：`docs/agent-adapters.md` 适配矩阵（Hermes / Claude Code / Cursor / DeepSeek / 豆包 / 腾讯元宝 / WorkBuddy / OpenClaw / 自建RAG）
- **隐含版权水印**：`scripts/watermark.py` 双层水印（L1 HTML注释 + L2 零宽字符嵌入#标题行，渲染不可见/源码可验），版权所有人于海峰(hlyhf)，全库17文件已打
- **GitHub 资料层**：`examples/示例_单集剧本格式示范.md`、`docs/agent-adapters.md`、`CONTRIBUTING.md`
- **通用工具脚本**：`scripts/word_count.py`（跨平台单集门禁校验器，纯标准库，CJK/场景/复读/对话占比/付费卡点/H1 一键校验）

### Changed
- 版本号统一升至 v2.2.0（全库引用同步）

## [2.1.0] - 2026-09-14

### Added
- 包内自包含知识库（references/01~08），零外部路径依赖，可跨机/跨用户复用
- 版权与创作工具署名规范（SKILL.md 十二章 + COPYRIGHT.md + LICENSE.md）
- GitHub 通用化：根 LICENSE/README/CHANGELOG/.gitignore、跨平台安装脚本

### Changed
- 品牌统一为「© 灵析剧创 · 智子编辑部 · 版权所有」
- frontmatter author 字段去个人化，version 提升至 2.1.0

### Removed
- 全部外部知识库路径引用（原 NAS 绝对路径表）
- 内嵌 AI 工具对比表中的第三方品牌条目（07 文件）

## [2.0.0] - 2026-09-14

### Added
- 整合内部知识库资源（爆款公式/节奏公式/方法论总纲/精读素材），v2.0 品牌化
<!-- © 灵析剧创·智子编辑部 | 版权所有人: 于海峰(hlyhf) | script-studio v2.2.0 | WM-001 -->
