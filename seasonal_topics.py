"""
冰火岛每日社牛圣经 — 季节性/日历话题库（中英双语）
按月份和日期范围配置，自动判断当周活跃话题
"""
from datetime import datetime, timezone, timedelta

TZ = timezone(timedelta(hours=8))

# ─── 按月份激活的经典话题 ──────────────────────────
SEASONAL_TOPICS = {
    # 固定日期类（节日/赛事/大事件）
    "fixed_date": [
        # 1月
        {"date": "01-01", "title": "元旦新年Flag", "title_en": "New Year Resolutions", "desc": "新年计划、跨年回忆", "heat": "🔥🔥🔥"},
        {"date": "01-28", "title": "春节倒计时", "title_en": "Spring Festival Countdown", "desc": "春运、年货、催婚、红包", "heat": "🔥🔥🔥🔥🔥"},
        # 2月
        {"date": "02-14", "title": "情人节", "title_en": "Valentine's Day", "desc": "约会、送礼、单身", "heat": "🔥🔥🔥🔥"},
        # 3月
        {"date": "03-08", "title": "妇女节", "title_en": "Women's Day", "desc": "性别平等、女性力量", "heat": "🔥🔥🔥"},
        # 4月
        {"date": "04-01", "title": "愚人节", "title_en": "April Fools' Day", "desc": "整蛊趣事、真假新闻", "heat": "🔥🔥"},
        # 5月
        {"date": "05-01", "title": "五一长假", "title_en": "May Day Holiday", "desc": "旅行计划、人从众", "heat": "🔥🔥🔥🔥"},
        # 6月
        {"date": "06-07", "title": "高考", "title_en": "Gaokao (College Entrance Exam)", "desc": "回忆杀、作文题吐槽", "heat": "🔥🔥🔥🔥🔥"},
        {"date": "06-10", "title": "毕业季", "title_en": "Graduation Season", "desc": "答辩、散伙饭、迷茫与憧憬", "heat": "🔥🔥🔥🔥"},
        {"date": "06-18", "title": "618 Shopping Fest", "title_en": "618 Shopping Festival", "desc": "购物清单、凑单技巧、智商税", "heat": "🔥🔥🔥"},
        # 欧洲杯/世界杯（偶数年6-7月，由monthly动态处理，避免与月份话题重复）
        # 9月
        {"date": "09-01", "title": "开学季", "title_en": "Back to School", "desc": "新生入学、暑假作业、校园回忆", "heat": "🔥🔥🔥"},
        {"date": "09-10", "title": "教师节", "title_en": "Teachers' Day", "desc": "印象最深的老师", "heat": "🔥🔥"},
        # 10月
        {"date": "10-01", "title": "国庆长假", "title_en": "National Day Holiday", "desc": "旅行、宅家、朋友圈摄影大赛", "heat": "🔥🔥🔥🔥"},
        {"date": "10-31", "title": "万圣节", "title_en": "Halloween", "desc": "变装、派对、恐怖片", "heat": "🔥🔥🔥"},
        # 11月
        {"date": "11-11", "title": "双十一", "title_en": "Singles' Day / Double 11", "desc": "剁手、尾款人、快递", "heat": "🔥🔥🔥🔥"},
        # 12月
        {"date": "12-24", "title": "圣诞&跨年", "title_en": "Christmas & New Year's Eve", "desc": "年终总结、明年Flag", "heat": "🔥🔥🔥🔥🔥"},
    ],
    # 按月份激活的季节话题
    "monthly": {
        1: [
            {"title": "冬季运动", "title_en": "Winter Sports", "desc": "滑雪、滑冰、温泉", "heat": "🔥🔥🔥"},
            {"title": "冬日夜景", "title_en": "Winter Nightscapes", "desc": "看雪、圣诞灯饰、圣诞市集", "heat": "🔥🔥🔥"},
        ],
        2: [
            {"title": "冬季运动", "title_en": "Winter Sports", "desc": "滑雪季收尾、温泉", "heat": "🔥🔥🔥"},
        ],
        3: [
            {"title": "春暖花开", "title_en": "Spring Blossoms", "desc": "赏樱、踏青、户外烧烤", "heat": "🔥🔥🔥"},
        ],
        4: [
            {"title": "春天户外", "title_en": "Spring Outdoors", "desc": "露营、骑行、放风筝", "heat": "🔥🔥🔥"},
        ],
        5: [
            {"title": "初夏", "title_en": "Early Summer", "desc": "海边、水上运动预告", "heat": "🔥🔥"},
        ],
        6: [
            {"title": "夏天来了", "title_en": "Summer is Here", "desc": "游泳、冲浪、水上乐园", "heat": "🔥🔥🔥🔥"},
            {"title": "端午", "title_en": "Dragon Boat Festival", "desc": "粽子甜咸、龙舟", "heat": "🔥🔥🔥"},
        ],
        7: [
            {"title": "盛夏", "title_en": "Peak Summer", "desc": "游泳、冲浪、潜水、漂流", "heat": "🔥🔥🔥🔥"},
            {"title": "暑假旅行", "title_en": "Summer Travel", "desc": "热门目的地、小众景点", "heat": "🔥🔥🔥🔥"},
            {"title": "音乐节", "title_en": "Music Festivals", "desc": "草莓、迷笛、Tomorrowland", "heat": "🔥🔥🔥"},
            {"title": "啤酒&夜市", "title_en": "Beer & Night Markets", "desc": "夏日烟火气", "heat": "🔥🔥🔥"},
        ],
        8: [
            {"title": "盛夏户外", "title_en": "Summer Outdoors", "desc": "露营、野外徒步、摄影", "heat": "🔥🔥🔥"},
            {"title": "暑假旅行", "title_en": "Summer Travel", "desc": "最后两周的疯狂", "heat": "🔥🔥🔥"},
            {"title": "奥运会年", "title_en": "Olympic Games Year", "desc": "赛事热议、名场面", "heat": "🔥🔥🔥🔥🔥"},
        ],
        9: [
            {"title": "秋高气爽", "title_en": "Crisp Autumn", "desc": "登山、赏秋、骑行", "heat": "🔥🔥🔥"},
            {"title": "秋季养生", "title_en": "Autumn Wellness", "desc": "贴秋膘、润燥", "heat": "🔥🔥"},
        ],
        10: [
            {"title": "金秋", "title_en": "Golden Autumn", "desc": "红叶、大闸蟹、露营", "heat": "🔥🔥🔥🔥"},
            {"title": "万圣变装", "title_en": "Halloween Costumes", "desc": "COS、派对话题", "heat": "🔥🔥🔥"},
        ],
        11: [
            {"title": "初冬", "title_en": "Early Winter", "desc": "火锅、围炉夜话", "heat": "🔥🔥🔥"},
            {"title": "双十一吐槽", "title_en": "Singles' Day Rants", "desc": "凑单、退货、电商生态", "heat": "🔥🔥🔥"},
        ],
        12: [
            {"title": "寒冬", "title_en": "Deep Winter", "desc": "滑雪季开板、温泉、圣诞市集", "heat": "🔥🔥🔥🔥"},
            {"title": "年终总结", "title_en": "Year-End Review", "desc": "年度报告、明年Flag、回顾", "heat": "🔥🔥🔥🔥"},
        ],
    },
    # 常青话题（每周选1-2个，轮换角度）— 中英双语
    "evergreen": [
        {"title": "最近看了什么好片", "title_en": "What movies have you watched lately?", "angles": ["大片", "小众", "纪录片", "老片重看"], "angles_en": ["Blockbusters", "Hidden gems", "Documentaries", "Rewatching classics"]},
        {"title": "在追什么剧/综艺", "title_en": "What shows are you binging?", "angles": ["国产", "英美剧", "日韩", "真人秀"], "angles_en": ["Chinese dramas", "US/UK series", "K-dramas/J-dramas", "Reality shows"]},
        {"title": "最近在读什么书", "title_en": "What are you reading?", "angles": ["非虚构", "小说", "畅销榜", "经典重读"], "angles_en": ["Non-fiction", "Novels", "Bestsellers", "Re-reading classics"]},
        {"title": "周末去哪儿", "title_en": "Weekend plans?", "angles": ["周边游", "探店", "展览", "演出"], "angles_en": ["Day trips", "New spots", "Exhibitions", "Live shows"]},
        {"title": "最近在听什么", "title_en": "What are you listening to?", "angles": ["播客", "新专辑", "老歌翻红", "音乐节"], "angles_en": ["Podcasts", "New albums", "Throwback hits", "Music festivals"]},
        {"title": "健身新花样", "title_en": "New fitness trends?", "angles": ["瑜伽", "攀岩", "拳击", "超慢跑"], "angles_en": ["Yoga", "Rock climbing", "Boxing", "Ultra-slow jogging"]},
        {"title": "什么让你上瘾", "title_en": "What are you obsessed with?", "angles": ["新爱好", "游戏", "收藏", "手作"], "angles_en": ["New hobbies", "Gaming", "Collecting", "DIY"]},
        {"title": "智商税吐槽", "title_en": "Consumer regrets & scams", "angles": ["网红产品", "知识付费", "过度消费"], "angles_en": ["Viral products", "Paid content", "Overconsumption"]},
        {"title": "AI又整了什么活", "title_en": "What's AI up to now?", "angles": ["ChatGPT新玩法", "AI绘画", "职场效率", "伦理争议"], "angles_en": ["New ChatGPT tricks", "AI art", "Workplace productivity", "Ethical debates"]},
    ],
}


def get_this_week_topics():
    """获取本周适用的季节性/常青话题"""
    from datetime import date
    today = date.today()
    month = today.month
    md = today.strftime("%m-%d")

    topics = []

    # 1. 固定日期话题：前7天后3天范围内激活
    for ft in SEASONAL_TOPICS["fixed_date"]:
        if "date" not in ft:
            continue
        fd = ft["date"]
        target = date(today.year, int(fd[:2]), int(fd[3:5]))
        diff = (target - today).days
        if -7 <= diff <= 3:
            topics.append({
                "title": ft["title"],
                "title_en": ft.get("title_en", ft["title"]),
                "desc": ft["desc"],
                "heat": ft.get("heat", "🔥🔥"),
                "type": "节日热点",
                "type_en": "Holiday Hotspot",
                "days_until": diff,
            })

    # 2. 月份话题
    if month in SEASONAL_TOPICS["monthly"]:
        for mt in SEASONAL_TOPICS["monthly"][month]:
            topics.append({
                "title": mt["title"],
                "title_en": mt.get("title_en", mt["title"]),
                "desc": mt["desc"],
                "heat": mt.get("heat", "🔥🔥"),
                "type": "季节话题",
                "type_en": "Seasonal Topic",
                "days_until": 0,
            })

    # 3. 动态足球大赛（6-7月）
    if month in (6, 7):
        fb = get_football_event()
        if fb:
            topics.append(fb)

    return topics


def get_football_event():
    """根据年份返回当前夏季的足球大赛（世界杯或欧洲杯）"""
    from datetime import date
    year = date.today().year
    # 世界杯：2026, 2030, 2034... → year % 4 == 2
    # 欧洲杯：2024, 2028, 2032... → year % 4 == 0
    if year % 4 == 2:
        world_cup_hosts = {2026: "美加墨", 2030: "西葡摩+南美", 2034: "沙特"}
        hosts = world_cup_hosts.get(year, "")
        host_str = f"（{hosts}）" if hosts else ""
        return {
            "title": f"世界杯 {host_str}",
            "title_en": f"World Cup {year}",
            "desc": "小组赛揭幕、爆冷预测、冠军猜想、熬夜看球",
            "heat": "🔥🔥🔥🔥🔥",
            "type": "季节话题",
            "type_en": "Seasonal Topic",
            "days_until": 0,
        }
    elif year % 4 == 0:
        return {
            "title": f"欧洲杯",
            "title_en": f"Euro Cup {year}",
            "desc": "豪门恩怨、冷门预测、熬夜看球",
            "heat": "🔥🔥🔥🔥🔥",
            "type": "季节话题",
            "type_en": "Seasonal Topic",
            "days_until": 0,
        }
    return None


def get_evergreen_pick(week_offset=0):
    """轮选常青话题（每周换一个角度）"""
    from datetime import date
    week_number = date.today().isocalendar()[1] + week_offset
    idx = week_number % len(SEASONAL_TOPICS["evergreen"])
    pick = SEASONAL_TOPICS["evergreen"][idx]
    angle_idx = week_number % len(pick["angles"])
    return {
        "title": pick["title"],
        "title_en": pick.get("title_en", pick["title"]),
        "angle": pick["angles"][angle_idx],
        "angle_en": pick.get("angles_en", pick["angles"])[angle_idx % len(pick.get("angles_en", pick["angles"]))],
        "type": "经典话题",
        "type_en": "Classic Topic",
    }
