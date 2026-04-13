#!/bin/bash

# ============================================================
#  zMaticoo DSP Design Skill 一键安装脚本
#
#  团队成员安装命令（复制发给团队即可）：
#  bash <(curl -fsSL https://raw.githubusercontent.com/【你的GitHub用户名】/【你的仓库名】/main/install.sh)
#
#  规范更新后，团队成员执行：
#  update-zmaticoo-skill
# ============================================================

set -e

# ────────────────────────────────────────────
# 【需要替换】第1处：填写你的 GitHub 用户名和仓库名
# 格式：用户名/仓库名
# 例如：zmaticoo-team/design-system
# ────────────────────────────────────────────
REPO="【你的GitHub用户名】/【你的仓库名】"

# ────────────────────────────────────────────
# 【需要替换】第2处：填写 skill 文件所在的分支名
# 通常是 main 或 master，保持默认即可
# ────────────────────────────────────────────
BRANCH="main"

# ────────────────────────────────────────────
# 【需要替换】第3处：填写 skill 文件在 repo 中的路径
# 如果你把文件放在 repo 根目录的 .claude/skills/zmaticoo-design/ 下，保持默认即可
# 如果放在其他位置（如 design/skills/zmaticoo-design/），需要修改
# ────────────────────────────────────────────
SKILL_PATH=".claude/skills/zmaticoo-design"

# ============================================================
# 以下内容无需修改
# ============================================================

BASE_URL="https://raw.githubusercontent.com/$REPO/$BRANCH/$SKILL_PATH"
DEST="$HOME/.claude/skills/zmaticoo-design"

echo ""
echo "📦 正在安装 zmaticoo-design skill..."
echo "   来源：https://github.com/$REPO"
echo ""

# 检查 curl 是否可用
if ! command -v curl &> /dev/null; then
  echo "❌ 未找到 curl，请先安装 curl 后重试"
  exit 1
fi

# 创建目录
mkdir -p "$DEST/references"

# 下载文件
echo "⬇️  下载 SKILL.md..."
curl -fsSL "$BASE_URL/SKILL.md" -o "$DEST/SKILL.md"

echo "⬇️  下载 DESIGN_SPEC.md..."
curl -fsSL "$BASE_URL/references/DESIGN_SPEC.md" -o "$DEST/references/DESIGN_SPEC.md"

echo "⬇️  下载 tokens.css..."
curl -fsSL "$BASE_URL/references/tokens.css" -o "$DEST/references/tokens.css"

# 注册 update 命令到 shell 配置文件
INSTALL_CMD="bash <(curl -fsSL https://raw.githubusercontent.com/$REPO/$BRANCH/install.sh)"
UPDATE_ALIAS="alias update-zmaticoo-skill='$INSTALL_CMD'"

# 自动检测 zsh 或 bash
if [ -f "$HOME/.zshrc" ]; then
  SHELL_RC="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
  SHELL_RC="$HOME/.bashrc"
else
  SHELL_RC="$HOME/.zshrc"
  touch "$SHELL_RC"
fi

if ! grep -q "update-zmaticoo-skill" "$SHELL_RC"; then
  echo "" >> "$SHELL_RC"
  echo "# zMaticoo DSP Design Skill" >> "$SHELL_RC"
  echo "$UPDATE_ALIAS" >> "$SHELL_RC"
  source "$SHELL_RC" 2>/dev/null || true
fi

# 完成提示
echo ""
echo "✅ 安装完成！skill 已保存至："
echo "   $DEST"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  使用方式："
echo ""
echo "  1. cd 进入任意项目目录"
echo "  2. 输入 claude 启动 Claude Code"
echo "  3. 对话里输入：/figma-use /zmaticoo-design"
echo ""
echo "  规范更新时，执行：update-zmaticoo-skill"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
