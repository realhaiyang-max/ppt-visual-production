# PPT Visual Production

[中文说明](#中文说明) | [English](#english)

An approval-gated Codex skill for turning source material or approved slide content into visually coherent, editable presentations.

---

## 中文说明

### 项目简介

`ppt-visual-production` 是一个面向 Codex 的演示文稿生产 skill。它将内容规划、视觉方向探索、页面生产和可编辑 PPTX 构建组织成带审批门的工作流，并根据页面内容选择图片、原生 PowerPoint 图形或混合分层方案。

它解决的重点不是“自动套模板”，而是以下问题：

- 在视觉设计前锁定内容，避免文字和事实在制作过程中漂移。
- 提供三个结构明显不同的视觉方向，而不只是更换配色。
- 根据内容选择图像优先、原生优先或混合生产路线。
- 使用高清视觉底板与原生文字层兼顾视觉品质和可编辑性。
- 控制图片污染、文字溢出、连线偏移和最终渲染差异。
- 管理重复方案选择、修订、审批和最终交付版本。

### 适用场景

- 将报告、规划、方案或提纲制作成专业 PPT。
- 需要先比较多套视觉方向，再确认整套设计。
- 需要高质量图片效果，同时保留核心文字和图形可编辑。
- 同一任务可能经历多轮方案选择和版本修订。
- 需要逐页预览、PPT 回读检查和明确的可编辑性报告。

### 四阶段工作流

| 阶段 | 主要产物 | 审批门 |
|---|---|---|
| 1. 内容规划 | 逐页提纲、`content-lock` | 确认内容、页数和顺序 |
| 2. 视觉探索 | 三套完整方案总览图 | 选择视觉方向 |
| 3. 视觉生产 | 生产路线、逐页媒介规划、代表页或高清图稿 | 确认视觉系统 |
| 4. PPTX 构建 | 可编辑 PPTX、回读预览、可编辑性报告 | 确认整套并交付 |

每个阶段必须获得明确确认后才能进入下一阶段。方案总览图、逐页高清图和 PPT 回读预览是三种不同产物，不能混用名称或互相替代。

### 三种生产路线

| 路线 | 适用内容 | 典型产物 |
|---|---|---|
| 图像优先 | 场景、氛围、插画或复杂视觉构图占主导 | 完整逐页高清图稿 |
| 原生优先 | 矩阵、路线图、流程、架构和管理内容占主导 | 原生 PowerPoint 图形与代表页 |
| 混合路线 | 既需要高级视觉效果，又要求核心信息可编辑 | 高清视觉底板＋原生信息层 |

逐页高清图片不是所有项目的强制中间步骤。生产路线可以按整套选择，也可以按页面分别选择。

### 关键管控

- 精确文字、数据、标签和页码使用确定性排版，不依赖生成图片中的文字。
- 图片必须承担明确的信息或视觉功能，避免无意义堆叠和碎片化图片区域。
- 视觉底板不得包含需要准确呈现或经常修改的文字和业务数据。
- 最终化、字体变化或文件重建后，必须重新渲染实际 PPTX。
- 连线端点、水平垂直关系、模块对齐和图层遮挡需要专项检查。
- 已完成或已审批的产物不得覆盖；重新生成必须创建新轮次或修订。
- 同一任务内的三方案标签持续递增：`A/B/C`、`D/E/F`、`G/H/I`。
- 最终预览通过 SHA-256 与实际交付 PPTX 绑定。

### 安装

将仓库克隆到 Codex skills 目录。

Windows PowerShell：

```powershell
git clone https://github.com/realhaiyang-max/ppt-visual-production.git "$env:USERPROFILE\.codex\skills\ppt-visual-production"
```

macOS / Linux：

```bash
git clone https://github.com/realhaiyang-max/ppt-visual-production.git ~/.codex/skills/ppt-visual-production
```

### 使用示例

```text
使用 $ppt-visual-production 将这份三年规划制作成专业 PPT。
先确认逐页内容，再提供三套视觉方向供选择；最终交付可编辑 PPTX、回读预览和可编辑性说明。
```

也可以从中间阶段继续：

```text
使用 $ppt-visual-production。内容已经确认，请从视觉方向探索阶段开始。
```

### 仓库结构

```text
ppt-visual-production/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── artifact-versioning.md
│   ├── phase-1-content.md
│   ├── phase-2-style-exploration.md
│   ├── phase-3-slide-rendering.md
│   └── phase-4-pptx-reconstruction.md
├── scripts/
│   ├── build_montage.py
│   ├── check_slide_outputs.py
│   └── validate_manifest.py
└── tests/
    └── test_skill_tools.py
```

### 测试

辅助脚本需要 Python 3 和 Pillow。

```bash
python -m unittest discover -s tests -v
```

### 许可证

本项目采用 [MIT License](LICENSE)。

---

## English

### Overview

`ppt-visual-production` is a Codex skill for producing professional presentations through an approval-gated workflow. It separates locked content from visual treatment, then chooses images, native PowerPoint objects, or hybrid layers according to each slide's communication needs.

The skill is designed to:

- lock slide content before visual production;
- present three structurally distinct visual directions instead of palette-only variations;
- choose image-first, native-first, or hybrid production by content;
- combine high-resolution visual baseplates with editable native information;
- detect image pollution, text overflow, connector drift, and final-render differences;
- preserve traceability across repeated direction rounds, revisions, approvals, and delivery.

### When to Use

- Turning reports, plans, proposals, or approved outlines into professional decks.
- Comparing multiple visual directions before committing to a full deck.
- Combining polished visual assets with editable text and diagrams.
- Managing repeated design rounds and revisions within one task.
- Delivering slide previews, PPTX readback evidence, and an editability report.

### Four-Phase Workflow

| Phase | Main artifacts | Approval gate |
|---|---|---|
| 1. Content planning | Slide outline and `content-lock` | Approve content, count, and order |
| 2. Visual exploration | Three complete direction montages | Select a visual direction |
| 3. Visual production | Production route, slide media plan, representative slides or high-resolution visuals | Approve the visual system |
| 4. PPTX construction | Editable PPTX, readback preview, and editability report | Approve and deliver the complete deck |

Each phase requires explicit approval before the next phase begins. A direction montage, an individual high-resolution slide set, and a PPTX readback preview are distinct artifacts and must not be presented as interchangeable.

### Production Routes

| Route | Best for | Typical output |
|---|---|---|
| Image-first | Scene fidelity, atmosphere, illustration, and complex visual composition | Complete high-resolution slide set |
| Native-first | Matrices, roadmaps, processes, architecture, and management content | Native PowerPoint objects and representative slides |
| Hybrid | Slides that need both polished visuals and editable exact information | High-resolution visual baseplate plus native information layer |

High-resolution full-slide images are not mandatory for every project. Routes may be selected for the whole deck or per slide.

### Key Controls

- Exact copy, figures, labels, and page numbers use deterministic layout rather than generated image text.
- Images need a clear informational or visual role; unrelated stacks and fragmented image tiles are rejected.
- Visual baseplates must not contain exact or frequently edited business content.
- The actual PPTX is rendered again after finalization, font changes, or package rewrites.
- Connector endpoints, alignment, spacing, reading direction, and layer visibility receive dedicated QA.
- Completed or approved artifacts are immutable; reruns create new rounds or revisions.
- Direction labels remain unique within a task: `A/B/C`, then `D/E/F`, then `G/H/I`.
- Final readback previews are bound to the delivered PPTX through SHA-256 provenance.

### Installation

Clone the repository into the Codex skills directory.

Windows PowerShell:

```powershell
git clone https://github.com/realhaiyang-max/ppt-visual-production.git "$env:USERPROFILE\.codex\skills\ppt-visual-production"
```

macOS / Linux:

```bash
git clone https://github.com/realhaiyang-max/ppt-visual-production.git ~/.codex/skills/ppt-visual-production
```

### Usage Examples

```text
Use $ppt-visual-production to turn this three-year plan into a professional presentation.
Approve the slide content first, then show three visual directions. Deliver an editable PPTX, readback preview, and editability report.
```

Resume from a later phase when prerequisites already exist:

```text
Use $ppt-visual-production. The content is approved; start from visual direction exploration.
```

### Repository Structure

```text
ppt-visual-production/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── artifact-versioning.md
│   ├── phase-1-content.md
│   ├── phase-2-style-exploration.md
│   ├── phase-3-slide-rendering.md
│   └── phase-4-pptx-reconstruction.md
├── scripts/
│   ├── build_montage.py
│   ├── check_slide_outputs.py
│   └── validate_manifest.py
└── tests/
    └── test_skill_tools.py
```

### Tests

The helper scripts require Python 3 and Pillow.

```bash
python -m unittest discover -s tests -v
```

### License

This project is licensed under the [MIT License](LICENSE).
