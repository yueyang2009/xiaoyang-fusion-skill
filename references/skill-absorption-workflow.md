# Skill 吸收融合工作流

> 当用户说「吸收融合/吸收进我的技能包/加进 xiaoyang-fusion」时执行
> 目标：把新 skill 的核心价值融入 xiaoyang-fusion，原 skill 独立保留

---

## 标准流程（三件套）

### 第一步：道框架归位

把新 skill 的哲学本质归入十脉对应的「道」：

| 类目 | 归入哪一脉 | 示例 |
|:----|:----------|:-----|
| 税法/制度分析 | 法学·制度脉（韩非子） | muyouzhi-perspective |
| 个人成长/能量/心态 | 存在主义·责任脉（彼得森·冯唐） | yangmou-open-source |
| 管理/经营/组织 | 宁向东脉 | 财务BP |
| 法律/公司治理 | 法学·制度脉 | 公司法评注 |
| 股权/资本 | 法学·制度脉 | 股权节税 |
| 习惯/效率/系统 | 笑来脉 | 原子习惯 |

### 第二步：Agent调度表注册

在 `SKILL.md` 的 Agent智能调度表格中加一行：

```
| **技能名（一句话说明）** | → **<skill-name>** skill（独立进化，保留完整） |
```

格式统一：
- 冒号前是技能名+括号说明（一句话点明用途）
- 冒号后是 → **skill名称** skill（独立进化，保留完整）

### 第三步：工具箱提炼

在「慕有枝融合工具箱」之后追加新工具箱区块，格式：

```
### 技能名工具箱（来自 <skill-name>）

**核心框架（2-5条）：**
1. ...
2. ...

**金句素材（3-5条，客户沟通直接用的）：**
- ...
- ...

遇到以下场景 → **手动加载 <skill-name>**：
- ...
- ...
```

### 第四步（可选）：更新十脉道框架表

如果该 skill 代表了新的哲学维度，在「以道驭术」的十脉表中追加或合并。

### 第五步：推送 GitHub

```bash
cd ~/hermes-skills-sync
rm -rf "./hermes/<skill-name>"
cp -r "$HOME/AppData/Local/hermes/skills/<skill-name>" "./hermes/<skill-name>"
# xiaoyang-fusion 更新
rm -rf "./hermes/xiaoyang-fusion"
cp -r "$HOME/AppData/Local/hermes/skills/productivity/xiaoyang-fusion" "./hermes/xiaoyang-fusion"
git add -A && git commit -m "sync mm-dd [Hermes] 新增<skill-name>; 更新xiaoyang-fusion" && git push
```

---

## 原则

1. **原 skill 独立保留** — 不删除、不覆盖、不解体。后续只需补充新增内容
2. **只提炼最核心的** — 工具箱不要超过5条框架+5条金句，多了记不住
3. **金句要能直接用在客户沟通中** — 不是学术总结，是谈单话术
4. **触发条件明确** — 什么时候该手动加载该skill，说清楚
