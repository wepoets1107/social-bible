#!/usr/bin/env python3
"""生成社牛圣经HTML预览，不发邮件"""
import os, sys, json, re, random
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seasonal_topics import get_this_week_topics, get_evergreen_pick
from social_bible_gen import (
    get_deepseek_config, gather_all, call_ai, build_ai_prompt,
    render_html, build_fallback_body, random_chapter, TOPIC_SOURCES
)

TZ = timezone(timedelta(hours=8))
NOW = datetime.now(TZ)
DATE_STR = NOW.strftime("%Y-%m-%d")

def main():
    print("🦐 社牛圣经 — 生成HTML预览")
    
    seasonal_topics = get_this_week_topics()
    evergreen_pick = get_evergreen_pick()
    print(f"  季节话题: {len(seasonal_topics)}个")
    print(f"  常青话题: {evergreen_pick['title']} → {evergreen_pick['angle']}")
    
    print("  采集热点中...")
    category_items = gather_all()
    total = sum(len(v) for v in category_items.values())
    print(f"  采集到 {total} 条")
    
    api_key, base_url = get_deepseek_config()
    prompt = build_ai_prompt(category_items, seasonal_topics, evergreen_pick)
    
    print("  AI生成中...")
    ai_text = call_ai(api_key, base_url, 
        f"你是「冰火岛社牛圣经」的主编小虾。今天是{DATE_STR}。",
        prompt)
    
    if ai_text and len(ai_text) > 500:
        print(f"  AI输出 {len(ai_text)} 字")
        text_for_send = ai_text
        chap_cn, _ = random_chapter()
        ch_match = re.search(r'(马太|马可|路加|约翰|创世|诗篇|箴言|传道)[^0-9]*(\d+)[：:]\s*(\d+)', ai_text)
        if ch_match:
            chap_cn = ch_match.group(0)
    else:
        print("  AI输出异常，使用备用模板")
        text_for_send, chap_cn = build_fallback_body(seasonal_topics, evergreen_pick)
    
    html_body = render_html(text_for_send, chap_cn)
    
    out_path = "/root/.openclaw/workspace/projects/binghuodao-social-bible/preview.html"
    with open(out_path, "w") as f:
        f.write(html_body)
    print(f"  ✅ 预览已保存: {out_path}")
    
    # 也复制到workspace根目录方便访问
    import shutil
    shutil.copy(out_path, "/root/.openclaw/workspace/social-bible-preview.html")
    print(f"  ✅ 副本: social-bible-preview.html")

if __name__ == "__main__":
    main()
