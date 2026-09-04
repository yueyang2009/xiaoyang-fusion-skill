# cc-switch 本地代理调试笔记

## 诊断流程
1. 检查端口: `netstat -ano | grep ":8642" | grep LISTENING`
2. 查进程ID对应的程序
3. 测试API: `curl http://127.0.0.1:8642/v1/chat/completions` (OpenAI格式)
4. 查日志: `tail -30 ~/.cc-switch/logs/cc-switch.log`
5. 查数据库provider: `~/.cc-switch/query_providers.py`

## 关键发现
- cc-switch存储API key到SQLite DB时显示为掩码(`sk-xxx...xxx`格式)
- 实际完整key需从服务商平台重新获取，DB中只有掩码
- cc-switch支持OpenAI协议(`/v1/chat/completions`)但不翻译Anthropic协议
- Claude Code需**直连**DeepSeek Anthropic接口，不走cc-switch代理

## DeepSeek Claude Code配置
```json
ANTHROPIC_BASE_URL: https://api.deepseek.com/anthropic
ANTHROPIC_MODEL: deepseek-v4-flash
```
API key需从 platform.deepseek.com 生成。

## Python路径（Windows）
- 不能用 `python3`（指向Windows Store）
- 用完整路径: `/c/Program\ Files/Python313/python.exe` 或 Git Bash自动
