#!/usr/bin/env python3
"""Replace build_prompt's return value with the V10-tested version"""
import re

path = '/root/.openclaw/workspace/projects/binghuodao-social-bible/social_bible_gen.py'
with open(path) as f:
    content = f.read()

# Find the build_prompt function's return value
marker = 'cc, ce = random_chapter()'
idx = content.find(marker)
if idx == -1:
    print("ERROR: marker not found")
    exit(1)

# Find the triple-quoted f-string after the marker
after = content[idx:]
fstr_start = after.find('    return f"""')
if fstr_start == -1:
    print("ERROR: fstr_start not found")
    exit(1)

fstr_start_abs = idx + fstr_start
# Find closing triple quotes
close = content.find('"""', fstr_start_abs + 16)
if close == -1:
    print("ERROR: closing not found")
    exit(1)
close_abs = close + 3

new_prompt = """    cc, ce = random_chapter()
    return f\"\"\"Bilingual social conversation newsletter in Markdown.

Today: {DATE_EN}, Saturday. Tag: {cc} / {ce}

RAW MATERIAL:
{raw}

SEASONAL TOPICS THIS WEEK:
{seas}

CLASSIC PICK: {ev['title']} / {ev.get('title_en','')}
Angle: {ev['angle']} / {ev.get('angle_en','')}

KEY RULE: Chinese FIRST (entire top half). English SECOND (entire bottom half). Do NOT interleave.

Structure: ALL Chinese sections first, then ALL English sections.

--- CHINESE HALF ---

## 本周必聊

2 hot topics in Chinese. Each: title, context, why sparks, conv starter, deeper dive.

## 分类话题

1-2 topics from each: 科技, 财经, 体育, 娱乐, 政治社会, 生活方式

## 季节限定

Seasonal topics in Chinese with conv starters.

## 经典话题新角度

{ev['title']}，角度 {ev['angle']}。3场景话术.

## 装逼话术精选

3-5 moves in Chinese.

## 圣经结语

结语中文

--- ENGLISH HALF ---

## Hot This Week

Same 2 topics in English.

## Category Topics

Same 6 categories in English.

## Seasonal Picks

Same in English.

## Classic Topic, Fresh Angle

{ev.get('title_en','')}, angle {ev.get('angle_en','')}. 3 scenarios in English.

## Power Moves of the Week

Same 3-5 in English.

## Closing

English closing.

Mandatory: Chinese first (top half), English second (bottom half). NOT interleaved. NOT line by line.\"\"\""""

new_content = content[:fstr_start_abs] + new_prompt + content[close_abs:]
with open(path, 'w') as f:
    f.write(new_content)
print("Prompt replaced successfully")
