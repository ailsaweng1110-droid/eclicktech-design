# raw.json Schema 参考

> 每次提取时自动生成，路径：`.design-spec-extractor/raw.json`
> 过程文件，隐藏目录，不进入正式产物，无需人工维护。
> 用途：记录所有原始数据，供出现问题时回溯定位。

---

## 写入规则

- 所有维度的**全部发现值**都要记录，包括只出现 1 次的孤立值，禁止提前筛选
- `occurrences` 记录出现次数，`locations` 记录发现位置（页面/组件路径）
- `conflicts_detected` 记录检测到的冲突，`severity` 分 high / medium / low
- `anomalies` 记录不符合规律的异常值，附说明
- `semantic_guess` 是 AI 的语义推断，标注候选/主要/疑似历史遗留等，供归一阶段使用
- **禁止在 raw.json 中做任何筛选或归一**，归一工作在输出 tokens.css 阶段进行

---

## 完整 Schema

```json
{
  "_meta": {
    "extracted_at": "YYYY-MM-DD HH:mm:ss",
    "source_type": "figma-mcp | figma-link | screenshot",
    "source": "Figma 文件链接 或 截图文件名",
    "pages_analyzed": ["登录页", "主导航", "数据列表页", "表单页", "详情页"],
    "tool": "design-spec-extractor v4.1",
    "note": "原始提取数据，未经归一处理，仅供回溯使用"
  },

  "colors": {
    "all_found": [
      {
        "value": "#1677FF",
        "occurrences": 3,
        "locations": ["登录页/主按钮", "列表页/操作按钮", "导航/激活状态"],
        "semantic_guess": "primary（候选）"
      },
      {
        "value": "#165DFF",
        "occurrences": 9,
        "locations": ["表单页/主按钮", "详情页/链接", "弹窗/确认按钮"],
        "semantic_guess": "primary（主要）"
      },
      {
        "value": "#1890FF",
        "occurrences": 1,
        "locations": ["登录页/旧版组件"],
        "semantic_guess": "疑似历史遗留，已标注"
      }
    ],
    "conflicts_detected": [
      {
        "type": "primary_color_mismatch",
        "severity": "high",
        "values": ["#1677FF", "#165DFF"],
        "recommendation": "以出现频次最高的 #165DFF 为准"
      }
    ]
  },

  "typography": {
    "all_found": [
      {
        "font_size": "12px",
        "font_weight": "400",
        "line_height": "20px",
        "occurrences": 24,
        "locations": ["..."]
      },
      {
        "font_size": "14px",
        "font_weight": "400",
        "line_height": "22px",
        "occurrences": 38,
        "locations": ["..."]
      },
      {
        "font_size": "13px",
        "font_weight": "400",
        "line_height": "20px",
        "occurrences": 2,
        "locations": ["表单页某组件"],
        "semantic_guess": "疑似孤立值"
      }
    ],
    "anomalies": [
      {
        "value": "13px/400",
        "occurrences": 2,
        "note": "不符合字号梯度规律，已标注为待确认"
      }
    ]
  },

  "spacing": {
    "all_found": [4, 8, 12, 16, 20, 24, 32, 40, 48, 13, 25],
    "base_unit_guess": "4px 或 8px",
    "anomalies": [
      {
        "value": "13px",
        "locations": ["表单页某行间距"],
        "note": "不符合步进规律，疑似手动调整"
      },
      {
        "value": "25px",
        "locations": ["详情页某模块间距"],
        "note": "不符合步进规律，疑似手动调整"
      }
    ]
  },

  "radius": {
    "all_found": [
      { "value": "4px", "occurrences": 18, "locations": ["输入框", "下拉菜单", "标签"] },
      { "value": "6px", "occurrences": 8,  "locations": ["卡片", "弹窗内输入框"] },
      { "value": "8px", "occurrences": 4,  "locations": ["卡片", "面板"] },
      {
        "value": "16px",
        "occurrences": 1,
        "locations": ["某特定弹窗"],
        "note": "超出 B 端常规范围（>12px），已标注待确认"
      }
    ],
    "conflicts_detected": [
      {
        "type": "input_radius_mismatch",
        "severity": "medium",
        "values": ["4px（表单页）", "6px（弹窗内）"],
        "recommendation": "以 4px 为准，弹窗内值疑似继承覆盖"
      }
    ]
  },

  "shadows": {
    "all_found": [
      {
        "value": "0 2px 8px rgba(0,0,0,0.12)",
        "occurrences": 6,
        "locations": ["卡片hover", "下拉菜单"]
      },
      {
        "value": "0 4px 16px rgba(0,0,0,0.16)",
        "occurrences": 3,
        "locations": ["弹窗", "抽屉"]
      },
      {
        "value": "0 1px 4px rgba(0,0,0,0.08)",
        "occurrences": 2,
        "locations": ["固定表头"]
      }
    ]
  },

  "layout": {
    "sidebar_width_found": ["240px", "260px"],
    "topbar_height_found": ["48px", "56px"],
    "conflicts_detected": [],
    "anomalies": []
  },

  "motion": {
    "durations_found": ["100ms", "200ms", "300ms"],
    "easings_found": ["cubic-bezier(0.4,0,0.2,1)"],
    "anomalies": []
  }
}
```

---

## 不一致上报话术（检测到 conflicts_detected 时使用）

```
在读取设计稿时，发现以下规范不一致，需要您确认：

🔴 【[类型] · [严重级别]】
   [描述冲突内容，列出各版本值和出现次数]
   → 建议：[recommendation 字段内容]
   → 请确认，或告知正确值

在您确认前，以上维度暂不写入 tokens.css，其余规范继续提取。
```

用户确认后可选：
- **A** 确认建议值
- **B** 指定正确值
- **C** 标注冲突注释，等设计稿修复后同步
- **D** 跳过此维度，标注「规范不一致·待确认」

冲突标注格式（选项 C）写入 tokens.css：
```css
/* ⚠️ 规范不一致·待确认
   发现 2 个版本：#1677FF（3处）vs #165DFF（9处）
   建议统一为 #165DFF，请设计师确认后更新此值 */
--color-primary: #165DFF;
```
