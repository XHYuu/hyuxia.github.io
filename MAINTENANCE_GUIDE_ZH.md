# 个人主页维护说明

这份说明用于以后快速修改主页文字、研究计划、论文、图片和样式。所有路径都以仓库根目录为起点。

## 1. 首页的主要文字和模块

文件：`_pages/about.md`

这个文件控制首页绝大部分内容，包括：

- 顶部姓名、学校、博士身份、导师、研究方向和邮箱链接；
- About me 中英文介绍；
- Selected publications 论文列表及 Paper、Project 链接；
- Selected projects 项目介绍；
- Education 教育经历；
- Honors & Awards 奖项；
- 页面末尾 Contact 联系模块。

修改方法：直接找到页面中对应的英文句子或 HTML 模块后替换文字。链接写在 `href="链接地址"` 中。新增论文时，建议复制一个完整的 `<article class="work-row ...">...</article>` 区块，再修改标题、作者、会议、简介和链接。

## 2. 最新研究计划

文件：`_data/research_plan.json`

这是首页 About me 后方研究计划卡片的数据来源：

- `title`：计划标题；
- `updated`：最近更新时间；
- `lead`：一句话重点；
- `description`：详细说明；
- `tags`：关键词；
- `invitation`：邀请交流的文字。

以后只修改这个 JSON 文件即可更新研究计划，不需要调整页面结构。请保留英文双引号、逗号和方括号的 JSON 格式。

## 3. 独立论文页面和 CV

- `_pages/publications.html`：导航栏 Publications 页面；
- `_pages/cv.md`：导航栏 CV 页面。

首页论文修改后，建议同步更新这两个文件，避免不同页面的信息不一致。

## 4. 头像和论文缩略图

目录：`images/`

- `images/profile-photo.jpg`：首页头像；
- `images/DRDD-poster.jpg`：DRDD 论文缩略图。

替换图片时，最简单的方法是使用相同文件名覆盖原文件，这样不需要修改页面代码。建议使用普通 JPG 或 PNG，确认本地能够正常打开后再上传。若使用不同文件名，需要同时修改 `_pages/about.md` 中相应 `<img src="...">` 的路径。

## 5. 页面颜色、字体、间距和布局

文件：`assets/css/main.scss`

常用位置：

- `.hero`、`.hero h1`：首页顶部布局和姓名字号；
- `.hero-portrait`：头像尺寸与比例；
- `.work-row`、`.work-thumbnail`：论文条目和缩略图；
- `.about-detail`：About me 布局；
- `.research-plan`：研究计划卡片；
- `.awards-grid`：奖项布局；
- `.contact-panel`：底部联系框；
- `@media (max-width: 800px)`：手机端布局。

只改文字时不要动这个文件。需要调整字号、颜色、宽度、留白或圆角时，再修改相应 CSS 属性。

## 6. 网站基础信息和导航栏

- `_config.yml`：网站名称、描述、域名、GitHub Pages 子路径和作者资料；
- `_data/navigation.yml`：顶部导航栏名称与链接。

`_config.yml` 中的 `baseurl: "/hyuxia.github.io"` 是当前项目页面资源路径的重要配置，不要随意删除，否则 CSS 和图片可能无法加载。

## 7. 修改后发布

在仓库目录中完成修改后，依次执行：

```bash
git add .
git commit -m "简短说明本次修改"
git push origin master
```

GitHub Pages 通常需要 1–3 分钟重新构建。发布后如果仍看到旧内容，可使用 `Ctrl + F5` 强制刷新浏览器缓存。

提交前建议确认：页面链接可打开、JSON 格式没有漏逗号或引号、图片已经完整上传，并且没有误改 `_config.yml` 中的 `baseurl`。

