#!/usr/bin/env bash
# 安装 script-studio 技能到 Hermes Agent skills 目录
# 用法: ./install.sh [目标skills目录]   默认: ~/.hermes/skills
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${1:-$HOME/.hermes/skills}"
mkdir -p "$DEST"
rm -rf "$DEST/script-studio"
cp -r "$REPO_ROOT/skill/script-studio" "$DEST/"
echo "✅ script-studio 已安装到 $DEST/script-studio"
echo "   重启 Hermes Agent 会话后自动可用（触发词: 原创剧本/改编剧本/审核剧本）"
