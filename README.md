# 社牛圣经 / The Social Bible 🦐

A weekly bilingual social cheat sheet. Every Saturday, one email — seven conversation modules, each with **one topic, 2-3 conversation angles, and a killer one-liner**.

不是新闻摘要，是**社交武器**。帮你把一条信息变成随时能开的腔。

---

## Philosophy

Knowing what happened ≠ knowing how to talk about it.

This project doesn't aggregate news. It **weaponizes** information for conversation. Each module picks the single best topic of the week and gives you multiple ways to open — whether you're at a dinner party, a coffee chat, or a WeChat group.

---

## Quick Start（丢给AI看这段就能配置）

### 1. Clone

```bash
git clone https://github.com/wepoets1107/social-bible.git
cd social-bible
```

### 2. Install dependencies

```bash
# Python deps
pip install openai markdown

# opencli (for social platform data — public feeds, no login required)
npm install -g @jackwener/opencli
```

### 3. Copy and edit config

```bash
cp .env.example .env
# Then edit .env with your real credentials
```

### 4. Run

```bash
source .env && python3 social_bible_gen.py
```

If you paste this whole section into an AI coding agent (Claude/ChatGPT/Cursor), it will understand everything it needs.

---

## Structure

| Module | Source |
|--------|--------|
| 本周必聊 / Hot This Week | Real-time feeds (Bloomberg, BBC, Sina Finance) |
| 社交热搜 / Social Buzz | V2EX, Bluesky trending |
| 科技×财经 / Tech×Finance | Bloomberg, Hacker News |
| 美食 / Food | Evergreen seasonal observations |
| 两性·情感 / Relationships | Evergreen social observations |
| 季节限定 / Seasonal Picks | Calendar events, World Cup, holidays |
| 经典话题 / Classic Topic | Rotating evergreen topics |

---

## Configuration Reference

| Env Var | Required | Default | Description |
|---------|----------|---------|-------------|
| `SMTP_SENDER` | ✅ | — | SMTP login email, e.g. `yourname@126.com` |
| `SMTP_RECIPIENT` | ✅ | — | Where the newsletter is sent, e.g. `you@gmail.com` |
| `SMTP_PASS` | ✅ | — | SMTP authorization code (NOT your email password) |
| `SMTP_SERVER` | ❌ | `smtp.126.com` | SMTP host (use `smtp.gmail.com` for Gmail, `smtp.qq.com` for QQ) |
| `SMTP_PORT` | ❌ | `465` | SMTP port (465=SSL, 587=TLS) |
| `DEEPSEEK_API_KEY` | ✅ | — | DeepSeek API key ([get one here](https://platform.deepseek.com/api_keys)) |
| `DEEPSEEK_BASE_URL` | ❌ | `https://api.deepseek.com` | API base URL |

### SMTP Notes

- **126/163 mail**: Get authorization code at Settings → POP3/SMTP
- **QQ mail**: Get code at Settings → Account → POP3/SMTP service
- **Gmail**: Enable 2FA → App password, or use `smtp.gmail.com:587` with TLS
- The password is **not** your email login password. It's a separate SMTP authorization code.

---

## Data Sources

- **opencli** — fetches from V2EX hot topics, Bluesky trending (public APIs, no cookie/login needed)
- **Bloomberg/BBC/Sina Finance** — news via opencli public endpoints
- **Calendar/seasonal** — built-in topic library in `seasonal_topics.py`

If a news source fails, the script falls back to seasonal topics only (no fake news generated).

---

## Anti-Fake-News

- Real data sources only (no AI hallucination)
- < 5 items from sources → skip AI generation, use fallback
- Specific factual claims explicitly banned in prompts
- Post-processing strips Chinese from English half

---

## Automate with Cron

Every Saturday 17:00 CST:
```
0 17 * * 6 cd /path/to/social-bible && source .env && python3 social_bible_gen.py >> /tmp/social-bible.log 2>&1
```

---

## License

MIT
