#!/usr/bin/env bash
# 冰火岛每日社牛圣经 — cron runner（周六17:00触发）
cd /root/.openclaw/workspace/projects/binghuodao-social-bible

# 加载.env
if [ -f /root/.openclaw/workspace/.env ]; then
  export $(grep -v '^#' /root/.openclaw/workspace/.env | xargs)
fi

# 加载bashrc（含EMAIL_SMTP_PASS）
if [ -f /root/.bashrc ]; then
  source /root/.bashrc
fi

/usr/bin/python3 social_bible_gen.py >> /tmp/social-bible.log 2>&1
