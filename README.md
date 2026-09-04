# xiaoyang-fusion · 小阳融合视角 Skill

李岳阳融合视角——**注册会计师 + 律师 + 毛选博弈 + 5000年人性洞察 + 稻盛经营哲学 + 苏格拉底认知检验**。

> 核心哲学：技术正确不等于政治可行，成交第一步不是专业而是信任。

## 这个 Skill 是什么

适用于财税咨询场景的思维框架技能，覆盖：

- **谈单与成交**：把方案讲成老板听得懂的话，先给结论再给步骤，不堆术语不吓客户
- **财税方案刀法**：问题反馈/风险诊断报告结构、5-7个核心风险、证据支撑、克制表述
- **融合视角**：技术正确（CPA）+ 合规底线（律师）+ 博弈策略（毛选）+ 人性洞察（5000年）+ 长期主义（稻盛）+ 认知检验（苏格拉底）
- **交付方法论**：短、准、能打、可落地、能成交、能交付

## 安装方法

### 方法一：手动复制（推荐，兼容所有 Agent）

```bash
# 1. 克隆本仓库，或直接 Download ZIP 并解压
git clone --depth 1 https://github.com/yueyang2009/xiaoyang-fusion-skill.git

# 2. 复制到 Hermes 技能目录（Windows 示例）
mkdir -p "$HOME/AppData/Local/hermes/skills/productivity/"
cp -r xiaoyang-fusion-skill "$HOME/AppData/Local/hermes/skills/productivity/xiaoyang-fusion"
```

### 方法二：Hermes CLI

```bash
hermes skills install --category productivity "https://github.com/yueyang2009/xiaoyang-fusion-skill" -y
```

> 若 CLI 提示未在 registry 注册，请使用方法一。

### 方法三：Claude Code / Codex

直接把整个目录复制到对应技能目录即可：

```bash
cp -r xiaoyang-fusion-skill ~/.claude/skills/xiaoyang-fusion   # Claude Code
```

## 目录结构

```
xiaoyang-fusion/
├── SKILL.md                 # 主技能文件（触发词与完整方法论）
├── manifest.json            # 技能元数据（v2.0.0）
├── build_simulation_doc.py  # 模拟文档生成脚本
├── agents/                  # 子 Agent 配置
└── references/              # 46个参考文档（案例、话术、方法论）
```

## 使用触发词

- 谈单 / 方案怎么写
- 财税诊断 / 风险报告
- 客户画像 / 话术
- 融合视角 / 小阳视角

## License

MIT