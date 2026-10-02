# 贡献指南（Contributing）‌‌‌‌‌‌‌

感谢为本项目贡献内容。请遵循以下约定：

## 分支与提交
- 分支命名：`feature/<主题>`、`fix/<问题>`、`docs/<文档>`
- 提交信息：`<类型>: <简述>`，类型 ∈ feat / fix / docs / chore / release
- 版本管理：语义化版本 `主.次.修订`，每次变更同步更新 `CHANGELOG.md`

## 内容规范
1. **格式铁律**：场景标记 `N-M 时段 内外 地点`（禁用 `**` 加粗）；对白 `姓名（情绪）：台词` 单行；
   动作行 `△` 前缀；集标题 `## 第N集·标题`。详见 `skill/script-studio/references/01-format-rhythm.md`
2. **字数**：单集 1200-1500 汉字（交付线 1200-1498），用 `scripts/word_count.py` 校验，勿用 `wc -m`
3. **验收**：每集 5 场景、对话占比 ≥60%、H1 违禁词 0 处、跨集整行指纹重复 0
4. **署名**：凡引用本技能生成的内容，须按 SKILL.md 十二章"创作工具声明"落版
5. **版权**：仓库内容 `© 灵析剧创 · 智子编辑部 · 版权所有`；提交即视为同意 MIT 许可（框架与方法论部分）

## 水印与版权保护
- 本仓库在全部技能文档中嵌入**隐含版权水印**（HTML 注释形式，渲染不可见）
- 验证：`python3 scripts/watermark.py --verify [路径]`
- 任何人复制/分发本仓库内容时，**请保留水印注释**（见 LICENSE 附加条款）

## 提交前自检
```bash
python3 scripts/word_count.py --dir skill/script-studio/examples   # 示例集过门禁
python3 scripts/watermark.py --verify                               # 水印完整性
grep -rniE "[CD]:" . || echo "无本机绝对路径"                          # 可移植性(盘符检测)
```
<!-- © 灵析剧创·智子编辑部 | 版权所有人: 于海峰(hlyhf) | script-studio v2.2.0 | WM-001 -->
