# 调试记录与修复报告 (Debug Log)

### 1

* **问题描述**：
    在解析中文版 JSON 时，解析器在第 36 行报错 `Expecting ',' delimiter`。
* **原因分析**：
    中文文本内部直接嵌套使用了 ASCII 半角双引号 `"`（例如 `"分解"一词`）。在 JSON 语法中，双引号被识别为字符串的终止符，导致解析器认为字符串已结束，从而引发后续格式损坏。此问题在文档中的游戏名称、Scratch 菜单引用及对话引用等处共出现了 11 处。
* **修复方案**：
    将所有嵌套在字符串内部的 ASCII 双引号替换为中文角引号 `「...」`。这些字符属于合法的 Unicode 字符，不会被 JSON 解析器识别为功能性定界符。替换后，JSON 文件解析成功。

---

### 2
* **问题描述**：
    脚本在 Windows 环境下运行时，控制台触发 `UnicodeEncodeError`。
* **原因分析**：
    Python 的 `print_report` 函数中包含了一些 Unicode 符号（如 `▶` 和 `✅`）。由于 Windows 系统的默认终端（CMD/PowerShell）通常使用 GBK 编码，无法正确处理这些特殊字符。
* **修复建议**：
    该错误发生在文件成功写入磁盘之后，因此并不影响 `.docx` 文档的最终生成结果。为了优化控制台体验，可以通过在运行前设置环境变量 `PYTHONIOENCODING=utf-8` 来解决编码兼容性问题。

---

### 3
* **问题描述**：
    在本次修改模式（Revision Mode）运行中，对 `LessonPlan-revised.json` 首次调用 `python Injection.py LessonPlan-revised.json` 时，控制台报出 `UnicodeEncodeError`（exit code 1），似乎执行失败。
* **原因分析**：
    与 Debug #2 完全一致——GBK 终端无法显示 `print_report` 中的 Unicode 符号（`▶`、`✅`）。该错误发生于文件保存完成之后，`.docx` 文件已正常写入磁盘（通过 `ls` 命令确认 `LessonPlan-revised.docx` 存在）。
* **解决方案**：
    后续对两个文件的调用均改用 `PYTHONIOENCODING=utf-8 python Injection.py <文件名>` 命令，两次执行均成功输出「总体状态 : 成功 ✅」。`LessonPlan-revised.docx` 和 `LessonPlan-zh-revised.docx` 均已正常生成。今后所有 Injection.py 调用统一使用此前缀。

---

### 4
* **问题描述**：
    本次默认模式（Default Mode）运行中，`Injection.py` 对 `LessonPlan.json` 和 `LessonPlan-zh.json` 的两次调用，均在运行报告中出现警告：「缺失警告: JSON 中未找到以下 30 个占位符数据，已自动填为空白: x62, x63, x64 ... x91」。
* **原因分析**：
    `Template.docx` 模板文件中包含从 `x01` 至 `x91` 共 91 个占位符，而 `GeneratingRules/KeyDefinitions.md` 中仅对 `x01`—`x61` 共 61 个键名有明确定义，`Schema.md` 虽提及 x91 但未提供 x62—x91 的语义定义。当前生成的 JSON 文件完整覆盖了已定义的 x01—x61，x62—x91 的空缺由渲染引擎自动填为空白，不影响文档的最终生成和核心内容呈现。
* **备注**：
    两次调用均以「总体状态 : 成功 ✅」结束，`LessonPlan.docx` 和 `LessonPlan-zh.docx` 均已正常写入磁盘。此警告为已知的结构性信息差异（模板比规范文件包含更多占位符），不视为错误。如未来需使用 x62—x91，应优先更新 `KeyDefinitions.md` 以明确其语义定义。

---

### 5
* **问题描述**：
    本次默认模式（Default Mode）运行中（教案主题：Lesson 1 of 8 — Game Deconstruction & Scratch Environment Setup），`Injection.py` 对 `LessonPlan.json` 和 `LessonPlan-zh.json` 的两次调用，均在运行报告中再次出现警告：「缺失警告: JSON 中未找到以下 30 个占位符数据，已自动填为空白: x62, x63, x64 ... x91」。
* **原因分析**：
    与 Debug #4 完全一致——`Template.docx` 中含 91 个占位符 (x01—x91)，而本次生成的 JSON 仅严格按照 `KeyDefinitions.md` 中已定义的 x01—x61 进行了完整填充，x62—x91 在规范文件中暂无语义定义，因此输出的 JSON 中没有这些键，渲染引擎自动将其填为空白。
* **备注**：
    两次调用均以「总体状态 : 成功 ✅」结束，`LessonPlan.docx` 和 `LessonPlan-zh.docx` 均已正常写入磁盘（59143 字节与 60377 字节）。此警告为预期内的结构性信息差异，不视为错误，文档最终内容呈现完整。本次执行从一开始即采用 `PYTHONIOENCODING=utf-8 python Injection.py <文件名>` 命令以预防 Debug #2 与 #3 中描述的 GBK 编码报错，两次调用过程中均未出现 `UnicodeEncodeError`，控制台输出干净。

---

### 6
* **问题描述**：
    本次默认模式（Default Mode）运行中（教案主题：Lesson 1 of 8 — Game Deconstruction & Scratch Environment Setup，Year 8），`Injection.py` 对 `LessonPlan.json` 与 `LessonPlan-zh.json` 的两次调用，均在运行报告中再次出现警告：「缺失警告: JSON 中未找到以下 30 个占位符数据，已自动填为空白: x62, x63, x64 ... x91」。
* **原因分析**：
    与 Debug #4 与 #5 完全一致——`Template.docx` 中含 91 个占位符 (x01—x91)，而本次生成的 JSON 严格按照 `KeyDefinitions.md` 中已定义的 x01—x61 进行了完整填充（已在生成前用 Python 校验过 `len(set(x-keys)) == 61`），x62—x91 在规范文件中暂无语义定义，因此输出的 JSON 中没有这些键，渲染引擎自动将其填为空白。
* **备注**：
    两次调用均以「总体状态 : 成功 ✅」结束，`LessonPlan.docx` 和 `LessonPlan-zh.docx` 均已正常写入磁盘（58943 字节与 60188 字节）。此警告为预期内的结构性信息差异，不视为错误，文档最终内容呈现完整。本次执行从一开始即采用 `PYTHONIOENCODING=utf-8 python Injection.py <文件名>` 命令以预防 Debug #2 与 #3 中描述的 GBK 编码报错，两次调用过程中均未出现 `UnicodeEncodeError`，控制台输出干净。

---

### 7
* **问题描述**：
    本次默认模式（Default Mode）运行中（教案主题：Lesson 1 of 8 — Game Deconstruction & Scratch Environment Setup，Year 8，日期 29/04/2026），`Injection.py` 对 `LessonPlan.json` 与 `LessonPlan-zh.json` 的两次调用，再次出现警告：「缺失警告: JSON 中未找到以下 30 个占位符数据，已自动填为空白: x62, x63, x64 ... x91」。
* **原因分析**：
    与 Debug #4、#5、#6 完全一致——`Template.docx` 中含 91 个占位符 (x01—x91)，而 `KeyDefinitions.md` 仅对 x01—x61 提供了语义定义，因此本次生成的 JSON 严格在 61 键上完整填充（已用 Python 校验 `len(keys)==61` 且无缺漏无溢出）。x62—x91 在规范文件中无语义，生成端选择不输出这些键，由 `Injection.py` 自动填为空字符串。
* **备注**：
    两次调用均以「总体状态 : 成功 ✅」结束。`LessonPlan.docx` 与 `LessonPlan-zh.docx` 均已正常写入磁盘，分别为 59504 字节与 60879 字节。本次执行全程使用 `PYTHONIOENCODING=utf-8 python Injection.py <文件名>` 命令以预防 Debug #2 与 #3 的 GBK 编码报错，两次调用过程中控制台输出干净，无 `UnicodeEncodeError`。此警告为已知的结构性信息差异，不视为错误。