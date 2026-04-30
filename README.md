# DGT Lesson Plan Generator

An agentic workflow for generating professional, SCSA-aligned **Learning Experience Plans (LEP)** for Digital Technologies education in Western Australia. Designed for ECU pre-service teachers (PSTs), this system takes raw teaching ideas and produces fully formatted, publication-ready Word documents through a structured multi-step pipeline.

---

## Overview

This project automates the creation of lesson plans from scratch (or from revision notes) by combining curriculum alignment, expert pedagogical rules, structured JSON generation, and Word document injection — all driven by an AI agent following a defined workflow.

**What you put in:** A brief or detailed teaching idea (`Insights/Insights.md`).

**What you get out:** Two polished `.docx` lesson plan files — one in English, one in Chinese — ready for ECU practicum submission.

---

## Project Structure

```
DGT/
├── WorkFlow.txt                  # Master workflow instructions for the AI agent
├── Injection.py                  # Python script: injects JSON data into the Word template
│
├── Insights/
│   └── Insights.md               # YOUR INPUT: teaching ideas, inspirations, lesson notes
│
├── References/
│   ├── SCSA-Curriculum.md        # Western Australia SCSA Digital Technologies curriculum
│   ├── OfficialExample.json      # Official lesson plan structure reference
│   ├── Template.docx             # Word template with placeholders (x01–x91)
│   └── Debug.md                  # Log of past errors and their solutions
│
├── EditingRules/
│   ├── 01_Role_Objective.md      # AI persona, teaching philosophy, and core objectives
│   ├── 02_Generative_Logic.md    # Pedagogical logic: 5E, PRIMM, Bloom's, assessment models
│   ├── 04_Language_Style.md      # Language register, style, and terminology rules
│   ├── 05_Length_Constraints.md  # Length limits, formatting, and JSON rendering syntax
│   └── 07_Feedbacks_and_Observations.md  # Real mentor feedback — highest priority rules
│
├── GeneratingRules/
│   ├── Schema.md                 # JSON structure, list formatting, and rich-text tag guide
│   └── KeyDefinitions.md         # Definitions for every JSON key (x01–x61)
│
├── ExtraDocs/                    # Supplementary reference documents (agent reads as needed)
│
└── Tmp/                          # Temporary intermediate files created by the agent
```

---

## Prerequisites

**Python** and the `docxtpl` library must be installed to run `Injection.py`.

```bash
pip install docxtpl
```

---

## How It Works

The workflow has two modes: **Default Mode** (generate a new lesson plan) and **Revision Mode** (revise an existing one). Both are triggered by telling the AI agent to follow `WorkFlow.txt`.

In both modes, the AI agent reads your inputs, generates a series of intermediate documents, and ultimately runs `Injection.py` to produce the final `.docx` files.

---

## Mode 1: Default Mode (Generate a New Lesson Plan)

### When to Use

Use this when you want to create a brand-new lesson plan from a teaching idea.

### How to Trigger

Provide your teaching idea in `Insights/Insights.md`, then tell the agent:

> "Follow WorkFlow.txt and generate a lesson plan."

Do **not** include the word "Revise" or "修改" in your prompt — that triggers Revision Mode instead.

### What the Agent Does (Step by Step)

| Step | Action | Output File |
|------|--------|-------------|
| **1** | Reads your `Insights/Insights.md` and cross-references `References/SCSA-Curriculum.md` to find the most relevant curriculum content codes (e.g., `WA8DIGDR1`). Records the mapping with justification. | `SCSA Connection.md` |
| **2** | Drafts a complete lesson plan in English using your ideas, curriculum links, and rules from `EditingRules/`. The plan is in two parts: a human-readable narrative and a key-value mapping of all required JSON fields. Then faithfully translates it into Chinese. | `DraftPlan.md` (EN) `DraftPlan-zh.md` (ZH) |
| **3** | Extracts the lesson plan into a strictly structured JSON file (English only, keys `x01`–`x61`), then produces a Chinese version with the same keys but Chinese content. | `LessonPlan.json` (EN) `LessonPlan-zh.json` (ZH) |
| **4** | Runs `Injection.py` on both JSON files to render them into the Word template. | `LessonPlan.docx` (EN) `LessonPlan-zh.docx` (ZH) |

### Run Command (Step 4, executed by the agent)

```bash
PYTHONIOENCODING=utf-8 python Injection.py LessonPlan.json
PYTHONIOENCODING=utf-8 python Injection.py LessonPlan-zh.json
```

> **Note:** The `PYTHONIOENCODING=utf-8` prefix prevents Unicode display errors on Windows terminals. The `.docx` files are still generated correctly even without it, but the prefix keeps the console output clean.

---

## Mode 2: Revision Mode (Revise an Existing Lesson Plan)

### When to Use

Use this when you have already generated a lesson plan and want to apply revisions — such as changes annotated on existing files or new direction in supplementary documents.

### How to Trigger

Include the keyword **"Revise"** or **"修改"** (case-insensitive) anywhere in your prompt to the agent.

> Example: "Revise the lesson plan based on the feedback in ExtraDocs."

### Preparing Your Revision Input

You can supply revision instructions in one or both of the following ways:

**Method A — Annotated copies of existing files:**
Save a modified copy of any previously generated file (e.g., `DraftPlan-revision.md`, `LessonPlan-revision.json`) with your changes or comments embedded. The `-revision` suffix tells the agent to load these as revision references.

**Method B — A standalone reference document:**
Place a dedicated revision instruction file in the current directory (the agent identifies it by its filename intent). For example: `ExtraDocs/RevisionNeedsForSpecialAssign.md`.

### What the Agent Does (Step by Step)

| Step | Action | Output File |
|------|--------|-------------|
| **0** | Scans the working directory for all `*-revision.*` files and any standalone reference documents. Compares them against the originals and produces a detailed diff report, including the intent behind each change. | `RevisionDifference.md` |
| **1** | Uses `RevisionDifference.md` as the guiding document for all subsequent steps. All outputs use a **`-revised`** suffix to avoid overwriting originals. Only minimum necessary changes are made; unrelated content is preserved verbatim. | *(guides all further steps)* |
| **2** | Re-generates `SCSA Connection.md` aligned with any revised teaching direction. | `SCSA Connection.md` |
| **3** | Re-generates both the English and Chinese draft lesson plans, applying only the changes specified. | `DraftPlan-revised.md` (EN) `DraftPlan-zh-revised.md` (ZH) |
| **4** | Re-extracts revised JSON files. | `LessonPlan-revised.json` (EN) `LessonPlan-zh-revised.json` (ZH) |
| **5** | Runs `Injection.py` on both revised JSON files. | `LessonPlan-revised.docx` (EN) `LessonPlan-zh-revised.docx` (ZH) |
| **6** | Prints a summary of every change made (grouped by semantic meaning, not file count). | *(console output)* |
| **7** | Abstracts meaningful changes into observations and appends them to `EditingRules/07_Feedbacks_and_Observations.md` with the `[Personal Observation]` tag. | `EditingRules/07_Feedbacks_and_Observations.md` |

> **Important:** The agent never directly edits `.docx` files. All changes go through the JSON → `Injection.py` → `.docx` pipeline.

---

## Output Files Summary

### Default Mode Outputs

| File | Language | Description |
|------|----------|-------------|
| `SCSA Connection.md` | English | Curriculum alignment document |
| `DraftPlan.md` | English | Full lesson plan (narrative + key-value mapping) |
| `DraftPlan-zh.md` | Chinese | Faithful Chinese translation of `DraftPlan.md` |
| `LessonPlan.json` | English | Structured JSON (keys `x01`–`x61`) |
| `LessonPlan-zh.json` | Chinese | Chinese version (same keys, translated content) |
| `LessonPlan.docx` | English | Final Word document |
| `LessonPlan-zh.docx` | Chinese | Final Chinese Word document |

### Revision Mode Outputs

All the same files, plus the diff report, with `-revised` appended to intermediate and final filenames:

| File | Description |
|------|-------------|
| `RevisionDifference.md` | Detailed diff report of all changes and their intent |
| `DraftPlan-revised.md` / `DraftPlan-zh-revised.md` | Revised drafts |
| `LessonPlan-revised.json` / `LessonPlan-zh-revised.json` | Revised JSON |
| `LessonPlan-revised.docx` / `LessonPlan-zh-revised.docx` | Final revised Word documents |

---

## JSON Structure (Quick Reference)

The lesson plan data is encoded in keys `x01` to `x61`, organized into logical sections:

| Keys | Section |
|------|---------|
| `x01`–`x07` | Lesson overview (subject, date, year level, time, etc.) |
| `x08`–`x09` | Learning outcomes and specific goals |
| `x10`–`x18` | Assessment matrix (Diagnostic / Formative / Summative) |
| `x19`–`x20` | Monitoring plan (What to watch / How to watch) |
| `x21` | Students' prior knowledge |
| `x22` | Preparation and resources list |
| `x23`–`x31` | Introduction (up to 3 parts × 3 keys each) |
| `x32`–`x52` | Body / Main teaching sequence (up to 7 parts) |
| `x53`–`x61` | Conclusion (up to 3 parts) |

Each teaching phase part uses a triplet of keys: **time → strategy/actions → focus questions or notes**.

For full key definitions, see `GeneratingRules/KeyDefinitions.md`. For formatting syntax (bullet lists, rich-text color tags, mixed text+list syntax), see `GeneratingRules/Schema.md` and `EditingRules/05_Length_Constraints.md`.

---

## Pedagogical Framework

The lesson plans generated by this system are grounded in:

- **Backward Design (UbD)** — outcomes first, then assessment, then activities
- **Gradual Release of Responsibility** — I do → We do → You do
- **5E Model** (Engage, Explore, Explain, Elaborate, Evaluate) as the default instructional framework
- **PRIMM Model** for coding and algorithm lessons
- **Bloom's Taxonomy** for writing measurable learning objectives (WALT / WILF)
- **Lorna Earl's Assessment Model** — Assessment *of*, *for*, and *as* learning
- **SCSA Achievement Standards** for Western Australia Digital Technologies (Year 7–10)
- **Madeline Hunter's model** for lesson sequencing (Anticipatory Set → Objective → Instruction → Guided Practice → Independent Practice → Closure)

---

## Known Issues & Notes

All past debugging notes are recorded in `References/Debug.md`. Key points:

- **Missing keys `x62`–`x91`:** The Word template contains 91 placeholders but only `x01`–`x61` are defined. The warning `"缺失警告: JSON 中未找到以下 30 个占位符数据"` is expected and harmless — those slots are auto-filled as blank.
- **Windows Unicode error:** If `Injection.py` exits with `UnicodeEncodeError`, the `.docx` file is still generated correctly. Use `PYTHONIOENCODING=utf-8 python Injection.py <file>` to suppress the error.
- **Embedded quotes in Chinese JSON:** Use `「...」` angle quotes instead of ASCII `"..."` inside Chinese string values to avoid JSON parse errors.

---

## Quick Start

1. Write your teaching idea into `Insights/Insights.md`.
2. Tell the AI agent: **"Follow WorkFlow.txt and generate a lesson plan."**
3. Wait for the agent to complete all four steps.
4. Collect `LessonPlan.docx` and `LessonPlan-zh.docx` from the project root.

To revise an existing plan:

1. Annotate your changes on a copy of any generated file, saving it with a `-revision` suffix (e.g., `DraftPlan-revision.md`), or place a revision guide in `ExtraDocs/`.
2. Tell the agent: **"Revise the lesson plan."**
3. Collect `LessonPlan-revised.docx` and `LessonPlan-zh-revised.docx`.
