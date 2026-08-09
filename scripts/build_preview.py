from pathlib import Path
import re
import json
import html

root = Path(__file__).resolve().parents[1]
source = (root / "_pages" / "about.md").read_text(encoding="utf-8")
body = source.split("---", 2)[2]
body = re.sub(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}", r"\1", body)
plan = json.loads((root / "_data" / "research_plan.json").read_text(encoding="utf-8"))
for key in ("updated", "title", "summary", "detail", "invitation"):
    body = body.replace("{{ site.data.research_plan." + key + " }}", html.escape(plan[key]))
tag_html = "".join(f"<span>{html.escape(tag)}</span>" for tag in plan["tags"])
body = re.sub(r"\{% for tag in site\.data\.research_plan\.tags %\}.*?\{% endfor %\}", tag_html, body)

scss = (root / "assets" / "css" / "main.scss").read_text(encoding="utf-8")
portfolio_css = scss.split("/* Research portfolio redesign */", 1)[1]

shell_css = """
*{box-sizing:border-box}body{margin:0;font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:#fff}
.masthead{position:sticky;top:0;z-index:20;height:74px}.masthead__inner-wrap{height:100%;margin:auto;padding:0 32px;display:flex;align-items:center;justify-content:space-between}.site-title{font-size:18px}.nav-links{display:flex;gap:28px}.nav-links a{font-size:14px;font-weight:650;text-decoration:none}.page{padding:0 32px}.page__footer{padding:28px;text-align:center;color:#697386;background:#f7f8fb;font-size:13px}@media(max-width:800px){.masthead__inner-wrap,.page{padding-left:20px;padding-right:20px}.nav-links{display:none}}
"""

html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hongyu Xia — Academic Portfolio</title><style>{shell_css}\n{portfolio_css}\nhtml{{scroll-behavior:auto!important}}</style></head>
<body><header class="masthead"><div class="masthead__inner-wrap"><strong class="site-title">Hongyu Xia</strong><nav class="nav-links"><a href="#about">About</a><a href="#research">Research</a><a href="#publications">Publications</a><a href="#awards">Awards</a></nav></div></header><main class="page">{body}</main><footer class="page__footer">© 2026 Hongyu Xia · Generative AI Researcher</footer></body></html>"""

out = root / "_preview"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(html, encoding="utf-8")
awards = re.search(r'<section class="home-section" id="awards">.*?</section>', body, re.S).group(0)
awards_html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Awards preview</title><style>{shell_css}\n{portfolio_css}</style></head><body><main class="page"><div class="research-home">{awards}</div></main></body></html>"""
(out / "awards.html").write_text(awards_html, encoding="utf-8")
print(out / "index.html")
