# 书籍→Skill 加工流程（Hermes版）

## 何时触发
用户给了一本电子书（EPUB/PDF/DOCX/MOBI），要求做成可复用的skill。

## 优先级规则
1. **先查现有skill是否已覆盖该领域** — 有则做Update/Fold-in，不新建
2. **新建时命名规则**：`{author-lastname}-{core-concept}`（如 carnegie-influence, cialdini-influence）
3. 产出物：SKILL.md + chapters/ + glossary.md + cheatsheet.md + 知识库人读版

## 踩坑记录

### 子Agent只生成了SKILL.md，chapters/目录为空
2026-06-28 实战：delegate_task 派子Agent做全量蒸馏，回来后只有SKILL.md有内容，chapters/空，glossary/patterns/cheatsheet缺失。
**对策**：验收时检查 `ls skills/<name>/chapters/` 是否非空。为空时手动补全——从已有SKILL.md的章节索引反推章节结构，逐章生成。

### 双语EPUB提取后章节标记重复
epub包含中英文两个版本时，extract.py输出的纯文本会有两套章节标记（中文"01"和英文"Chapter 1"），grep找章节偏移量会翻倍。
**对策**：提取后先看metadata.json确认是否有重复章节。用Python去重：保留第一套完整标记，删除第二套重复。

### 谈单转化是用户刚需
每章Key Takeaways中必须有一条"谈单转化"（how to use in sales context），这是与通用book-to-skill的核心差异。
