# GUI Design Patent CN

用于中国大陆 GUI 外观设计专利案件的 Codex skill。

这个 skill 的目标不是只生成一段说明，而是把 GUI 专利案件从材料整理、结构判断、视图规划，一直推进到逐图说明、简要说明和可选的 Word 交底初稿。

## 这个仓库包含什么

- `SKILL.md`
  这是主技能文件，定义整个工作流、触发条件、默认输出和风险处理方式。
- `references/`
  这里放规则说明、起草流程说明，以及单张总图模式的完整示例。
- `scripts/`
  这里放辅助脚本，例如把案件信息整理成结构化工作包。
- `assets/`
  这里放模板资产，例如案件输入模板和 Word 模板。

## 适用场景

适用于这些需求：

- 用户说“我要做 GUI 专利”“界面外观设计专利怎么写”
- 用户上传了 GUI 截图、状态图、总图或交互流程
- 用户希望得到中国大陆 GUI 外观设计专利的申请结构建议
- 用户希望自动生成逐图界面说明、简要说明、交互说明
- 用户希望整理成交底材料或 Word 初稿

## 支持的两种图片工作流

### 1. 单张总图模式

用户直接上传一张大图，其中已经包含全部或大部分 GUI 图。

skill 会按这个顺序处理：

1. 提示如何上传总图
2. 识别总图中的子图数量与顺序
3. 输出总图拆分识别结果
4. 输出逐图界面说明草稿
5. 输出逐图审核结果
6. 再进入简要说明和交互说明

示例见：

- `references/single-composite-example.md`

### 2. 多张分图模式

用户按状态逐张上传截图。

skill 会按这个顺序处理：

1. 生成截图上传指引
2. 按顺序逐图分析
3. 输出逐图界面说明草稿
4. 输出逐图审核结果
5. 再进入简要说明和交互说明

## skill 的核心特点

- 默认按中国大陆 GUI 外观设计专利口径处理
- 尽量先产出一版可推进的结果，而不是一开始反复追问
- 先判断主案、相似设计、分案结构，再写说明
- 支持动态 GUI、静态 GUI、局部设计、相似设计
- 支持单张总图拆图分析
- 支持结构化输入与脚本化输出

## 本地文件结构

```text
gui-design-patent-cn/
├─ SKILL.md
├─ README.md
├─ requirements.txt
├─ agents/
│  └─ openai.yaml
├─ assets/
│  ├─ case-intake-template.json
│  └─ word-template.docx
├─ references/
│  ├─ cnipa-gui-rules.md
│  ├─ company-word-template-rules.md
│  ├─ drafting-workflow.md
│  ├─ intake-and-output-schema.md
│  └─ single-composite-example.md
├─ tests/
│  └─ test_export_smoke.py
└─ scripts/
   ├─ build-case-packet.ps1
   └─ export_gui_patent_docx.py
```

## 如何在 Codex 中使用

当用户提到 GUI 专利、界面专利、图形用户界面外观设计专利，或者上传界面截图、状态图、总图时，触发这个 skill。

典型调用方式：

- “帮我做这个 GUI 的外观设计专利申请方案”
- “我有一张总图，你帮我分析并写 GUI 专利”
- “请给我逐图界面说明和简要说明草稿”

## 脚本使用示例

如果你已经有结构化案件输入，可以运行：

```powershell
powershell.exe -ExecutionPolicy Bypass -File .\scripts\build-case-packet.ps1 -InputPath .\assets\case-intake-template.json -OutputPath .\generated-case-packet.md
```

生成与公司模板一致的 `02界面说明.docx` + `jpg/` 图片包（推荐最终交付）：

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/export_gui_patent_docx.py \
  --input .\case.json \
  --template .\assets\word-template.docx \
  --output-dir .\dist \
  --docx-name 02界面说明.docx
```

Windows PowerShell 亦可 `--ExportDocx`（详见 `references/intake-and-output-schema.md`）。

运行自动化自检：

```bash
.venv/bin/pytest -q
```

## 发布到 GitHub 的最简单方法

如果你不想碰命令行，最简单的方法是：

1. 在 GitHub 网站新建一个空仓库
2. 打开本地 `gui-design-patent-cn` 文件夹
3. 把这个文件夹里的全部文件直接拖进 GitHub 仓库网页
4. 填写一次提交说明并提交

如果仓库里已经存在自动生成的 `README.md`、`.gitignore` 或 `LICENSE`，建议先删除或改为空仓库后再上传当前项目文件。

## 注意事项

- 这个 skill 生成的是工作草稿，不替代专利代理人或律师的最终复核。
- 涉及公开时间、权属、优先权、动态链是否成立等高风险问题时，仍需专业复核。
- 若截图无法清楚表达状态关系，建议补充更清晰的总图、分图或录屏帧。
