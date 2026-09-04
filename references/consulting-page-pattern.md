# 咨询公司页面写作模式（故事驱动型 → 成交系统）

适用场景：龙头会服官网中需要"说服老板"的独立页面，如《为什么企业需要年度财税顾问》。
核心原则：不卖产品、不堆术语、用故事带认知、用筛选建信任。

---

## 核心写作法则

| 原则 | 不要 | 要 |
|------|-----|----|
| 故事化 | "很多企业存在财税管理薄弱的问题" | "企业从几百万做到几千万，老板一个人撑起全局。但到了某个阶段，事情不一样了。" |
| 不说"我们" | "我们提供年度财税顾问服务" | "年度顾问帮你建立经营口径的利润表" |
| 不做营销 | "限时优惠""立即购买" | 语气：判断、理解、选择 |
| 不堆术语 | "建立业财税一体化管理体系" | "让老板每月看到自己企业真实的盈利状况" |
| 先破后立 | "你需要长期财税顾问" | "很多老板的第一反应是：再招个好会计就行了。但问题不在会计身上。" |
| 强筛选 | 来者不拒 | 明确告知适合/不适合，劝退不合适的客户 |
| CTA克制 | "免费咨询""立即预约" | "申请企业经营尽调（限量开放）" + 稀缺性辅助说明 |

## 11屏说服型成交页架构（已验证）

| # | 模块 | 标题 | 关键写法 |
|---|------|------|---------|
| ① | Hero | 不是所有企业都需要财税顾问，但你的企业可能正处在需要的时候 | 建立选择压力，不推销 |
| ② | 痛点 | 为什么很多企业越做越累？ | 逻辑链：规模增长→财务没升级→看不清利润→决策靠经验 |
| ③ | 产品定义 | 什么是企业年度财税顾问？ | 双卡设计：左边"不是"(浅色) → 右边"而是"(深色) |
| ④ | 核心交付 | 一年下来，你会得到什么？ | 6项结果型交付，禁止"可能/建议/提供咨询"等模糊词。必须写：尽调报告、风险清单、经营分析、复盘报告。 |
| ⑤ | 服务流程 | 我们如何陪伴企业一年？ | 4步：尽调→计划→陪跑→复盘 |
| ⑥ | 如果不做 | 如果不做年度财税顾问，企业会发生什么？ | 4条后果 + 结论"问题不是突然出现的" |
| ⑦ | 筛选 | 我们如何判断是否适合服务？ | 双卡：适合4条(强调) / 不适合3条(抑制) |
| ⑧ | 合作流程 | 申请企业经营尽调后会发生什么？ | 5步：申请→沟通→尽调→适配→决定 |
| ⑨ | FAQ | 你可能关心的问题 | 6个：适合性/时长/收费/见面频率/税务处理/开始方式 |
| ⑩ | 对比表 | 年度财税顾问 vs 传统代账服务 | 5个维度 + 结论"两者解决的是完全不同层级的问题" |
| ⑪ | CTA | 申请企业经营尽调（限量开放） | 辅助说明三行：每月仅服务有限企业 / 需初步评估适配性 / 不适合所有企业 |

## 全站CTA规范

所有页面统一改为：

```
主按钮：申请企业经营尽调（限量开放）
辅助说明（三行）：
- 每月仅服务有限企业
- 需初步评估适配性
- 不适合所有企业
```

**更新范围**：首页Hero/服务区/联系区、决策页、联系页、404页、Header按钮、LeadForm、CTASection等所有组件。

## 页面类型模板

### About 页（咨询公司风格）
5板块：为什么存在（起源故事）→ 我们相信什么（信念陈述）→ 我们不做什么（4条边界）→ 我们是谁（团队简介）→ 最终信任声明（"我们不承诺做不到的事，但我们承诺合作期间尽心尽力"）

### 首页
Hero → 痛点4卡 → 方法4步 → 年度顾问（适合/包含/流程）→ 团队（数据+4人）→ 案例2个 → 最终决策模块（"如果你正在考虑"）→ 联系

### /assessment 尽调页
Hero（标题+说明）→ 5步流程（申请→沟通→尽调→适配→决定）→ 适合/不适合双卡 → CTA

## 风格参数（Tailwind）

```css
/* 配色 */
brand-ink:   #111111  /* 标题 */
brand-muted: #6B7280  /* 辅助文字 */
brand-line:  #E5E7EB  /* 分割线 */
brand-soft:  #F9FAFB  /* 浅灰背景 */

/* 排版 */
标题:    text-3xl/tight md:text-4xl/tight → text-4xl/tight md:text-5xl/tight
正文:    text-base/8 text-brand-muted
引文:    border-l-4 border-brand-ink bg-brand-soft px-6 py-5 text-lg font-medium
标签:    text-xs font-semibold uppercase tracking-[0.12em] text-brand-muted

/* 留白 */
每屏内边距:     py-24 md:py-28
Hero首屏:       py-24 md:py-36
内容区宽度:     max-w-3xl
区隔:           border-b border-brand-line
背景交替:       白色 → bg-brand-soft → 白色 → 循环
```

## 内联组件定义

每个咨询风格页面定义一套内联组件，不引入外部依赖：

```
Label({text})          — 标签（12px, 全大写, 追踪宽, 灰色）
Heading({children})    — 标题（30/36px, semibold, 紧排, ReactNode）
Body({children})       — 正文容器（mt-8, space-y-5, 16px/8, text-brand-muted）
QuoteLine({children})  — 引用线（左边框4px, 浅灰底, 18px, 加粗）
```

注意：Heading 的 children 类型用 `React.ReactNode`（而非 `string`），因为可能含 `<br />` 等 JSX。

## 胶片颗粒效果（头像用）

```css
.grain { position: relative; overflow: hidden; }
.grain::after {
  content: "";
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.7' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size: 256px 256px;
  opacity: 0.10;
  mix-blend-mode: multiply;
  pointer-events: none;
}
```

可调参数：opacity（密度）、baseFrequency（颗粒粗细）。

---

## 参考页面

- 决策页：`/why-annual-advisor` → https://yueyang2009.github.io/longtou-accounting-service-site/why-annual-advisor/
- 首页：`/` → https://yueyang2009.github.io/longtou-accounting-service-site/
- About：`/about` → https://yueyang2009.github.io/longtou-accounting-service-site/about/
- 尽调：`/assessment` → https://yueyang2009.github.io/longtou-accounting-service-site/assessment/
