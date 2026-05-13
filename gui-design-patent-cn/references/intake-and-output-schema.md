# Intake And Output Schema

用这个参考文件把零散案件材料整理成结构化输入：

- `scripts/build-case-packet.ps1` → **Markdown 预填包**（便于 chat review）。
- `scripts/export_gui_patent_docx.py` → **`02界面说明.docx` + `jpg/` 图片包**（推荐最终交付）。

## Recommended JSON Shape

```json
{
  "date": "2026年4月30日",
  "patent_type": "GUI外观设计专利",
  "domain": "软件界面外观设计",
  "product_name": "电子设备的广告智能投放图形用户界面",
  "product_name_candidates": [
    "电子设备的广告智能投放图形用户界面"
  ],
  "applicant": "",
  "inventor": "曹振",
  "id_card": "待补充",
  "phone": "18967105815",
  "email": "example@example.com",
  "carrier_product": "PC端、平板电脑",
  "filing_goal": "帮助广告主进行广告智能投放分析",
  "core_novelty": [
    "顶部问答区域与中部图表区域的组合布局",
    "下钻分析与报表状态的多状态界面呈现"
  ],
  "single_state_images_ready": true,
  "interaction_summary": "用户按照状态图顺序在各界面之间进行操作和跳转，完成从首页分析到下钻决策的连续交互流程。",
  "interface_states": [
    {
      "name": "AI投放工作台首页",
      "description": "页面上部显示问候信息和提示语，中部显示图表和摘要区域，下部显示建议卡片和输入区域。",
      "image_path": "01-homepage.jpg"
    },
    {
      "name": "Asset Details下拉选择状态",
      "description": "用户点击Asset Details后展开下拉菜单，菜单中显示多个资产名称供选择。",
      "image_path": "02-asset-details.jpg"
    }
  ]
}
```

## Minimum Required Fields

这些字段缺失时，脚本生成的预填包只能作为半成品：

- `carrier_product`
- `interface_states`

## Useful Optional Fields

这些字段建议提供，便于直接落标准模板：

- `summary_intro`：覆盖摘要首段「用于…展示」句式（不传则按 `carrier_product` + `filing_goal` 自动生成）。
- `summary_bullets`：摘要下列列表条目（不传则默认使用各状态名称）。
- `design_points_sentence`：完整的「本外观设计的设计要点在于……。」句式（不传则由 `core_novelty` 拼接）。
- `inventors`：多位发明人数组（每项含 `name` / `id_card`），最多 8 位；不传则退回单字段 `inventor` + `id_card`。
- `fixed_phone`：模板「固定电话：」字段（不传则为 `(补充信息)`）。
- `inventor_contact_phone`：`发明联系方式：`前缀专用号码（不传则退回 `phone`）。
- `date`
- `patent_type`
- `domain`
- `product_name`
- `product_name_candidates`
- `applicant`
- `inventor`
- `id_card`
- `phone`
- `email`
- `filing_goal`
- `core_novelty`
- `interaction_summary`
- `single_state_images_ready`
- `interface_states[].description`
- `interface_states[].image_path`

## Output Sections

脚本默认输出这些板块：

- 标准模板字段
- 单张状态图检查
- 成稿前检查
- 摘要草稿
- 各界面状态说明草稿
- 交互说明草稿

不再默认输出：

- 案件摘要
- 申请策略建议
- 视图计划
- 风险与待确认事项

## Usage

```powershell
powershell.exe -ExecutionPolicy Bypass -File .\scripts\build-case-packet.ps1 -InputPath .\case.json -OutputPath .\word-prep.md

# 需要在生成 Markdown 的同时导出 DOCX + JPG 时追加：
powershell.exe -ExecutionPolicy Bypass -File .\scripts\build-case-packet.ps1 `
  -InputPath .\case.json `
  -ExportDocx `
  -ExportOutputDir .\dist `
  -ExportTemplatePath .\assets\word-template.docx
```

如果 `-OutputPath` 省略，脚本会在输入文件同目录生成同名 `.word-prep.md` 文件。  
如果误传入 `.docx` 输出路径，脚本会自动改写为 `.md`，除非显式传入 `-ExportDocx` 触发 Python 导出器。

## DOCX / JPG 导出

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/export_gui_patent_docx.py \
  --input ./case.json \
  --template ./assets/word-template.docx \
  --output-dir ./dist \
  --docx-name 02界面说明.docx
```

导出目录结构：

```text
dist/
├─ 02界面说明.docx
└─ jpg/
   ├─ 变化状态图01_示例首页.jpg
   └─ ...
```
