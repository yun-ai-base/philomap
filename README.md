# 脉络 Philomap — 人类思想星图

在群星闪耀时，发现思想的引力。

## 使用方式

直接访问：https://yun-ai-base.github.io/philomap/

本地预览需启动服务器（因为 fetch 加载 JSON 需要 HTTP）：

```bash
npx serve D:\applications\AI_files\philomap
```

## 技术

纯 HTML/CSS/JS + D3.js（自托管 vendor/d3.min.js），GitHub Pages 部署。

## 测试

Playwright 冒烟测试覆盖核心交互（数据加载 / 六视图切换 / 球内多行名字 / 关系旅行 / 时间推进 / 关系类型筛选 / 详情折叠 / 基因测试 / XSS·CSP / 无障碍 / 语言切换），共 22 例。

```bash
# 首次：安装依赖 + 浏览器
npm install
npx playwright install chromium

# 运行冒烟测试（webServer 自动启动静态服务，端口 8911）
npm run test:smoke
```

> 测试依赖受管 Node（`C:/Users/yun/.workbuddy/binaries/node/versions/22.12.0/node.exe`）与受管 Python 静态服务。测试产物写入系统临时目录，不污染仓库。

