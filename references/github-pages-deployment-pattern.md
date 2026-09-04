# GitHub Pages + Next.js 静态站点部署模式

适用于咨询公司/品牌展示型 Next.js 网站的 GitHub Pages 部署。

## 项目配置

### next.config.mjs

```js
const repoName = "your-repo-name";
const isGithubPages = process.env.GITHUB_PAGES === "true";

const nextConfig = {
  output: "export",           // 必须：生成纯静态文件
  trailingSlash: true,        // GitHub Pages 推荐
  basePath: isGithubPages ? `/${repoName}` : "",
  assetPrefix: isGithubPages ? `/${repoName}/` : ""
};
```

### .github/workflows/deploy.yml

```yaml
- name: Build static site
  run: GITHUB_PAGES=true NEXT_PUBLIC_BASE_PATH=/your-repo-name npm run build
```

`GITHUB_PAGES=true` 控制 `basePath`（Next.js 构建时的资源路径前缀）。
`NEXT_PUBLIC_BASE_PATH` 控制客户端 JavaScript 中图片/链接的路径前缀。

## 关键陷阱

### 1. 图片路径（已踩坑 · 必查）

`<img src="/images/headshot.png" />` 在 GitHub Pages 下会请求 `https://user.github.io/images/headshot.png`（不带 repo 名），**404**。

**解法：** 用环境变量给图片路径加 basePath。

```tsx
const siteBasePath = process.env.NEXT_PUBLIC_BASE_PATH || "";
// ...
<img src={`${siteBasePath}/images/headshot.png`} alt="" />
```

并在 deploy.yml 中设置 `NEXT_PUBLIC_BASE_PATH=/repo-name`。

注意：`next.config.mjs` 的 `assetPrefix` 只影响 Next.js 构建产物内部的资源引用（如 JS/CSS chunk），**不影响** `<img>` 标签和 `<Link>` 标签（这些是客户端运行时渲染的）。

### 2. 部署后必须验证（被用户"你自己看是个啥"纠正过）

每次推送后，等 GitHub Actions 跑完（约1分钟），**必须用浏览器打开生产 URL 验证**，不能只看 build 输出。

检查项：
- 控制台无 404 错误
- 所有图片正常加载
- 页面滚动到各区块无布局错乱
- 移动端 viewport 无横向滚动

### 3. 静态站点的表单提交

纯静态站点没有后端，表单提交不能 POST。可选方案：

| 方案 | 操作 | 风险 |
|------|------|------|
| mailto 链接 | `<a href="mailto:xxx@qq.com?subject=...&body=...">` | 需用户有默认邮件客户端；部分浏览器不弹窗 |
| 显示联系信息 | 提交后展示"请发送邮件到 xxx@qq.com 或致电" | 最稳，用户手动操作 |
| Formspree | 注册后获得 POST endpoint | 免费版每月50条 |

mailto 陷阱：**用户点了提交不等于邮件已发送。** mailto 只是打开本地邮件客户端，用户还需要在客户端里点"发送"。如果用户没配默认邮箱（或只用网页版），点了没反应。解决方案：提交步骤显示"请将以下信息发送至 xxx@qq.com，或直接致电 138xxxxxxxx"。

### 4. GitHub Actions 部署时间

从 push 到生产环境生效约 **60-90 秒**。Actions 状态可通过 `gh run list` 查看。

## 验证命令

```bash
# 本地构建验证
cd project && npm run build

# 检查部署状态
gh run list --repo user/repo --limit 1

# 浏览器打开生产 URL
open https://user.github.io/repo-name/
```
