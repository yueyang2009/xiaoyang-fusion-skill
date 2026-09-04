# 电子书→Skill 蒸馏工作流

## 流水线（已验证6轮）

```
用户扔PDF/EPUB → book-to-skill CLI提取全文 → 
    子Agent通读全文提取心智模型 → 
    输出分层结构(SKILL.md + chapters/ + glossary/ + patterns/ + cheatsheet) → 
    注册进xiaoyang-fusion Agent调度表 → 
    提炼工具箱(金句+框架+触发条件) → 
    推送到GitHub备份
```

## 已验证成功的书籍

| 书名 | 格式 | 规模 | 产出 |
|------|------|------|------|
| 原子习惯 | EPUB | 427KB | 12文件/841行 |
| 公司法评注(李建伟) | PDF | 1037页 | 11文件 |
| 财务BP案例 | DOC(41个) | 18万字 | 9文件/952行 |
| 股权节税(李利威) | PDF | 417页 | 9文件/1047行 |

## 关键踩坑

1. **中文PDF提取** — pypdf比pdftotext更稳（Windows无pdftotext）
2. **DOC文件** — 后缀.doc但可能是docx格式，先检查ZIP头(PK开头)
3. **提取字数偏少** — "Words"计数对中文不准，看总字节数更可靠
4. **子Agent打断** — 大文件(500KB+)容易timeout，拆成两个子任务或直接手动编译

## Claude Code接口配置

当前Claude Code走DeepSeek Anthropic兼容接口：
- ANTHROPIC_BASE_URL: https://api.deepseek.com/anthropic
- ANTHROPIC_MODEL: deepseek-v4-flash
- cc-switch本地代理(8642端口)仅支持OpenAI协议，不兼容Anthropic Messages API
- DeepSeek API key需从platform.deepseek.com获取
