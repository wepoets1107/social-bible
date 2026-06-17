# 社牛圣经 / The Social Bible 🦐

A weekly bilingual social cheat sheet. Every Saturday, one email — seven conversation modules, each with one topic, 2-3 conversation angles, and a killer one-liner.

## Philosophy

Knowing what happened ≠ knowing how to talk about it.

This project doesn't aggregate news. It **weaponizes** information for conversation. Each module picks the single best topic of the week and gives you multiple ways to open — whether you're at a dinner party, a coffee chat, or a WeChat group.

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

## Tech Stack

- Python (generation pipeline)
- DeepSeek V4 Flash (content generation)
- opencli (social platform data)
- RSS feeds (Bluesky, V2EX, Bloomberg, BBC, Sina Finance)
- SMTP (email delivery)

## Anti-Fake-News

- Real data sources only (no AI hallucination)
- RSS < 5 items → fallback mode (no AI generation)
- Specific factual claims explicitly banned in prompts
- Post-processing strips Chinese from English half

## Run

```bash
./run.sh
# or
python3 social_bible_gen.py
```
