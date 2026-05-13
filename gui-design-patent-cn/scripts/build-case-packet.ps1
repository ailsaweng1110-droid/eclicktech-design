param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [string]$OutputPath,

    [ValidateSet("auto", "markdown", "docx")]
    [string]$OutputFormat = "auto",

    [string]$TemplatePath,

    [switch]$ExportDocx,

    [string]$ExportOutputDir,

    [string]$DocxName = "02界面说明.docx",

    [string]$PythonExe = "python",

    [string]$ExportTemplatePath
)

function Get-StringValue {
    param(
        $Value,
        [string]$Fallback = "待补充"
    )

    if ($null -eq $Value) {
        return $Fallback
    }

    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) {
        return $Fallback
    }

    return $text.Trim()
}

function Join-List {
    param(
        $Value,
        [string]$Fallback = "待补充"
    )

    if ($null -eq $Value) {
        return $Fallback
    }

    $items = @($Value) | ForEach-Object {
        if ($null -ne $_) {
            ([string]$_).Trim()
        }
    } | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }

    if ($items.Count -eq 0) {
        return $Fallback
    }

    return ($items -join "、")
}

function Add-BulletBlock {
    param(
        [System.Collections.Generic.List[string]]$Lines,
        [string]$Title,
        [array]$Items
    )

    $Lines.Add("## $Title") | Out-Null
    foreach ($item in $Items) {
        $Lines.Add("- $item") | Out-Null
    }
    $Lines.Add("") | Out-Null
}

function Resolve-OutputPath {
    param(
        [string]$InputFilePath,
        [string]$RequestedOutputPath,
        [string]$RequestedFormat
    )

    if ([string]::IsNullOrWhiteSpace($RequestedOutputPath)) {
        $dir = Split-Path -Parent $InputFilePath
        $name = [System.IO.Path]::GetFileNameWithoutExtension($InputFilePath)
        return (Join-Path $dir "$name.word-prep.md")
    }

    $ext = [System.IO.Path]::GetExtension($RequestedOutputPath)
    if ($RequestedFormat -eq "docx" -or $ext -eq ".docx") {
        Write-Warning "当前脚本默认仍输出 Markdown 预填包（已改为 .md）。若要生成 DOCX + JPG，请在调用参数中追加 -ExportDocx，并确保已安装 requirements.txt（python-docx / Pillow）。"
    }

    if ($ext -eq ".md") {
        return $RequestedOutputPath
    }

    return ([System.IO.Path]::ChangeExtension($RequestedOutputPath, ".md"))
}

$resolvedInput = Resolve-Path -LiteralPath $InputPath -ErrorAction Stop
$resolvedOutputPath = Resolve-OutputPath -InputFilePath $resolvedInput.Path -RequestedOutputPath $OutputPath -RequestedFormat $OutputFormat

$raw = Get-Content -LiteralPath $resolvedInput.Path -Raw -Encoding UTF8 -ErrorAction Stop
$case = $raw | ConvertFrom-Json

$states = @($case.interface_states)
$stateCount = $states.Count
$stateNames = if ($stateCount -gt 0) {
    ($states | ForEach-Object { Get-StringValue -Value $_.name } | Where-Object { $_ -ne "待补充" })
} else {
    @()
}

$singleStateImagesReady = $false
if ($null -ne $case.single_state_images_ready) {
    $singleStateImagesReady = [bool]$case.single_state_images_ready
} elseif ($stateCount -gt 0) {
    $imagePaths = @($states | ForEach-Object { $_.image_path } | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) })
    if ($imagePaths.Count -eq $stateCount) {
        $singleStateImagesReady = $true
    }
}

$missingFields = New-Object System.Collections.Generic.List[string]
foreach ($field in @("carrier_product", "interface_states")) {
    $value = $case.$field
    if ($null -eq $value) {
        $missingFields.Add($field) | Out-Null
        continue
    }

    if ($value -is [string] -and [string]::IsNullOrWhiteSpace($value)) {
        $missingFields.Add($field) | Out-Null
        continue
    }

    if ($value -is [System.Collections.IEnumerable] -and -not ($value -is [string])) {
        if (@($value).Count -eq 0) {
            $missingFields.Add($field) | Out-Null
        }
    }
}

$productName = Get-StringValue -Value $case.product_name
if ($productName -eq "待补充" -and $null -ne $case.product_name_candidates) {
    $firstName = @($case.product_name_candidates) | Select-Object -First 1
    $productName = Get-StringValue -Value $firstName
}

$inventor = Get-StringValue -Value $case.inventor
$applicant = Get-StringValue -Value $case.applicant
$dateText = Get-StringValue -Value $case.date -Fallback (Get-Date -Format "yyyy年M月d日")
$domain = Get-StringValue -Value $case.domain -Fallback "软件界面外观设计"
$carrierProduct = Get-StringValue -Value $case.carrier_product
$filingGoal = Get-StringValue -Value $case.filing_goal
$designPoints = Join-List -Value $case.core_novelty

$summaryLines = New-Object System.Collections.Generic.List[string]
$summaryLines.Add("本外观设计产品用于在${carrierProduct}上展示，用于${filingGoal}的图形用户界面。") | Out-Null
if ($stateNames.Count -gt 0) {
    $summaryLines.Add("包括：$($stateNames -join '、')。") | Out-Null
}
if ($designPoints -ne "待补充") {
    $summaryLines.Add("本外观设计的设计要点在于$designPoints。") | Out-Null
} else {
    $summaryLines.Add("本外观设计的设计要点请结合单张状态图进一步补充。") | Out-Null
}

$interactionText = Get-StringValue -Value $case.interaction_summary -Fallback ""
if ([string]::IsNullOrWhiteSpace($interactionText)) {
    if ($stateNames.Count -gt 1) {
        $interactionText = "用户按照状态图顺序在各界面之间进行操作和跳转，完成从起始界面到后续状态界面的连续交互流程。"
    } else {
        $interactionText = "请根据最终保留状态图补充交互说明。"
    }
}

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# 最终 Word 成稿前预填包") | Out-Null
$lines.Add("") | Out-Null

$fieldItems = @(
    "日期：$dateText",
    "专利类型：$(Get-StringValue -Value $case.patent_type -Fallback 'GUI外观设计专利')",
    "领域：$domain",
    "专利名称：$productName",
    "申请人：$applicant",
    "发明人：$inventor",
    "身份证号：$(Get-StringValue -Value $case.id_card)",
    "手机：$(Get-StringValue -Value $case.phone)",
    "邮箱：$(Get-StringValue -Value $case.email)"
)
Add-BulletBlock -Lines $lines -Title "标准模板字段" -Items $fieldItems

$imageCheckItems = @(
    "最终保留状态图数量：$stateCount",
    "状态图名称：$(if ($stateNames.Count -gt 0) { $stateNames -join '、' } else { '待补充' })",
    "单张状态图是否已齐：$(if ($singleStateImagesReady) { '是' } else { '否' })"
)
if (-not $singleStateImagesReady) {
    $imageCheckItems += "进入最终Word前，必须补齐每个保留状态对应的单张状态图。"
}
Add-BulletBlock -Lines $lines -Title "单张状态图检查" -Items $imageCheckItems

$gapItems = New-Object System.Collections.Generic.List[string]
if ($missingFields.Count -eq 0) {
    $gapItems.Add("最小必填字段已齐。") | Out-Null
} else {
    foreach ($field in $missingFields) {
        $gapItems.Add("缺少字段：$field") | Out-Null
    }
}
Add-BulletBlock -Lines $lines -Title "成稿前检查" -Items $gapItems

$lines.Add("## 摘要草稿") | Out-Null
foreach ($line in $summaryLines) {
    $lines.Add($line) | Out-Null
}
$lines.Add("") | Out-Null

$lines.Add("## 各界面状态说明草稿") | Out-Null
if ($stateCount -eq 0) {
    $lines.Add("请先补充最终保留状态图。") | Out-Null
    $lines.Add("") | Out-Null
} else {
    $index = 1
    foreach ($state in $states) {
        $stateName = Get-StringValue -Value $state.name -Fallback ("状态图{0:D2}" -f $index)
        $stateSummary = Get-StringValue -Value $state.description -Fallback ""
        if ([string]::IsNullOrWhiteSpace($stateSummary)) {
            $stateSummary = Get-StringValue -Value $state.summary -Fallback "请根据该单张状态图补充客观界面描述。"
        }

        $lines.Add("## 变化状态图{0:D2} · $stateName" -f $index) | Out-Null
        $lines.Add($stateSummary) | Out-Null
        if (-not [string]::IsNullOrWhiteSpace([string]$state.image_path)) {
            $lines.Add("对应单张图：$($state.image_path)") | Out-Null
        }
        $lines.Add("") | Out-Null
        $index += 1
    }
}

$lines.Add("## 交互说明草稿") | Out-Null
$lines.Add($interactionText) | Out-Null
$lines.Add("") | Out-Null

$lines.Add("## 脚本说明") | Out-Null
$lines.Add("Markdown 预填包用于 chat / 代理人复核；正式 DOCX + JPG 请运行 scripts/export_gui_patent_docx.py，或使用 build-case-packet.ps1 -ExportDocx。") | Out-Null
$lines.Add("") | Out-Null

$outDir = Split-Path -Parent $resolvedOutputPath
if (-not [string]::IsNullOrWhiteSpace($outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

Set-Content -LiteralPath $resolvedOutputPath -Value $lines -Encoding UTF8

Write-Output "Created $resolvedOutputPath"

if ($ExportDocx) {
    $repoRoot = Split-Path -Parent $PSScriptRoot
    $pyScript = Join-Path $PSScriptRoot "export_gui_patent_docx.py"
    if (-not (Test-Path -LiteralPath $pyScript)) {
        Write-Error "找不到 Python 导出脚本：$pyScript"
        exit 1
    }

    $defaultTemplate = Join-Path $repoRoot "assets\\word-template.docx"
    $tpl = $defaultTemplate
    if (-not [string]::IsNullOrWhiteSpace($ExportTemplatePath)) {
        $tpl = $ExportTemplatePath
    }
    elseif (-not [string]::IsNullOrWhiteSpace($TemplatePath)) {
        $tpl = $TemplatePath
    }

    $inputDir = Split-Path -Parent $resolvedInput.Path
    $outDir = if (-not [string]::IsNullOrWhiteSpace($ExportOutputDir)) {
        $ExportOutputDir
    }
    else {
        Join-Path $inputDir "gui-patent-export"
    }

    New-Item -ItemType Directory -Force -Path $outDir | Out-Null

    $pyArgs = @(
        $pyScript,
        "--input", $resolvedInput.Path,
        "--template", $tpl,
        "--output-dir", $outDir,
        "--docx-name", $DocxName
    )

    Write-Output "Running DOCX export via $PythonExe..."
    & $PythonExe @pyArgs
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Python DOCX 导出失败，退出码 $LASTEXITCODE"
        exit $LASTEXITCODE
    }
}


