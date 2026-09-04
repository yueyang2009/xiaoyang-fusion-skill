# 咨询公司官网首页模式（Stripe/麦肯锡风格）

来源：2026-07-05 龙头会服官网实战。Codex 搭建 Next.js 骨架 → Hermes 接手内容改造。
⚠️ 品牌名经用户确认：**龙头会服**（不是"龙头快服"，详见踩坑记录）

---

## 8区块首页结构

```
Hero → 痛点 → 方法论 → 服务 → 团队 → 案例 → 最终决策模块 → 联系
```

最终决策模块（2026-07-05新增）：
- 标题：「如果你正在考虑，我们建议先做一次判断。」
- 说明两句：年度顾问更适合年营收2000万以上企业 / 如果还在初创阶段可能不是最优选择
- CTA：「申请企业经营尽调（限量开放）」
- 背景浅灰居中
- 位置：案例区之后、联系区之前

其他区块保持原7块结构不变。

---

## 配色方案（Stripe/咨询公司极简风）

| 用途 | 色值 | Tailwind变量 |
|------|------|-------------|
| 主要文字 | #111111 | brand-ink |
| 次要文字 | #6B7280 | brand-muted |
| 分割线/边框 | #E5E7EB | brand-line |
| 背景交替 | #F9FAFB | brand-soft |
| 强调色 | 纯黑(按钮) | bg-brand-ink |
| 字体 | Inter / PingFang SC | font-sans |

不使用金色、蓝色、渐变、花哨装饰。

---

## data.ts 数据层原则

- 所有文案集中到 `lib/data.ts` 管理
- 首页引用的数据：brand, homePainCards, longtouMethod, annualPlan, trustMetrics, experts, clientStories
- 核心产品（annualPlan）字段：title, summary, suitable[], whatYouGet[], process[]
- 组件层不写死任何中文文案

---

## 首页结构代码模式

```tsx
// 每个区块 = 一个 <section>，用 border-b brand-line 分割
// SectionTitle 组件：label（小字灰色）+ title（大字黑色）+ 居中
// CTA按钮：Link组件 + bg-brand-ink + text-white + hover:bg-black
// 交替背景：白色区块用 bg-white，交替区块用 bg-brand-soft
// 全站用一个 div 包裹，header+main+footer 都在一个文件内（首页专有）
```

---

## 设计参考：Sac个人品牌站 (sac-ai.com)

来源：2026-07-05 用户指定参考。https://sac-ai.com/

### 可借鉴的设计手法
- 人物照胶片颗粒质感（CSS SVG feTurbulence 实现）
- 极简导航
- 内容标签体系

### 核心主张
>"AI时代，个人网站就是最好的简历。"

对应龙头会服：**"财税行业，官网就是最好的信任状。"**

---

## 关键踩坑记录

### 品牌名不一致
Codex 建站时品牌名写"龙头会服"、我准备的内容写"龙头快服"，导致第一次修改方向错误。**接手另一个AI的项目时，不假设你的版本是权威版本——先问用户哪个是对的。**

### 配色大幅修改
Codex 用了深蓝+金色，用户要求改为 Stripe 黑白灰极简风。涉及 tailwind.config.ts + 所有组件中 text-brand-gold 的引用。

### 引号导致TS编译错误
中文引号在 TypeScript 字符串中与 JS 双引号冲突：
```typescript
// 错误
problem: "老板说"口袋没钱""
// 正确
problem: '老板说"口袋没钱"'
```

### 头像路径与 GitHub Pages basePath
Next.js 静态导出时图片路径要加 basePath：
1. `const siteBasePath = process.env.NEXT_PUBLIC_BASE_PATH || ""`
2. 图片 src: `` `${siteBasePath}/images/headshot.png` ``
3. deploy.yml 中设置 `NEXT_PUBLIC_BASE_PATH=/longtou-accounting-service-site`
