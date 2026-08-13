# 脉络 Philomap — 全维度审核报告

> 审核日期：2026-08-13
> 审核对象：`index.html`（2199 行，177KB）+ `data/philosophers.json`（60 位哲人，1.05MB）+ `scripts/`（9 个脚本）+ `vendor/d3.min.js`（v7.9.0）
> 部署：https://yun-ai-base.github.io/philomap/
> 结论：项目核心体验已相当完整（星图/时光长河/光谱/对决/基因测试/孪生宇宙六视图，中英双语，收藏、深链接、键盘导航均已落地），且上一轮审计（`PHILOMAP_改进建议.md`）中的多数 Bug 已修复。**但存在一处数据一致性的高危问题、一处远程数据注入的安全隐患，以及若干结构性技术债**，详见下文。

---

## 执行摘要（TL;DR）

| 优先级 | 问题 | 影响 |
|---|---|---|
| 🔴 高 | 基因测试引用 42 个不存在于数据集的哲人 id，结果被静默丢弃 | 测试结果失真，用户被误导 |
| 🔴 高 | 孪生宇宙从远程 `projects.json` 拉取内容后直接 `innerHTML` 拼接，无 CSP | 存储型 XSS 风险 |
| 🟠 中 | 文明圈严重失衡（西 45 / 东 12 / 印 2 / 伊 1），"四大文明"名不副实 | 内容权威性受损 |
| 🟠 中 | 对决/光谱打分是关键词启发式，无"示意性"标注 | 易被误读为严谨结论 |
| 🟠 中 | 单文件 2199 行 CSS+HTML+JS 混写，9 个一次性脚本遗留 | 维护成本高 |
| 🟡 低 | 无测试、无构建、无 CSP、无障碍缺失、对比度不足 | 工程与体验打磨 |

---

## 一、用户交互

### 现状亮点（已做得不错）
- 键盘导航已覆盖 `/`（聚焦搜索）、`f`（折叠筛选）、`Esc`（关闭）、`1–6`（切视图）、方向键（节点间导航）、`Enter`（打开）。
- 深链接 `#view=…&p=…` 与分享链接已实现，`hashchange` 监听可回溯。
- 收藏持久化（localStorage）、随机哲人、字号调节均可用。

### 问题与建议

**1.【中】边的交互信息完全缺失（死代码）**
`#edge-tip` 的 DOM 与 CSS 都已写好（行 636、230–233），`relationshipTypes` 里也有 `description` 字段，但 `edgeLines`（渲染在行 1589）**从未绑定任何 `mouseenter/mousemove` 事件**。结果是：
- 图上 132 条边（师承/影响/论战）只能靠虚线样式猜类型；
- 关系描述数据躺在 JSON 里永远不被消费。

**建议**：给 `edgeLines` 绑定 hover，填充 `#edge-tip` 的 `et-title`（两哲人 + 类型）、`et-type`、`et-desc`，并把 hover 命中线加粗高亮。这是补齐"关系为什么重要"的关键一步。

**2.【中】对决视图的交互门槛偏高**
`setupDuel` 每次进入都重新填充 `<select>` 并硬编码默认 `confucius` vs `plato`（行 1791）。但"开始对决"前需要用户先选两个哲人 + 选议题，三个下拉的引导弱，无空状态提示。

**建议**：议题未选时禁用"开始对决"按钮并给出 tooltip；首次进入随机预选两位哲人（增加探索趣味）；记忆用户上次的对决组合。

**3.【低】时光长河的滚动无惯性/吸附提示**
`renderTimeRiver` 用 2600px 宽 canvas + 横向滚动，但无"当前所处时代"的高亮指示，也无滚动到某时代的快捷方式。

**建议**：顶部加一个迷你时代刻度条，点击跳到对应年份；滚动时高亮当前时代标签。

**4.【低】筛选反馈可更即时**
`applyAllFilters` 已做 500ms 淡入淡出，但筛选后面板数字徽标（`filter-count`）只在点击时更新，缺少"当前可视 N 位哲人"的总数提示。

**建议**：筛选后在图角落显示"当前显示 X / 60 位哲人"，空结果时给"无匹配，重置筛选"引导按钮。

---

## 二、UI 设计与布局

### 现状亮点
- 深色星空主题统一，文明四色（`#818cf8/#fbbf24/#f472b6/#34d399`）贯穿节点、边渐变、雷达图、徽章，视觉语言一致。
- CSS 变量集中管理字号（`--fs-*`）与文明色，字号三档可调。
- 移动端有 `mob-filter-btn` + 遮罩层适配，响应式做了基本处理。

### 问题与建议

**1.【中】对比度不足，次级文本偏暗**
多处使用 `#64748b`（浅灰蓝）作为次级文本色，置于 `#000008` 深底上，对比度约 **3.9:1**，低于 WCAG AA 正文 4.5:1 标准。涉及：loading 提示、subtitle、tooltip 年份、搜索占位符、空状态、`.sr-meta`、`.dp-*` 次级描述等。

**建议**：把次级文本统一提升到 `#94a3b8` 或 `#a5b4c8`；`#64748b` 仅用于装饰性/禁用态。

**2.【高】可访问性基本缺失**
- 所有节点是 SVG `<circle>`，**无 `tabindex`、无 `role`、无 `aria-label`**，屏幕阅读器与纯键盘用户无法感知图结构。
- 无 `aria-live` 用于筛选结果、详情面板开合等动态变化。
- `<html lang="zh-CN">` 固定，切到 EN 时未同步 `document.documentElement.lang`。
- 无 `prefers-reduced-motion` 处理：星空动画（170 星点 requestAnimationFrame）与力导向动画对前庭敏感用户不友好。

**建议**（按优先级）：
1. 给节点 group 加 `tabindex="0"` + `role="button"` + `aria-label="泰勒斯，公元前624—546"`，Enter 打开详情（已有 `kbFocusIdx` 逻辑，可复用）。
2. 加 `@media (prefers-reduced-motion: reduce)` 关闭星空动画与模拟动画。
3. `applyLang()` 内同步 `document.documentElement.lang = lang==='en'?'en':'zh-CN'`。

**3.【中】节点标签重叠问题仍存在**
`updateLabelOpacity`（行 1657）已按缩放级别 + 影响力淡入标签，但高影响力节点在中等缩放下仍会互相重叠（60 个节点，12 位高影响力哲人集中在中西轴心区）。

**建议**：引入简单标签碰撞检测（如按 `labelAnchor` 或检测相邻节点屏幕距离），重叠时只显示影响力最高者；或让标签支持拖拽偏移。

**4.【低】组件复用度低**
六视图的开关逻辑（`switchView`）用大量 `if...else` + 逐个 `style.display` 切换，重复度高。

**建议**：抽一个视图配置表（`{view, panelIds, onEnter, onExit}`），用数据驱动切换，减少样板代码。

---

## 三、内容维度

### 现状亮点
- 60 位哲人字段完整度高：summary/coreThoughts/goldenQuotes/anecdote/aiReview/thoughtEvolution/representativeWorks 均 100% 覆盖。
- 中文内容质量高，"入门/类比/研究"三层递进（l1/l2/l3）设计很有想法。
- 中英双语数据已基本补齐（`summaryEn` 0 缺失）。

### 问题与建议

**1.【高】基因测试的选项指向 42 个不存在于数据集的哲人（数据一致性 BUG）**
实测扫描：`quizQuestions` 共引用 **83 个哲人 id，其中 42 个在 `philosophers.json` 中不存在**（如 `camus/sartre/beauvoir/montaigne/epictetus/bentham/habermas/popper/gandhi/rawls/smith/marcus-aurelius`（实际 id 是 `marcus-aurelius` 但题里写 `marcus`）、`zen`、`christianity`、`mao`、`lenin` 等）。

`computeQuizResults` 里虽有一个 26 条的 `idMap`，但只覆盖了极小部分，且**不存在的 id 会被 `if(dataRef.philosophers.find(...))` 静默丢弃**（行 1979）。后果：用户选"反抗痛苦、创造意义"本应命中加缪/萨特，却因这些 id 不存在而分数丢失，最终结果被少数"真实存在"的哲人霸榜，**测试结论系统性失真**。

**建议**（高优先）：
1. 用脚本校验 `quizQuestions` 所有 id 与数据集对齐，把幽灵 id 替换为真实 id 或补录哲人。
2. 为 `computeQuizResults` 增加运行时告警（`console.warn('quiz 引用缺失哲人', id)`）。
3. 把 quiz 数据抽到 JSON 或至少集中一个常量表，避免散落硬编码。

**2.【高】文明圈严重失衡，与"四大文明"定位不符**
实测：西方 45 / 东方 12 / 印度 2 / 伊斯兰 1。印度与伊斯兰几乎是点缀，`civilizations` 却声明了 4 个圈、界面也展示 4 色图例。这削弱了"人类思想星图"的完整性与可信度。

**建议**：按 `PHILOMAP_改进建议.md` 的清单补强——印度（商羯罗/龙树/陈那/泰戈尔）、伊斯兰黄金时代（法拉比/阿威罗伊/安萨里/伊本·赫勒敦），以及日本京都学派、非洲/拉美思想者。若短期不补，至少在图例或 About 页说明"当前收录偏向，持续扩充中"。

**3.【中】对决/光谱的打分结果缺乏"示意性"声明**
`scoreByKeywords` / `scorePhilosopher` 是关键词命中计数（行 1820–1834、2076–2081），属于启发式打分，但界面（雷达图、光谱散点、对决胜负）**没有任何"仅供参考/非严谨学术结论"的标注**。用户可能把"尼采 8.5 分 vs 康德 7.2 分"当作客观排名。

**建议**：在光谱图和对决结果区加一行小字脚注："维度得分为基于文本关键词的示意性估计，非权威学术评价。"同时可附上"查看文本依据"入口。

**4.【低】头像覆盖仅 50%，且全依赖 Wikimedia 外链**
30/60 有头像（全部 `upload.wikimedia.org`），其余用首字母占位。外链头像受网络/版权影响，且无本地缓存。

**建议**：统一生成 SVG 字母牌（保持现有首字母方案的美观版）作为兜底；公共领域画像可下载到本地 `assets/portraits/` 减少外链依赖。

**5.【低】时代划分可再细化**
`eras` 有 14 个，但时光长河（`renderTimeRiver`）用的是另一套硬编码的 6 段（行 1744），两处时代体系不一致。

**建议**：统一用 `data/eras` 驱动时光长河，消除双轨；并细分"启蒙法/德分流""分析哲学""存在主义"等。

---

## 四、数据多样性

### 现状亮点
- 数据模型设计合理：`metadata/civilizations/schools(37)/eras(14)/relationshipTypes(3)/philosophers(60)` 分层清晰，哲人字段丰富（含 `layers.L7_legacy` 影响图谱、`furtherReading`、`timeline`、`famousEvents`）。
- 孤儿关系已修复（上一轮审计的 11 条 dangling 已归零）。
- 关系类型区分（师承/影响/论战）+ 强度字段，为可视化提供了数据基础。

### 问题与建议

**1.【中】1MB JSON 全量一次性 fetch，无加载态粒度**
`init()` 直接 `fetch('data/philosophers.json')` 全量加载（行 1571），60 人已 1.05MB。若按建议扩充到数百人，首屏会明显变慢，且低带宽/移动端体验差。

**建议**：
1. 短期：gzip 预压缩（GitHub Pages 支持 `.json.gz`）+ 加 `Content-Encoding`；或生成 minify 版 JSON（去缩进，可省 ~30%）。
2. 长期：按文明分片（`western.json/indian.json/...`）懒加载，星图首屏只载节点骨架（id/name/civilization/birth/influence），详情面板再按需拉取该哲人完整字段。

**2.【中】`philosophers.bak.json`（1.05MB）作为备份文件进了仓库**
`data/philosophers.bak.json` 与主数据几乎同大，属于临时备份，不应随仓库分发（增加 Pages 体积、易造成"哪个是权威数据"的困惑）。

**建议**：移出仓库（改用 git 历史或本地备份），或在 `.gitignore` 排除 `*.bak.json`。

**3.【低】缓存策略缺失**
`fetch` 未带缓存控制，`projects.json` 用 `cache:'no-cache'` 但主数据没有。浏览器可能缓存旧数据导致用户看不到更新。

**建议**：主数据 fetch 加 `cache:'no-store'` 或版本号 query（`philosophers.json?v=3`），配合 `metadata.version` 字段做一致性检查。

**4.【低】状态管理散落全局变量**
`dataRef/simData/simulation/selectedNode/favSet/currentView/currentFilters/timeRange` 全是模块级 `let/const`，无统一状态容器。当前规模尚可控，但扩展视图/功能时会互相踩踏。

**建议**：引入轻量 store（如一个 `state` 对象 + `setState` 订阅，或直接上 Vue/React 响应式），至少把"视图状态 vs 数据状态"分离。

---

## 五、代码质量与安全

### 现状亮点
- 命名整体清晰（`processData/renderGraph/openDetailPanel/buildSearchIndex` 等），函数职责基本单一。
- 性能优化到位：力导向预计算 150 tick、星空动画按视图/可见性门控、概念网络模拟复用并 `stop()` 旧实例（上一轮的内存泄漏已修）。
- `try/catch` 覆盖了 localStorage、fetch、hash 写入等易抛异常处。
- 未发现硬编码 token/key/secret（已扫描）。

### 问题与建议

**1.【高】孪生宇宙存在存储型 XSS 注入点**
`buildTwinUniverse`（行 1547–1566）从远程 `https://yun-ai-base.github.io/psychscope/projects.json` 拉取内容，然后把 `name/desc/icon/cat` **直接拼进 `innerHTML`**（行 1562、1566）。该 JSON 是跨仓库维护的、非本仓库可信数据。一旦 `projects.json` 被篡改（或供应链被污染），恶意 `<img onerror>` / `<script>` 会注入 philomap 页面，且**页面无任何 CSP**。

**建议**（高优先）：
1. 对所有动态拼接进 `innerHTML` 的字符串做 `escapeHtml()` 转义（`name/desc/icon` 尤甚）。
2. 加 CSP meta 头：`default-src 'self'; img-src 'self' https://upload.wikimedia.org data:; style-src 'self' 'unsafe-inline'; script-src 'self'`。
3. 顺带排查详情面板里大量 `innerHTML` 拼接（`summary/quotes/timeline/works/furtherReading`），虽然数据来自本地 JSON（相对可信），但数据文件本身也是外部输入，统一走 `escapeHtml` 或改用 `textContent` 更稳妥。

**2.【中】单文件 2199 行，CSS+HTML+JS 混写**
这是最大的可维护性债。任何功能改动都要在这 177KB 的单文件里定位，易冲突、难 review、难复用。

**建议**：拆分 ES module（静态托管下 `type="module"` 完全可用）：
- `data.js`（数据加载 + 处理）、`graph.js`（力导向）、`views/star.js|river.js|spectrum.js|duel.js|quiz.js|twin.js`、`i18n.js`、`store.js`。
- CSS 拆到 `styles/`。这是一次性重构，回报高。

**3.【中】`scripts/` 下 9 个 `fix_en_*.py` 一次性脚本遗留**
`fix_en_quotes.py / fix_en_deep.py / fix_en_deep_all.py / fix_en_final.py / fix_en_remaining.py / fix_en_all_deep.py / fix_en_mass.py / fix_en_all_we.py` 是历次修英文数据的临时脚本，已无复用价值，留在仓库误导后人（哪个是最终版？）。

**建议**：归档到 `scripts/archive/` 或删除；保留一个权威的 `scripts/build_data.py`（校验 + 归一化 + 生成 minify）即可。

**4.【低】无自动化冒烟测试**
改一处 JS 可能悄悄弄坏某视图，目前全凭人工。

**建议**：加 Playwright 冒烟（加载→无 console error→切 6 视图→开详情→收藏→切语言→对决→基因测试走完），挂到 CI。至少先加 `node --check` 语法校验到提交前钩子。

**5.【低】`formatYear` 等纯函数与 DOM 逻辑混杂**
`formatYear/formatYears/lf/escapeHtml`（`escapeHtml` 尚未存在）等纯函数散落在渲染代码里。

**建议**：抽 `utils.js`，便于单测。

---

## 六、项目整体质感与功能

### 现状亮点
- 功能完整性高：六视图 + 搜索 + 筛选 + 收藏 + 随机 + 深链接 + 双语 + 导出 Markdown，是同类里少见的完整形态。
- 视觉质感出色：星空背景、发光节点、文明色渐变边、玻璃拟态面板，主题统一且精致。
- 已自托管 d3（v7.9.0），不依赖 CDN，加载可控。
- GitHub Pages 部署链路已跑通，README 说明了本地 `npx serve` 预览方式。

### 问题与建议

**1.【中】构建/部署是"手推"式的**
无构建脚本、无 minify、无校验。当前 `git status` 显示 `data/philosophers.json`、`index.html` 有未提交改动，还有多个 untracked 文件——说明上线靠手工 git push，容易漏文件或漏步骤（用户记忆里也记录了 Pages 连发部署会卡死的坑）。

**建议**：加一个 `deploy.sh`/`deploy.py`（校验 JSON → `node --check` → 一次性 commit+push），并遵循"一次集成 push"的教训。README 补一段部署说明。

**2.【中】访问统计是死代码**
历史提交显示曾接入 CountAPI 后改为"本地 stats-server"，但当前代码里统计逻辑已移除，仅剩注释残留。README 未提任何统计。

**建议**：要么落地一个隐私友好的计数（如 Cloudflare/自建），要么明确删除并说明"本站无任何追踪"，消除代码与文档的模糊。

**3.【低】README 过于单薄**
仅 15 行，未说明功能清单、数据结构、贡献方式、许可、隐私声明。

**建议**：补全：功能概览、数据来源与许可（画像版权、名言出处）、如何贡献哲人数据、隐私说明（localStorage 用途）。

**4.【低】缺 `robots`/SEO 元信息**
`<meta>` 只有 viewport 和 charset，无 description、og、canonical。作为可分享的知识型站点，分享到社交媒体的卡片是空白的。

**建议**：补 `description`、`og:title/og:image`、`twitter:card`，生成一张分享封面图。

---

## 总体改进路线图

### 第一阶段：止血（高优先，1–2 天）
1. **修复基因测试幽灵 id**：脚本对齐 42 个缺失 id，替换或补录，加运行时告警。
2. **修复孪生宇宙 XSS**：加 `escapeHtml()` + CSP meta。
3. **移出 `philosophers.bak.json`**，`.gitignore` 加 `*.bak.json`。

### 第二阶段：内容与可信度（3–5 天）
4. 文明圈补强（印度 2→5+、伊斯兰 1→5+，优先）。
5. 对决/光谱加"示意性非权威"脚注。
6. 统一时光长河的时代表（复用 `data/eras`）。
7. 补全 50% 缺失头像（SVG 字母牌兜底 + 本地化公共领域画像）。

### 第三阶段：工程化与可访问性（1 周）
8. 拆分单文件为 ES module + 独立 CSS。
9. 补边的 hover tooltip（消费 `relationshipTypes.description`）。
10. 无障碍：节点 `tabindex/role/aria-label`、`prefers-reduced-motion`、同步 `<html lang>`。
11. 对比度提升到 WCAG AA。

### 第四阶段：基建与增长（持续）
12. 数据分片懒加载 + gzip + 版本化缓存。
13. Playwright 冒烟测试 + CI + 部署脚本。
14. README/SEO/分享卡片补全。
15. 统一状态管理，为后续新视图（对比、时间线联动）铺路。

---

*报告完。所有行号基于审核时点的本地文件快照。*
