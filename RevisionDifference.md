# 修订差异报告 (Revision Difference Report)
## 修订模式 — 教案第1课（共8课）

**生成日期：** 30/04/2026
**参考来源：** ExtraDocs/RevisionNeedsForSpecialAssign.md（已被用户明确指定为本次修订的核心参考意见文件）
**扫描结果：** 在整个工作目录及子目录中未发现任何以 "-revision" 结尾的文件，因此本报告以 ExtraDocs 文件夹内的 RevisionNeedsForSpecialAssign.md 作为用户意图的唯一权威来源，与现有教案文件（DraftPlan.md、LessonPlan.json、LessonPlan-zh.json 等）进行对比分析。

---

## 按文件分组的差异分析

---

### 文件组 A：LessonPlan.json / LessonPlan-zh.json（影响最大的结构性文件）

---

#### 差异 A-1：课程总时长不符合要求

**现有内容：**
- `x06 = "Period 1 - 8:30 to 9:20"`（50分钟）
- 教学序列各部分之和：5+5+5+10+7+8+5+5 = 50分钟

**要求内容（RevisionNeedsForSpecialAssign.md 模块 2.1）：**
> "课程总时长：您的教案必须是一堂不多不少刚好 **60 分钟**的课。"

**差异描述：** 现有教案总时长为50分钟，比要求少10分钟，且时间段标注（8:30至9:20）明确体现了50分钟时长。需要将课时调整为60分钟，并更新 x06 字段为 "Period 1 - 8:30 to 9:30"，同时对各教学环节的时间分配进行相应调整。

**用户意图分析：** 这是大学作业的硬性格式要求（共计1.5分权重来自时间约束），所有教案必须设计为60分钟课时。原有的50分钟设计源自 Insights.md 中的规划（"每节课假设为50分钟"），但 ExtraDocs 作为大学作业提交规范，其要求凌驾于内部规划之上。需增加约10分钟，建议分配到以下环节：Input环节延长（5→8分钟）、新增 Checking for Understanding 独立环节（5分钟），其余部分相应微调。

**对课程设计的指导：** x06 修改为60分钟时段；各环节时间重新分配以求和等于60分钟；KeyDefinitions 要求 x06 时长必须等于所有子时间字段之和。

---

#### 差异 A-2：Madeline Hunter 8步骤均未以红色明确标注

**现有内容：** 教案正文（x24-x61 各策略字段）中没有任何 Madeline Hunter 步骤标题或红色标注。8个步骤分别隐式分布于各环节中，但从未显式命名。

**要求内容（RevisionNeedsForSpecialAssign.md 模块 1.3，权重5分/15分）：**
> "您的流程中必须显式地体现出以下 8 个关键步骤，在合适的位置明确包含这八个标题，并着重明显地**使用红色！**标示出来：
> 1. 预设情境 (Anticipatory Set)
> 2. 目标和目的 (Objective and Purpose)
> 3. 信息输入 (Input)
> 4. 建模/示范 (Modeling)
> 5. 检查理解 (Checking for Understanding)
> 6. 指导练习 (Guided Practice)
> 7. 独立练习 (Independent Practice)
> 8. 总结 (Closure)"

**差异描述（详细，每步分析）：**

| MH步骤 | 现有对应内容 | 是否明确标注（红色）？ | 问题 |
|---|---|---|---|
| Anticipatory Set | 导入Part 2：演示游戏 + 分解问题 | ❌ 无标注 | 仅内容对应，无标签；且位于WALT/WILF之后（顺序倒置） |
| Objective and Purpose | 导入Part 1：WALT/WILF幻灯片 | ❌ 无标注 | 仅内容对应，无标签；且位于钩子之前（顺序倒置） |
| Input | 主体Part 1：Scratch界面介绍 | ❌ 无标注 | 仅内容对应，无标签 |
| Modeling | 主体Part 2中的"I do"部分 | ❌ 无标注，且与Guided Practice混合 | Modeling与Guided Practice融合，无法分辨 |
| Checking for Understanding | 无独立环节；分散于巡视描述中 | ❌ 无此环节 | **缺失独立步骤**，这是最大的结构性缺口 |
| Guided Practice | 主体Part 2的"We do"部分 + Part 3 | ❌ 无标注 | 仅内容对应，无标签 |
| Independent Practice | 主体Part 4：备用工作纸 | ❌ 无标注 | 仅内容对应，无标签 |
| Closure | 总结Part 2：词汇复述 | ❌ 无标注 | 仅内容对应，无标签 |

**用户意图分析：** Madeline Hunter模型占该教案评分的33%（5/15分），是得分权重最高的单项。现有设计在内容上实质已符合Hunter模型的精神，但完全缺乏显式标注。修订的核心工作是：在对应策略字段（x25/x27/x33/x36/x39/x42/x45/x57）的开头加入 `<r><b>Madeline Hunter Step — [步骤名]</b></r>` 红色标签，以满足"明确包含且使用红色标示"的要求。

**对课程设计的指导：** 每个 MH 步骤必须在对应的 JSON 策略字段开头添加红色标注；同时需解决步骤顺序问题（见差异 A-3）和 Checking for Understanding 缺失问题（见差异 A-4）。

---

#### 差异 A-3：Anticipatory Set 与 Objective and Purpose 顺序倒置

**现有内容：**
- 导入Part 1（5分钟）：点名 + WALT/WILF（= Objective and Purpose）
- 导入Part 2（5分钟）：演示游戏 + 分解问题（= Anticipatory Set）

**要求内容（RevisionNeedsForSpecialAssign.md 模块 1.3）：**
> "1. 预设情境 (Anticipatory Set)：在正式上课**前**，设计一个简短的活动或提示，将学生过去的经验与今天的内容联系起来，以激发兴趣并集中注意力。
> 2. 目标和目的 (Objective and Purpose)：明确**告诉**学生他们将要学什么、为什么需要学..."

**差异描述：** MH模型明确规定 Anticipatory Set（钩子/情境引入）必须发生在正式教学目标宣布之前。现有教案将 WALT/WILF（目标宣告）置于演示游戏钩子活动之前，顺序与MH标准相反。

**用户意图分析：** 正确的MH顺序要求先用钩子勾住学生的注意力，再告诉他们今天的学习目标。这样做的教学逻辑是：让学生先对内容产生好奇心（通过看演示游戏），然后再告诉他们"今天我们要做这个"，学习动机更强。需将两个导入部分的内容对调：Part 1变为演示游戏钩子（Anticipatory Set），Part 2变为点名+WALT/WILF（Objective and Purpose）。

**对课程设计的指导：** 导入Part 1的x24/x25内容替换为Anticipatory Set（演示游戏、分解问题、白板记录）；导入Part 2的x27内容替换为Objective and Purpose（点名+WALT/WILF展示），其中也需添加建构主义理论提及。

---

#### 差异 A-4：缺少独立的 Checking for Understanding 环节

**现有内容：** 无独立的 Checking for Understanding 步骤。理解检查分散嵌入于巡视说明中（"Pause and visually confirm..."），不构成独立教学阶段。

**要求内容（RevisionNeedsForSpecialAssign.md 模块 1.3）：**
> "5. 检查理解 (Checking for Understanding)：在练习前，教师通过提问等策略确认学生是否已经掌握所讲内容，以此决定是继续推进还是重新讲解。"

**差异描述：** MH模型要求在Modeling之后、Guided Practice之前，设置一个独立的"检查理解"阶段，通过提问等方式确认学生已理解示范内容。现有教案跳过了这一独立阶段，直接从示范进入练习。

**用户意图分析：** 这一缺失是最需要新增内容的地方。Checking for Understanding的作用是"决策门控"——如果学生还没明白，就不该开始练习，否则会强化错误。需在Modeling之后（主体Part 3位置）新增一个5分钟的CfU环节，内容为：教师向小组提问3个关于界面和操作步骤的问题，扫视确认理解程度，如有必要重新演示。

**对课程设计的指导：** 主体Part 3（x38/x39/x40）由原来的 "Icebreaker Coding: Event Trigger" 改为独立的 Checking for Understanding 环节；原来的绿旗积木操作并入主体Part 4（Guided Practice）中，作为第4个guided practice步骤。

---

#### 差异 A-5：缺少建构主义理论明确表述

**现有内容：** 教案中无任何关于教学理论基础的明确表述。

**要求内容（RevisionNeedsForSpecialAssign.md 模块 1.1）：**
> "理论支撑：您的教案设计必须建立在建构主义（侧重以学生为中心、探究式学习）理论基础之上。"

**差异描述：** 尽管现有教案的设计实质上体现了建构主义精神（学生通过观察和操作主动建构理解），但教案文本中完全没有明确点明"建构主义"作为理论基础。

**用户意图分析：** 评分标准模块1.1要求理论支撑可见。只需在Objective and Purpose环节（x27）中加入一句话，说明本课建立在建构主义理论基础之上即可。无需大篇幅展开，一句简洁说明即满足要求。

**对课程设计的指导：** 在修订后的x27（Objective and Purpose部分）中添加："This lesson is grounded in constructivist theory: students actively construct understanding by observing a complex system, identifying its components, and building upon prior experience."

---

### 文件组 B：DraftPlan.md / DraftPlan-zh.md

这些文件是JSON的前置叙述性版本，需同步更新以反映上述所有JSON层面的改动。具体差异与A组完全一致（时长、MH标注、顺序、CfU缺失、建构主义），在DraftPlan层面体现为叙述文字和表格内容的对应更新。不作单独逐条展开，以DraftPlan-revised.md体现最终修订后叙述形式。

---

### 文件组 C：SCSA Connection.md

**差异程度：极小。** SCSA课程对接文档的核心内容（课标代码、对应分析、逻辑推理）与本次修订需求无实质冲突，不需要修改SCSA代码对应关系。仅需将文档开头对时间的引用从"50分钟"更新为"60分钟"。其余内容保持不变。

**用户意图分析：** SCSA对接的修订无实质教学意图驱动，仅为文件一致性的形式更新。

---

## 改动优先级总表

| 差异编号 | 差异内容 | 改动文件 | 改动类型 | 优先级 |
|---|---|---|---|---|
| A-1 | 课时50→60分钟，时间字段更新 | JSON / DraftPlan | 时间调整 | 🔴 最高 |
| A-2 | 8个MH步骤加红色标签 | JSON / DraftPlan | 标注添加 | 🔴 最高 |
| A-3 | Anticipatory Set与WALT/WILF顺序对调 | JSON / DraftPlan | 结构调整 | 🔴 高 |
| A-4 | 新增Checking for Understanding独立环节 | JSON / DraftPlan | 内容新增 | 🔴 高 |
| A-5 | 添加建构主义理论表述 | JSON / DraftPlan | 内容添加 | 🟡 中 |
| B | DraftPlan同步更新 | DraftPlan.md / DraftPlan-zh.md | 内容同步 | 🟡 中 |
| C | SCSA Connection时间引用更新 | SCSA Connection.md | 形式更新 | 🟢 低 |

---

## 修订方案对比（修订前 vs 修订后教学序列）

| 位置 | 修订前（50分钟） | 修订后（60分钟） |
|---|---|---|
| 导入Part 1（x23） | 5分 — 点名 + WALT/WILF | **5分 — Anticipatory Set**（演示游戏 + 分解问题） |
| 导入Part 2（x26） | 5分 — 演示游戏 + 分解问题 | **5分 — Objective and Purpose**（点名 + WALT/WILF + 建构主义） |
| 主体Part 1（x32） | 5分 — Interface Input | **8分 — Input**（延长，更充分的界面讲解） |
| 主体Part 2（x35） | 10分 — Guided Practice (I do/We do合并) | **8分 — Modeling**（教师完整演示全部4步，学生仅观察） |
| 主体Part 3（x38） | 7分 — Icebreaker Coding（绿旗积木，仍属Guided Practice） | **5分 — Checking for Understanding**（新增，组合提问确认理解） |
| 主体Part 4（x41） | 8分 — Independent Practice（工作纸） | **12分 — Guided Practice**（学生复现全部4步，含绿旗积木） |
| 主体Part 5（x44） | （空） | **7分 — Independent Practice**（工作纸 + 独立探索） |
| 总结Part 1（x53） | 5分 — 命名/保存 | **5分 — 命名/保存**（不变） |
| 总结Part 2（x56） | 5分 — 词汇复述 Closure | **5分 — Closure**（内容不变，添加MH标签） |
| **总计** | **50分钟** | **60分钟 ✓** |

---

*本报告由修改模式步骤0自动生成，将作为后续所有步骤（步骤1-7）的修订导航依据。*
