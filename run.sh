#!/usr/bin/env bash
# 冰火岛每日社牛圣经 — cron runner（每日17:00触发）
cd /root/.openclaw/workspace/projects/binghuodao-social-bible

# 加载.env（项目目录优先，含 SMTP_SENDER / SMTP_RECIPIENT）
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# 加载bashrc（含EMAIL_SMTP_PASS）
if [ -f /root/.bashrc ]; then
  source /root/.bashrc
fi

# EMAIL_SMTP_PASS → SMTP_PASS（变量名对齐）
if [ -n "$EMAIL_SMTP_PASS" ] && [ -z "$SMTP_PASS" ]; then
  export SMTP_PASS="$EMAIL_SMTP_PASS"
fi

/usr/bin/python3 social_bible_gen.py >> /tmp/social-bible.log 2>&1
