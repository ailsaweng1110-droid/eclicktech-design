from __future__ import annotations

import json
import sys
from pathlib import Path

from docx import Document
from PIL import Image


def _load_exporter(repo_root: Path):
    scripts_dir = repo_root / "scripts"
    sys.path.insert(0, str(scripts_dir))
    import export_gui_patent_docx as exporter  # noqa: E402

    return exporter


def test_export_generates_docx_and_jpg(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    exporter = _load_exporter(repo_root)

    template = repo_root / "assets" / "word-template.docx"
    assert template.is_file()

    img_path = tmp_path / "shot.png"
    Image.new("RGB", (120, 80), color=(240, 240, 240)).save(img_path)

    case = {
        "date": "2026年5月13日",
        "patent_type": "GUI外观设计专利",
        "domain": "软件界面外观设计",
        "product_name": "测试图形用户界面",
        "carrier_product": "智能手机",
        "filing_goal": "演示业务流程",
        "applicant": "示例申请人公司",
        "inventor": "张三",
        "id_card": "110101199001011234",
        "phone": "13800000000",
        "email": "demo@example.com",
        "interaction_summary": "如图01所示进入界面；如图02所示完成提交。",
        "core_novelty": ["示例布局要点A", "示例交互要点B"],
        "interface_states": [
            {
                "name": "示例首页",
                "description": "页面中部展示示例卡片与示例按钮。",
                "image_path": img_path.name,
            },
            {
                "name": "示例提交页",
                "description": "页面底部展示示例提交控件。",
                "image_path": img_path.name,
            },
        ],
    }

    json_path = tmp_path / "case.json"
    json_path.write_text(json.dumps(case, ensure_ascii=False, indent=2), encoding="utf-8")

    out_dir = tmp_path / "out"
    docx_out, jpgs = exporter.export_case(json_path, template, out_dir)

    assert docx_out.is_file()
    assert len(jpgs) == 2
    assert jpgs[0].suffix.lower() == ".jpg"

    doc = Document(str(docx_out))
    texts = "\n".join(p.text for p in doc.paragraphs)
    assert "界面说明如下：" in texts
    assert "摘要：" in texts
    assert "示例首页（变化状态图01）" in texts
    assert "示例提交页（变化状态图02）" in texts
    assert "交互说明：" in texts
