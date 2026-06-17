#!/usr/bin/env python3
"""
冰火岛社牛圣经 / Binghuodao Social Bible — 周六推送
中英双语分离版（中文上半、英文下半）
"""
import smtplib, os, sys, json, subprocess, re, hashlib, random, textwrap
from datetime import datetime, timezone, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from openai import OpenAI
from collections import OrderedDict
import markdown

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seasonal_topics import get_this_week_topics, get_evergreen_pick

SMTP_SERVER = "smtp.126.com"
SMTP_PORT = 465
SENDER = "zhangbojin1107@126.com"
PASSWORD = os.environ.get("EMAIL_SMTP_PASS", "")
RECIPIENT = "9006549@qq.com"
TZ = timezone(timedelta(hours=8))
NOW = datetime.now(TZ)
DATE_STR = NOW.strftime("%Y-%m-%d")
DATE_EN = NOW.strftime("%B %d, %Y")

BOOKS_CN = ["创世记","出埃及记","利未记","民数记","申命记","约书亚记","士师记","路得记",
    "撒母耳记上","撒母耳记下","列王纪上","列王纪下","历代志上","历代志下",
    "以斯拉记","尼希米记","以斯帖记","约伯记","诗篇","箴言",
    "传道书","雅歌","以赛亚书","耶利米书",
    "马太福音","马可福音","路加福音","约翰福音",
    "使徒行传","罗马书","哥林多前书","哥林多后书",
    "加拉太书","以弗所书","腓立比书","歌罗西书","启示录"]
BOOKS_EN = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth",
    "1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles",
    "Ezra","Nehemiah","Esther","Job","Psalms","Proverbs",
    "Ecclesiastes","Song of Solomon","Isaiah","Jeremiah",
    "Matthew","Mark","Luke","John","Acts","Romans","1 Corinthians","2 Corinthians",
    "Galatians","Ephesians","Philippians","Colossians","Revelation"]

def random_chapter():
    i = random.randint(0, len(BOOKS_CN)-1)
    return f"{BOOKS_CN[i]} {random.randint(1,30)}:{random.randint(1,40)}", f"{BOOKS_EN[i]} {random.randint(1,30)}:{random.randint(1,40)}"

# ─── 采集 ───
TOPIC_SOURCES = OrderedDict([
    ("科技 · Tech", {"icon":"🖥️", "feeds":[
        {"url":"https://36kr.com/feed","name":"36氪","max":6},
        {"url":"https://rsshub.app/producthunt/today","name":"ProductHunt","max":4}]}),
    ("财经 · Finance", {"icon":"💰", "feeds":[
        {"url":"https://feeds.a.dj.com/rss/RSSMarketsMain.xml","name":"WSJ Markets","max":5},
        {"url":"https://www.ftchinese.com/rss/news","name":"FT中文网","max":5},
        {"url":"https://feedx.net/rss/bbc.xml","name":"BBC中文","max":5}]}),
    ("体育 · Sports", {"icon":"🏀", "feeds":[
        {"url":"https://www.espn.com/espn/rss/news","name":"ESPN","max":5},
        {"url":"https://www.theguardian.com/sport/rss","name":"Guardian Sport","max":4}]}),
    ("娱乐·音乐·影视 · Entertainment", {"icon":"🎬", "feeds":[
        {"url":"https://www.theguardian.com/culture/rss","name":"Guardian Culture","max":5},
        {"url":"https://rss.nytimes.com/services/xml/rss/nyt/Arts.xml","name":"NYT Arts","max":4},
        {"url":"https://www.billboard.com/feed/","name":"Billboard","max":4}]}),
    ("政治·社会 · Politics & Society", {"icon":"🌍", "feeds":[
        {"url":"https://www.theguardian.com/world/rss","name":"Guardian World","max":4},
        {"url":"https://feedx.net/rss/bbc.xml","name":"BBC中文","max":4},
        {"url":"https://www.aljazeera.com/xml/rss/all.xml","name":"Al Jazeera","max":4}]}),
    ("生活·健康 · Lifestyle & Wellness", {"icon":"🧘", "feeds":[
        {"url":"https://www.theguardian.com/lifeandstyle/rss","name":"Guardian Life","max":4},
        {"url":"https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/well/rss.xml","name":"NYT Well","max":3}]}),
])

def fetch(url, n=6):
    try:
        r = subprocess.run(["curl","-s","--max-time","10","-A","Mozilla/5.0", url], capture_output=True, text=True, timeout=15)
        if r.returncode: return []
        raw = r.stdout
        items = []
        blocks = re.findall(r'<item>(.*?)</item>', raw, re.DOTALL) or re.findall(r'<entry>(.*?)</entry>', raw, re.DOTALL)
        for b in blocks[:n]:
            tl = ld = ""
            for p in [r'<title><!\[CDATA\[(.*?)\]\]></title>', r'<title>(.*?)</title>']:
                m = re.search(p, b, re.DOTALL)
                if m: tl = m.group(1).strip(); break
            m = re.search(r'<link>(.*?)</link>', b, re.DOTALL)
            if m: ld = m.group(1).strip()
            ds = ""
            for p in [r'<description><!\[CDATA\[(.*?)\]\]></description>', r'<description>(.*?)</description>', r'<summary.*?>(.*?)</summary>']:
                m = re.search(p, b, re.DOTALL)
                if m: ds = re.sub(r'<[^>]+>',' ',m.group(1)).strip()[:200]; break
            if tl and ld and len(tl)>4:
                import email.utils
                for p in [r'<pubDate>(.*?)</pubDate>',r'<published>(.*?)</published>']:
                    m = re.search(p,b,re.DOTALL)
                    if m:
                        try:
                            pub = email.utils.parsedate_to_datetime(m.group(1).strip())
                            if (datetime.now(pub.tzinfo or TZ)-pub).total_seconds() > 96*3600: break
                        except: pass
                        break
                else:
                    items.append({"title":tl,"link":ld,"desc":ds})
        return items
    except: return []

def gather_rss():
    """采集RSS源"""
    d = {}
    for cat,cfg in TOPIC_SOURCES.items():
        seen = set(); items = []
        for f in cfg["feeds"]:
            for it in fetch(f["url"], f["max"]):
                k = hashlib.md5((it["title"]+it["link"]).encode()).hexdigest()
                if k not in seen: seen.add(k); items.append(it)
        d[cat] = items
    return d

def _opencli_json(cmd):
    """执行opencli命令并解析JSON结果"""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if r.returncode: return []
        data = json.loads(r.stdout)
        return data if isinstance(data, list) else []
    except:
        return []

def _to_item(x, title_key="title", desc_key="summary"):
    """标准化opencli返回转为{title, link, desc}格式"""
    t = x.get(title_key, "") or x.get("title", "") or x.get("content", "") or ""
    if not t:
        return None
    # 微博热搜格式特殊
    if isinstance(x, dict) and not x.get(title_key):
        t = x.get("word", "") or x.get("title", "") or ""
    return {
        "title": t.strip(),
        "link": x.get("url", "") or x.get("link", "") or "",
        "desc": (x.get(desc_key, "") or x.get("excerpt", "") or x.get("content", "") or "").strip()[:200],
    }


def gather_opencli():
    """使用opencli采集社交平台+新闻源（公开API，无需cookie）"""
    cat_map = [
        # 社交热点
        ("社交热搜 · Social Buzz", [
            # V2EX 热门话题（技术+生活社区讨论）
            lambda: [{"title":x.get("title",""),"link":x.get("link","") or x.get("url",""),"desc":x.get("summary","") or x.get("desc","")} for x in _opencli_json(["opencli", "v2ex", "hot", "-f", "json"])[:6]],
            # Bluesky trending（社交平台热搜）
            lambda: [{"title":x.get("topic",""),"link":"","desc":""} for x in _opencli_json(["opencli", "bluesky", "trending", "-f", "json"])[:6]],
        ]),
        ("科技 · Tech", [
            lambda: [{"title":x.get("title",""),"link":x.get("url","") or x.get("link",""),"desc":x.get("excerpt","") or x.get("summary","")} for x in _opencli_json(["opencli", "bbc", "news", "-f", "json"])[:4]],
        ]),
        ("财经 · Finance", [
            lambda: [{"title":x.get("content",""),"link":"","desc":""} for x in _opencli_json(["opencli", "sinafinance", "news", "-f", "json"])[:6]],
            lambda: [{"title":x.get("title",""),"link":x.get("url","") or x.get("link",""),"desc":x.get("summary","")} for x in _opencli_json(["opencli", "bloomberg", "markets", "-f", "json"])[:3]],
        ]),
        ("体育 · Sports", [
            lambda: [{"title":x.get("title",""),"link":x.get("url","") or x.get("link",""),"desc":x.get("summary","")} for x in _opencli_json(["opencli", "bbc", "news", "-f", "json"])[:6] if "sport" in (x.get("title","") + x.get("summary","")).lower()],
        ]),
        ("娱乐·音乐·影视 · Entertainment", [
            lambda: [{"title":x.get("title",""),"link":x.get("url","") or x.get("link",""),"desc":x.get("summary","")} for x in _opencli_json(["opencli", "hackernews", "top", "--limit", "5", "-f", "json"])[:4]],
        ]),
        ("政治·社会 · Politics & Society", [
            lambda: [{"title":x.get("title",""),"link":x.get("url","") or x.get("link",""),"desc":x.get("summary","")} for x in _opencli_json(["opencli", "bloomberg", "politics", "-f", "json"])[:4]],
        ]),
        ("生活·健康 · Lifestyle & Wellness", [
            lambda: [{"title":x.get("title",""),"link":x.get("url","") or x.get("link",""),"desc":x.get("summary","")} for x in _opencli_json(["opencli", "bloomberg", "main", "-f", "json"])[:3]],
        ]),
    ]
    d = {}
    for cat, fns in cat_map:
        items = []
        seen = set()
        for fn in fns:
            for it in fn():
                if not it.get("title"): continue
                k = hashlib.md5((it["title"] + it.get("link","")).encode()).hexdigest()
                if k not in seen:
                    seen.add(k)
                    items.append(it)
        if items:
            d[cat] = items
    return d

def get_ds():
    with open(os.path.expanduser("~/.openclaw/openclaw.json")) as f:
        c = json.load(f)
    ds = c["models"]["providers"]["deepseek"]
    return ds["apiKey"], ds["baseUrl"]

def call_ai(ak, bu, sp, up):
    from openai import OpenAI as OAI
    client = OAI(api_key=ak, base_url=bu)
    try:
        r = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[{"role":"system","content":sp},{"role":"user","content":up}],
            max_tokens=10000, temperature=0.75, timeout=120)
        return r.choices[0].message.content
    except Exception as e:
        print(f"  AI Error: {e}"); return None

# ─── 去重 ───────────────────────────────────────────
SEASONAL_TOPIC_NAMES = {
    "毕业季", "618 Shopping Fest", "夏天来了", "端午", "Dragon Boat Festival", "Summer is Here",
    "世界杯", "World Cup", "Gaokao", "高考",
}


def build_prompt(cat_items, season_topics, ev):
    # 收集本季节性话题的标题，用于在prompt中标明禁止重复
    season_title_lower = set()
    for s in season_topics:
        season_title_lower.add(s['title'].lower())
        season_title_lower.add(s.get('title_en', '').lower())
        season_title_lower.add(s.get('desc', '').lower()[:20])
    forbidden_topics = sorted(s for s in season_title_lower if s)

    raw = ""
    for cat, its in cat_items.items():
        raw += f"\n## {cat}\n"
        for it in its[:4]:
            raw += f"- {it['title']}\n  {it['desc'][:150]}\n  {it['link']}\n"

    seas = ""
    for s in season_topics:
        seas += f"- {s['title']} / {s.get('title_en','')} — {s.get('desc','')} {s.get('heat','')}\n"

    cc, ce = random_chapter()
    prompt = f"""Two separate newsletters in one document. First half is pure Chinese, second half is pure English.

Today: {DATE_EN}, Saturday. Tag: {cc} / {ce}

RAW MATERIAL (all real RSS data — use this for "本周必聊" and "分类话题"):
{raw}

SEASONAL TOPICS THIS WEEK (use ONLY for "季节限定" section):
{seas}

CLASSIC PICK: {ev['title']} / {ev.get('title_en','')}
Angle: {ev['angle']} / {ev.get('angle_en','')}

### ⚠️ NO FAKE NEWS — NEWS SECTIONS
- "本周必聊", "社交热搜", "科技×财经" must ONLY use topics present in RAW MATERIAL above. Do NOT invent prices, dates, scores, product names, or factual events.
- If RAW MATERIAL is empty for a category, skip it. Do not fabricate news to fill space.
- Examples of what you MUST NOT make up: "Bitcoin broke $200K", "GPT-5 just released", "NBA Finals X-Y", "Marvel trailer views", any specific claim not in the material.

### ⚠️ NO FAKE NEWS — EVERGREEN SECTIONS
- "美食" and "两性·情感" are evergreen. Write from general seasonal observations and social trends. Do NOT invent specific restaurant names, menu items, celebrity stories, or data points.
- "季节限定" and "经典话题新角度" use SEASONAL TOPICS and CLASSIC PICK data directly.

### 🔁 NO REPETITION
- The following topics are ALREADY covered in SEASONAL TOPICS: {', '.join(forbidden_topics[:10])}...
- Do NOT write about any of these topics in "本周必聊", "分类话题" or "Hot This Week". They go ONLY in "季节限定".
- Do NOT write about seasonal topics in the evergreen section either.
- The same topic must NEVER appear in multiple sections.

### FORMAT RULES
- Chinese half: headers in Chinese only. Content in Chinese only.
- English half: headers in English only. Content in English only. ZERO Chinese characters — no parenthetical Chinese translations, no company names in Chinese. If a name has a Chinese equivalent, use the English name only.
- No "中文版本" "英文版本" labels.

PHILOSOPHY: 社牛圣经不是为了汇总新闻，而是把一条信息变成一个社交武器。

每个模块只选 ONE 条最优信息，然后提供 2-3 个不同的切入角度——不同的人用不同的方式聊同一个话题。

Structure:

# 社牛圣经

> 一句封面语（跟封面语呼应）

---

## 本周必聊（最优1条，不是2条）

1条本周最有谈资价值的新闻/话题。

格式：
- 发生了什么？（1-2句简洁交代）
- 📌 角度A：跟谁聊、怎么切入
- 📌 角度B：另一个场合/人群的切入
- 📌 角度C：进阶玩法/深度拆解
- 💬 金句（一句话的social summary）

如果素材不够就别硬凑。不写季节限定列表中的内容。

## 社交热搜

1条来自RAW MATERIAL中"社交热搜 · Social Buzz"的热门社区讨论。

格式同上：1条信息 + 2-3个切入角度 + 金句

## 科技 × 财经

1条。科技与财经交界的话题（最硬核的谈资）。

格式同上：1条信息 + 2-3角度 + 金句

## 美食

1条。常青话题，不需要RAW MATERIAL。写当季最值得聊的美食话题——时令食材、网红吃法、饮食趋势、社交聚餐场景。
不要编造具体的店铺名、菜单、明星代言等，只写通用观察和角度。
格式同上：1条话题 + 2-3角度 + 金句

## 两性·情感

1条。常青话题，不需要RAW MATERIAL。写当季最值得聊的两性话题——约会观察、关系动态、社交中的性别互动。
不要编造具体人物、事件、数据。从趋势和观察角度写。
格式同上：1条话题 + 2-3角度 + 金句

## 季节限定

1条。从SEASONAL TOPICS中选当前最应景的一条。

格式同上：1条信息 + 2-3角度 + 金句

## 经典话题新角度

{ev['title']}，角度 {ev['angle']}。3场景话术。

## 结语

1句呼应封面语。

---

# The Social Bible

---

## Hot This Week (1 topic, not 2)

1 most conversation-worthy item from RAW MATERIAL.

Format:
- What happened? (1-2 sentences)
- 📌 Angle A: Who to talk to and how to open
- 📌 Angle B: Alternative approach for different crowd
- 📌 Angle C: Deeper play
- 💬 One-liner summary

## Social Buzz

1 item from "社交热搜 · Social Buzz" in RAW MATERIAL.

Same format: 1 news + 2-3 angles + one-liner

## Tech × Finance

1 item at the intersection of tech and finance.

Same format: 1 news + 2-3 angles + one-liner

## Food

Evergreen topic — write about seasonal food trends, what's in season, social dining scenes.
Do NOT invent specific restaurants, menus, or celebrity endorsements. General observations only.
Same format: 1 topic + 2-3 angles + one-liner

## Relationships

Evergreen topic — write about dating observations, relationship dynamics, social gender interactions.
Do NOT fabricate specific people, events, or data. Trend-level observations only.
Same format: 1 topic + 2-3 angles + one-liner

## Seasonal Pick

1 item from SEASONAL TOPICS.

Same format: 1 news + 2-3 angles + one-liner

## Classic Topic, Fresh Angle

{ev.get('title_en','')}, angle {ev.get('angle_en','')}. 3 scenarios.

## Closing

1 line echoing the cover line."""
    return prompt

# ─── HTML ───────────────────────────────────────────
CSS_STYLE = """
* { margin:0; padding:0; box-sizing:border-box; }
body {
  font-family: -apple-system, "PingFang SC", "Noto Sans SC", "Helvetica Neue", "SF Pro Text", sans-serif;
  background: #fff;
  margin:0; padding:0;
  -webkit-font-smoothing: antialiased;
}
.container {
  max-width: 620px;
  margin:0 auto;
  background: #fff;
}
.header {
  padding: 28px 24px 16px;
  border-bottom: 1px solid #e5e5ea;
}
.header .title {
  font-size: 28px;
  font-weight: 700;
  color: #000;
  letter-spacing: -0.5px;
}
.header .title .en {
  color: #8e8e93;
  font-weight: 400;
  font-size: 22px;
}
.header .meta {
  color: #8e8e93;
  font-size: 13px;
  margin-top: 6px;
}
.header .meta .tag {
  color: #c7c7cc;
  font-size: 12px;
  margin-left: 4px;
}
.content {
  padding: 8px 28px 20px;
  color: #1c1c1e;
  line-height: 1.6;
  font-size: 17px;
}
.content h1 {
  font-size: 24px;
  font-weight: 700;
  color: #000;
  margin: 32px 0 6px;
  letter-spacing: -0.3px;
}
.content h1 + p {
  color: #8e8e93;
  font-size: 15px;
  margin: 0 0 14px;
}
.content h2 {
  font-size: 16px;
  font-weight: 600;
  color: #8e8e93;
  margin: 36px 0 18px;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-top: 2px solid #e5e5ea;
  padding-top: 24px;
}
.card {
  background: #fafafa;
  border: 1px solid #eee;
  border-radius: 10px;
  padding: 16px 18px;
  margin: 16px 0;
}
.card h3 {
  font-size: 20px;
  font-weight: 600;
  color: #1c1c1e;
  margin: 0 0 8px;
  letter-spacing: -0.3px;
}
.card p {
  margin: 6px 0;
  font-size: 17px;
  line-height: 1.7;
  color: #1c1c1e;
}
.card em {
  font-style: normal;
  color: #8e8e93;
  font-size: 16px;
}
.card strong {
  color: #000;
  font-weight: 600;
}
.card blockquote {
  margin: 10px 0 0 0;
  padding: 12px 16px;
  background: #f2f2f7;
  border-radius: 10px;
  font-size: 17px;
  line-height: 1.7;
  color: #1c1c1e;
}
.card blockquote blockquote {
  margin: 4px 0 0 0;
  padding: 4px 0 0 10px;
  background: transparent;
}
.card blockquote em {
  color: #8e8e93;
  font-size: 15px;
}
.card blockquote strong {
  display: block;
  color: #8e8e93;
  font-size: 12px;
  font-weight: 600;
  margin-bottom: 2px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.content > p {
  font-size: 15px;
  color: #666;
}
.content > hr {
  border: none;
  height: 1px;
  background: #e5e5ea;
  margin: 18px 0;
}
.content ul, .content ol {
  margin: 4px 0;
  padding: 0 0 0 16px;
}
.content li {
  margin: 4px 0;
  font-size: 15px;
  color: #1c1c1e;
}
.content a { color: #007aff; text-decoration: none; }
.content code { background: #f2f2f7; padding:0 4px; border-radius:4px; font-size:13px; }
.footer {
  padding: 16px 24px;
  border-top: 1px solid #e5e5ea;
  text-align: center;
  font-size: 12px;
  color: #c7c7cc;
  line-height: 1.6;
}
"""

FULL_HTML_TEMPLATE = """<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>{CSS}</style>
</head><body>
<div class="container">
<div class="content">
{BODY}
</div>
<div class="footer">
  冰火岛 · 每周六17:00 · 中英双语
</div>
</div></body></html>"""

def wrap_cards(html):
    """Post-process: wrap each h3 topic into a .card div"""
    result = []
    card_buf = None
    lines = html.split('\n')
    for line in lines:
        s = line.strip()
        is_h3 = bool(re.match(r'<h3[> ]', s))
        is_section_break = bool(re.match(r'<(h[12]|hr[/ ])', s))
        if is_h3:
            if card_buf is not None:
                result.append('<div class="card">')
                result.extend(card_buf)
                result.append('</div>')
            card_buf = [line]
        elif is_section_break:
            if card_buf is not None:
                result.append('<div class="card">')
                result.extend(card_buf)
                result.append('</div>')
                card_buf = None
            result.append(line)
        elif card_buf is not None:
            card_buf.append(line)
        else:
            result.append(line)
    if card_buf is not None:
        result.append('<div class="card">')
        result.extend(card_buf)
        result.append('</div>')
    return '\n'.join(result)

def convert_md_to_html(md_text, chap_cn, chap_en):
    extensions = ["extra", "codehilite"]
    body_html = markdown.markdown(md_text, extensions=extensions)
    body_html = wrap_cards(body_html)
    html = FULL_HTML_TEMPLATE.format(
        CSS=CSS_STYLE,
        DATE_CN=f"{DATE_STR} 周六",
        DATE_EN=DATE_EN,
        CHAP_CN=chap_cn,
        CHAP_EN=chap_en,
        BODY=body_html,
    )
    return html

def send(html, text_alt):
    pw = os.environ.get("EMAIL_SMTP_PASS", "")
    if not pw:
        import subprocess
        try:
            r = subprocess.run(["bash","-c","source ~/.bashrc && echo $EMAIL_SMTP_PASS"], capture_output=True, text=True, timeout=5)
            pw = r.stdout.strip()
        except: pass
    if not pw:
        print("  ❌ No SMTP password"); return
    msg = MIMEMultipart("alternative")
    msg["From"] = SENDER; msg["To"] = RECIPIENT
    msg["Subject"] = f"社牛圣经 / Social Bible | {DATE_STR}"
    msg.attach(MIMEText(text_alt or "HTML only", "plain", "utf-8"))
    msg.attach(MIMEText(html, "html", "utf-8"))
    try:
        s = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        s.login(SENDER, pw)
        s.sendmail(SENDER, [RECIPIENT], msg.as_string())
        s.quit()
        print(f"  ✅ Sent to {RECIPIENT}")
    except Exception as e:
        print(f"  ❌ Send failed: {e}")
    print("✅ 完成")

def fallback(seasons, ev):
    cc, ce = random_chapter()
    md = "# 社牛圣经\n\n> 今天的小话题\n\n---\n\n## 本周必聊\n\n---\n\n## 分类话题\n\n---\n\n## 季节限定\n"
    for s in seasons:
        md += f"\n### {s['title']}\n{s.get('desc','')}\n\n"
    md += "---\n\n## 经典话题新角度\n\n"
    md += f"{ev['title']}，角度 {ev['angle']}\n\n---\n\n## 装逼话术精选\n\n> **Move 1**\n> 「最近太忙了，连XX都没时间追」\n> — 万能开场\n\n> **Move 2**\n> 「你说得对，不过换个角度想……」\n> — 万能接话\n\n---\n\n## 圣经结语\n\n社交没那么可怕。\n\n---\n\n# The Social Bible\n\n---\n\n## Seasonal Picks\n"
    for s in seasons:
        md += f"\n### {s.get('title_en','')}\n{s.get('desc','')}\n\n"
    md += "---\n\n## Classic Topic, Fresh Angle\n\n"
    md += f"{ev.get('title_en','')}, angle {ev.get('angle_en','')}\n\n---\n\n## Power Moves of the Week\n\n> **Move 1**\n> \"I've been so busy lately...\"\n> — Universal opener\n\n---\n\n## Closing\n\nSocializing isn't that scary.\n"
    return md, cc, ce

def main():
    print(f"🦐 社牛圣经 {DATE_STR}")
    seasons = get_this_week_topics()
    ev = get_evergreen_pick()
    print(f"  Season: {len(seasons)}, Evergreen: {ev['title']}")
    print("  Fetching opencli...")
    data = gather_opencli()
    total = sum(len(v) for v in data.values())
    print(f"  Got {total} items from opencli")
    if total < 5:
        print(f"  opencli too few ({total}), trying RSS...")
        data = gather_rss()
        total = sum(len(v) for v in data.values())
        print(f"  Got {total} items from RSS")
    if total < 5:
        print(f"  Only got {total} items — too few for AI generation, using fallback")
        raw_md, cc, ce = fallback(seasons, ev)
    else:
        ak, bu = get_ds()
        prompt = build_prompt(data, seasons, ev)
        print("  AI generating...")
        ai_text = call_ai(ak, bu, f"Today {DATE_STR} Saturday. Write in Markdown.", prompt)
        if ai_text and len(ai_text) > 500:
            print(f"  AI output: {len(ai_text)} chars")
            raw_md = ai_text
            cc, ce = random_chapter()
        else:
            print("  AI failed, using fallback")
            raw_md, cc, ce = fallback(seasons, ev)
    # 后处理：清除英文半区中的中文 + 防斜体
    half = raw_md.split('# The Social Bible', 1)
    if len(half) == 2:
        en_clean = re.sub(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]+', '', half[1])
        raw_md = half[0] + '# The Social Bible' + en_clean
    # 行首 * 列表标记 -> - ，防止markdown解析为斜体
    raw_md = re.sub(r'^\* ', '- ', raw_md, flags=re.MULTILINE)

    html = convert_md_to_html(raw_md, cc, ce)
    preview_path = os.path.expanduser("~/.openclaw/workspace/social-bible-preview.html")
    with open(preview_path, "w") as f:
        f.write(html)
    md_path = os.path.expanduser("~/.openclaw/workspace/social-bible-preview.md")
    with open(md_path, "w") as f:
        f.write(raw_md)
    print(f"  ✅ Preview saved")
    send(html, raw_md)

if __name__ == "__main__":
    main()
