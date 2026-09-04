# Agent 智能调度规则

## 自动判断，用户不指定

用户只描述任务，由 Hermes 自动选择最合适的执行者。

## 路由表

| 任务类型 | 执行者 | 命令 |
|---------|--------|------|
| 财税方案/审计报告/合规建议 | Hermes（主战） | 本进程 |
| 代码开发/重构/调试 | Claude Code | `claude -p "..."` |
| 批量数据处理/Excel分析 | Codex CLI | `codex exec "..."` |
| 长文档精读/中文分析 | Kimi子Agent | `delegate_task` |
| 银行流水/扫描件OCR | Hermes（ocr-and-documents） | 本进程 |
| 图片/PDF识别 | Hermes（vision_analyze） | 本进程 |
| 并行多任务 | 拆分到多Agent | 并行delegate |

## 特殊规则

- Codex 熟练 财税报告（合利盛实战验证），数据处理优先派它
- Codex 禁止处理图片任务（会卡死）
- 紧急/并行场景 → 财税任务 Hermes+Codex 一起上
