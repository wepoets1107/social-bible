"""
冰火岛每日社牛圣经 — 季节性/日历话题库（中英双语）
按月份和日期范围配置，自动判断当周活跃话题
常青话题池 160+ 个，按年积日轮选，保证日更不重复
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
    # 常青话题（每天轮选一个，160+ 保证每轮不重复）— 16类别
    "evergreen": [
        # ===== 1. 娱乐·影视·音乐 (10) =====
        {"title": "最近看了什么好片", "title_en": "What movies have you watched lately?", "angles": ["大片", "小众", "纪录片", "老片重看"], "angles_en": ["Blockbusters", "Hidden gems", "Documentaries", "Rewatching classics"]},
        {"title": "在追什么剧/综艺", "title_en": "What shows are you binging?", "angles": ["国产", "英美剧", "日韩", "真人秀"], "angles_en": ["Chinese dramas", "US/UK series", "K-dramas/J-dramas", "Reality shows"]},
        {"title": "最近听了什么好歌", "title_en": "New music discoveries", "angles": ["新专辑", "老歌翻红", "现场演出", "歌单分享"], "angles_en": ["New albums", "Throwback hits", "Live shows", "Playlist sharing"]},
        {"title": "最近在读什么书", "title_en": "What are you reading?", "angles": ["非虚构", "小说", "畅销榜", "经典重读"], "angles_en": ["Non-fiction", "Novels", "Bestsellers", "Re-reading classics"]},
        {"title": "播客推荐", "title_en": "Podcast picks", "angles": ["知识类", "闲聊类", "故事类", "商业类"], "angles_en": ["Educational", "Casual chat", "Storytelling", "Business"]},
        {"title": "动漫/漫画", "title_en": "Anime & manga", "angles": ["热血番", "治愈番", "国产动画", "老番重温"], "angles_en": ["Action", "Slice of life", "Chinese animation", "Rewatching classics"]},
        {"title": "游戏时间", "title_en": "Gaming", "angles": ["手游", "PC/主机", "独立游戏", "怀旧游戏"], "angles_en": ["Mobile games", "PC/console", "Indie games", "Retro gaming"]},
        {"title": "B站/抖音刷到什么", "title_en": "What's trending on video platforms?", "angles": ["UP主", "短视频", "知识区", "搞笑区"], "angles_en": ["Creators", "Short videos", "Educational", "Comedy"]},
        {"title": "网红/博主", "title_en": "Influencers & creators", "angles": ["翻车", "种草", "人设", "带货"], "angles_en": ["Cancel culture", "Product push", "Persona", "Live selling"]},
        {"title": "追星吗", "title_en": "Fan culture", "angles": ["演唱会", "粉丝经济", "塌房", "饭圈"], "angles_en": ["Concerts", "Fan economy", "Scandals", "Fandom"]},
        # ===== 2. 美食 (10) =====
        {"title": "最难忘的一顿饭", "title_en": "Memorable meals", "angles": ["家常", "旅行中", "约会", "一个人吃"], "angles_en": ["Home cooking", "While traveling", "On a date", "Dining solo"]},
        {"title": "深夜放毒", "title_en": "Midnight snacks", "angles": ["泡面", "外卖", "路边摊", "冰箱有什么"], "angles_en": ["Instant noodles", "Delivery", "Street food", "Fridge raid"]},
        {"title": "家乡味道", "title_en": "Hometown flavors", "angles": ["妈妈做的菜", "童年零食", "地域特色", "在国外做中餐"], "angles_en": ["Mom's cooking", "Childhood snacks", "Regional specialties", "Cooking Chinese abroad"]},
        {"title": "网红餐厅打卡", "title_en": "Trendy restaurants", "angles": ["排队值不值", "拍照VS味道", "新店测评", "隐藏菜单"], "angles_en": ["Worth the queue?", "Looks vs taste", "New spot review", "Secret menu"]},
        {"title": "自己做饭", "title_en": "Home cooking", "angles": ["翻车现场", "拿手菜", "便当党", "懒人食谱"], "angles_en": ["Kitchen fails", "Signature dish", "Lunchbox crew", "Lazy recipes"]},
        {"title": "咖啡/奶茶上瘾", "title_en": "Coffee & bubble tea", "angles": ["每天几杯", "小众咖啡店", "奶茶新花样", "减糖斗争"], "angles_en": ["Cups per day", "Hidden coffee spots", "New tea trends", "Sugar battle"]},
        {"title": "喝酒文化", "title_en": "Drinking culture", "angles": ["精酿", "清吧VS夜店", "酒桌规矩", "一个人喝"], "angles_en": ["Craft beer", "Bar vs club", "Table etiquette", "Drinking solo"]},
        {"title": "烧烤/火锅", "title_en": "BBQ & hotpot", "angles": ["蘸料哲学", "食材争议", "南北差异", "社交属性"], "angles_en": ["Dipping sauce", "Ingredient debate", "North vs south", "Social bonding"]},
        {"title": "吃不腻的东西", "title_en": "Foods you never get tired of", "angles": ["碳水快乐", "零食", "comfort food", "万能酱料"], "angles_en": ["Carbs joy", "Snacks", "Comfort food", "Universal sauce"]},
        {"title": "下馆子还是外卖", "title_en": "Dine out vs delivery", "angles": ["省钱", "卫生", "体验感", "选择困难"], "angles_en": ["Saving money", "Hygiene", "Experience", "Decision fatigue"]},
        # ===== 3. 旅行·户外 (10) =====
        {"title": "旅行的意义", "title_en": "Travel stories", "angles": ["小众目的地", "穷游vs奢游", "独自旅行", "旅行搭子"], "angles_en": ["Hidden gems", "Budget vs luxury", "Solo travel", "Travel buddies"]},
        {"title": "周末去哪儿", "title_en": "Weekend plans?", "angles": ["周边游", "探店", "展览", "演出"], "angles_en": ["Day trips", "New spots", "Exhibitions", "Live shows"]},
        {"title": "旅行翻车现场", "title_en": "Travel disasters", "angles": ["航班延误", "丢行李", "语言不通", "被坑"], "angles_en": ["Flight delays", "Lost luggage", "Language barriers", "Getting scammed"]},
        {"title": "住酒店", "title_en": "Hotel experiences", "angles": ["青旅", "五星", "民宿", "奇葩酒店"], "angles_en": ["Hostels", "Luxury", "B&Bs", "Quirky hotels"]},
        {"title": "露营/户外", "title_en": "Camping & outdoors", "angles": ["装备", "小白入门", "夜晚体验", "坑"], "angles_en": ["Gear", "Beginner tips", "Night experience", "Pitfalls"]},
        {"title": "自驾游", "title_en": "Road trips", "angles": ["路线推荐", "路上歌单", "加油站美食", "房车体验"], "angles_en": ["Route tips", "Road trip playlist", "Gas station food", "RV life"]},
        {"title": "飞机/高铁/自驾", "title_en": "Travel modes", "angles": ["出行选择", "延误焦虑", "火车风景", "飞行体验"], "angles_en": ["Mode choice", "Delay anxiety", "Train scenery", "Flying experience"]},
        {"title": "旅行纪念品", "title_en": "Souvenirs", "angles": ["冰箱贴", "明信片", "当地特产", "智商税"], "angles_en": ["Magnets", "Postcards", "Local products", "Rip-offs"]},
        {"title": "想去但还没去的地方", "title_en": "Dream destinations", "angles": ["国内", "国外", "一个人去", "和谁去"], "angles_en": ["Domestic", "International", "Going solo", "Travel companions"]},
        {"title": "黄金周/长假体验", "title_en": "Holiday travel", "angles": ["人从众", "宅家", "反向旅游", "错峰秘诀"], "angles_en": ["Crowds", "Staying home", "Reverse tourism", "Off-peak tips"]},
        # ===== 4. 工作·职业 (10) =====
        {"title": "职场潜规则", "title_en": "Workplace unwritten rules", "angles": ["向上管理", "站队", "加班文化", "办公室政治"], "angles_en": ["Managing up", "Taking sides", "Overtime culture", "Office politics"]},
        {"title": "想辞职吗", "title_en": "Thinking of quitting?", "angles": ["裸辞", "骑驴找马", "gap year", "创业冲动"], "angles_en": ["Quitting without backup", "Job hunting", "Gap year", "Entrepreneurial itch"]},
        {"title": "面试故事", "title_en": "Interview stories", "angles": ["奇葩面试", "压力面", "谈薪", "被拒经历"], "angles_en": ["Weird interviews", "Stress tests", "Salary negotiation", "Rejection stories"]},
        {"title": "远程办公", "title_en": "Remote work", "angles": ["效率", "孤独", "时差", "WFH装备"], "angles_en": ["Productivity", "Loneliness", "Time zones", "WFH setup"]},
        {"title": "同事关系", "title_en": "Coworker relationships", "angles": ["合得来", "讨厌的同事", "离职后还联系吗", "办公室友谊"], "angles_en": ["Good chemistry", "Difficult coworkers", "Keeping in touch", "Work friendships"]},
        {"title": "35岁危机", "title_en": "Mid-career crisis", "angles": ["互联网", "体制内", "转行", "年龄焦虑"], "angles_en": ["Tech industry", "Government jobs", "Career change", "Age anxiety"]},
        {"title": "加班文化", "title_en": "Overtime culture", "angles": ["996", "摸鱼", "无效加班", "work-life balance"], "angles_en": ["996 culture", "Slacking off", "Useless overtime", "Work-life balance"]},
        {"title": "开会", "title_en": "Meeting culture", "angles": ["废话连篇", "站着开会", "远程会", "会前准备什么"], "angles_en": ["Pointless meetings", "Stand-ups", "Remote calls", "Meeting prep"]},
        {"title": "第一份工作", "title_en": "First job", "angles": ["踩坑", "成长", "老板", "工资低"], "angles_en": ["Mistakes", "Growth", "Boss", "Low salary"]},
        {"title": "自由职业/数字游民", "title_en": "Freelancing & digital nomads", "angles": ["收入不稳定", "自律", "社保", "值得吗"], "angles_en": ["Unstable income", "Self-discipline", "Insurance", "Is it worth it?"]},
        # ===== 5. 金钱·消费 (10) =====
        {"title": "副业搞钱", "title_en": "Side hustles", "angles": ["自媒体", "接单平台", "投资理财", "技能变现"], "angles_en": ["Content creation", "Freelance platforms", "Investing", "Skill monetization"]},
        {"title": "租房还是买房", "title_en": "Rent vs buy", "angles": ["一线城市", "二线", "房贷焦虑", "自由vs安定"], "angles_en": ["1st-tier cities", "2nd-tier", "Mortgage anxiety", "Freedom vs stability"]},
        {"title": "存钱还是享受", "title_en": "Save vs enjoy", "angles": ["月光族", "强制储蓄", "消费主义", "FIRE运动"], "angles_en": ["Living paycheck to paycheck", "Forced saving", "Consumerism", "FIRE movement"]},
        {"title": "记账习惯", "title_en": "Budget tracking", "angles": ["记账APP", "预算管理", "冲动消费", "省钱技巧"], "angles_en": ["Budgeting apps", "Budget management", "Impulse buying", "Saving tips"]},
        {"title": "保险买不买", "title_en": "Insurance", "angles": ["重疾", "医疗", "养老", "踩坑经历"], "angles_en": ["Critical illness", "Medical", "Pension", "Scam stories"]},
        {"title": "信用卡/花呗", "title_en": "Credit cards & debt", "angles": ["额度焦虑", "积分羊毛", "分期陷阱", "逾期"], "angles_en": ["Credit limits", "Rewards", "Installment traps", "Late payments"]},
        {"title": "二手交易", "title_en": "Second-hand market", "angles": ["闲鱼经验", "以旧换新", "捡漏", "卖不出去"], "angles_en": ["Xianyu tips", "Trade-ins", "Deal hunting", "Unsold items"]},
        {"title": "税和钱", "title_en": "Taxes & salary", "angles": ["个税", "年终奖怎么发", "五险一金", "到手工资"], "angles_en": ["Income tax", "Bonuses", "Social insurance", "Take-home pay"]},
        {"title": "奢侈品买不买", "title_en": "Luxury goods", "angles": ["包包", "手表", "中古", "平替"], "angles_en": ["Bags", "Watches", "Vintage", "Dupe culture"]},
        {"title": "给父母/长辈花钱", "title_en": "Spending on parents", "angles": ["礼物", "红包", "旅游", "体检"], "angles_en": ["Gifts", "Red packets", "Travel", "Health check-ups"]},
        # ===== 6. 社交·关系 (10) =====
        {"title": "独处vs社交", "title_en": "Alone time vs social time", "angles": ["I人E人", "社交充电", "独居", "周末安排"], "angles_en": ["Introvert vs extrovert", "Social battery", "Living alone", "Weekend plans"]},
        {"title": "社死现场", "title_en": "Embarrassing moments", "angles": ["职场", "公共场合", "聊天翻车", "认错人"], "angles_en": ["At work", "In public", "Chat fails", "Mistaken identity"]},
        {"title": "和父母沟通", "title_en": "Talking to parents", "angles": ["催婚", "代沟", "报喜不报忧", "教父母用手机"], "angles_en": ["Marriage pressure", "Generation gap", "Good news only", "Teaching tech"]},
        {"title": "发小和老朋友", "title_en": "Childhood friends", "angles": ["多久联系一次", "变了没变", "借钱", "渐行渐远"], "angles_en": ["How often?", "Same or different?", "Lending money", "Drifting apart"]},
        {"title": "群聊文化", "title_en": "Group chat culture", "angles": ["家族群", "工作群", "同学群", "消息免打扰"], "angles_en": ["Family groups", "Work chats", "Class groups", "Muted forever"]},
        {"title": "朋友圈发什么", "title_en": "Moments strategy", "angles": ["三天可见", "晒娃", "旅行九宫格", "分组可见"], "angles_en": ["3-day visibility", "Baby photos", "Travel grids", "Circle policies"]},
        {"title": "饭局社交", "title_en": "Dinner party etiquette", "angles": ["敬酒", "谁买单", "冷场救场", "带什么去"], "angles_en": ["Toasting", "Who pays?", "Breaking silence", "What to bring"]},
        {"title": "邻居关系", "title_en": "Neighbor relationships", "angles": ["噪音", "电梯里聊什么", "帮忙收快递", "老死不相往来"], "angles_en": ["Noise", "Elevator chat", "Package help", "Keep to yourself"]},
        {"title": "被拉黑/拉黑别人", "title_en": "Blocking people", "angles": ["前任", "微商", "杠精", "绝交"], "angles_en": ["Exes", "WeChat sellers", "Trolls", "Ending friendships"]},
        {"title": "如何拒绝别人", "title_en": "How to say no", "angles": ["借钱", "帮忙", "聚会邀请", "工作要求"], "angles_en": ["Lending money", "Favors", "Party invites", "Work requests"]},
        # ===== 7. 生活·日常 (10) =====
        {"title": "通勤路上在干嘛", "title_en": "Commute routines", "angles": ["播客", "听歌", "看书", "发呆"], "angles_en": ["Podcasts", "Music", "Reading", "Zoning out"]},
        {"title": "睡得好吗", "title_en": "Sleep habits", "angles": ["失眠", "早起挑战", "午睡文化", "睡前仪式"], "angles_en": ["Insomnia", "Early rising", "Napping culture", "Bedtime rituals"]},
        {"title": "断舍离", "title_en": "Decluttering", "angles": ["扔东西", "极简主义", "收纳", "二手卖掉"], "angles_en": ["Throwing away", "Minimalism", "Storage hacks", "Selling second-hand"]},
        {"title": "最治愈的一件小事", "title_en": "Small joys", "angles": ["宅家", "散步", "做饭", "整理"], "angles_en": ["Staying in", "Walking", "Cooking", "Organizing"]},
        {"title": "手机里最舍不得删的照片", "title_en": "Photos you'll never delete", "angles": ["家人", "旅行", "美食", "宠物"], "angles_en": ["Family", "Travel", "Food", "Pets"]},
        {"title": "养宠物那些事", "title_en": "Pet stories", "angles": ["猫vs狗", "养宠成本", "云吸宠", "宠物医疗"], "angles_en": ["Cats vs dogs", "Pet costs", "Virtual pets", "Pet healthcare"]},
        {"title": "健身新花样", "title_en": "New fitness trends?", "angles": ["瑜伽", "攀岩", "拳击", "超慢跑"], "angles_en": ["Yoga", "Rock climbing", "Boxing", "Ultra-slow jogging"]},
        {"title": "什么让你上瘾", "title_en": "What are you obsessed with?", "angles": ["新爱好", "游戏", "收藏", "手作"], "angles_en": ["New hobbies", "Gaming", "Collecting", "DIY"]},
        {"title": "心情不好怎么办", "title_en": "Bad day remedies", "angles": ["吃甜的", "运动", "找人聊", "一个人待着"], "angles_en": ["Sweet treats", "Exercise", "Talking it out", "Alone time"]},
        {"title": "拖延症", "title_en": "Procrastination", "angles": ["deadline是第一生产力", "番茄钟", "为什么拖", "救了你的拖延"], "angles_en": ["Last-minute rush", "Pomodoro", "Why we procrastinate", "Saves from procrastination"]},
        # ===== 8. 科技·数码 (10) =====
        {"title": "AI又整了什么活", "title_en": "What's AI up to now?", "angles": ["ChatGPT新玩法", "AI绘画", "职场效率", "伦理争议"], "angles_en": ["New ChatGPT tricks", "AI art", "Workplace productivity", "Ethical debates"]},
        {"title": "换手机吗", "title_en": "Phone upgrade?", "angles": ["苹果vs安卓", "折叠屏", "用多久换", "为什么换不动了"], "angles_en": ["iPhone vs Android", "Foldables", "Upgrade cycle", "Upgrade fatigue"]},
        {"title": "APP推荐/吐槽", "title_en": "App recommendations & rants", "angles": ["最近发现的好APP", "越来越臃肿", "付费订阅", "替代品"], "angles_en": ["New finds", "Feature bloat", "Subscription fatigue", "Alternatives"]},
        {"title": "电脑配置", "title_en": "PC specs & setup", "angles": ["Mac vs Windows", "装机", "外设", "够用就好"], "angles_en": ["Mac vs Windows", "Building PCs", "Peripherals", "Good enough"]},
        {"title": "充电焦虑", "title_en": "Battery anxiety", "angles": ["快充", "无线充", "共享充电宝", "续航比拼"], "angles_en": ["Fast charging", "Wireless charging", "Power banks", "Battery race"]},
        {"title": "智能家居", "title_en": "Smart home", "angles": ["音箱", "灯", "扫地机器人", "值不值"], "angles_en": ["Speakers", "Lights", "Robot vacuums", "Worth it?"]},
        {"title": "密码管理", "title_en": "Password management", "angles": ["记不住", "全用同一个", "两步验证", "密码管理器"], "angles_en": ["Can't remember", "Same password", "2FA", "Password managers"]},
        {"title": "云存储/备份", "title_en": "Cloud storage & backup", "angles": ["iCloud", "网盘", "NAS", "数据丢了"], "angles_en": ["iCloud", "Cloud drives", "NAS", "Data loss stories"]},
        {"title": "购物被算法推荐", "title_en": "Algorithmic shopping", "angles": ["精准推送", "信息茧房", "杀熟", "冲动消费"], "angles_en": ["Targeted ads", "Filter bubbles", "Price discrimination", "Impulse buys"]},
        {"title": "数字断舍离", "title_en": "Digital declutter", "angles": ["删APP", "手机使用时间", "退出无用的群", "戒社交媒体"], "angles_en": ["Deleting apps", "Screen time", "Leaving useless groups", "Social media detox"]},
        # ===== 9. 成长·心理 (10) =====
        {"title": "小时候vs长大后", "title_en": "Childhood vs adulthood", "angles": ["童年回忆", "长大幻灭", "心态变化", "最想回到哪一天"], "angles_en": ["Childhood memories", "Adulting letdowns", "Mindset shifts", "One day to relive"]},
        {"title": "人生导师", "title_en": "Life mentors", "angles": ["老师", "老板", "长辈", "书里的人物"], "angles_en": ["Teachers", "Bosses", "Elders", "Fictional characters"]},
        {"title": "后悔的事", "title_en": "Regrets", "angles": ["没学什么", "没说什么", "选错了", "如果能重来"], "angles_en": ["Not learning", "Not saying", "Wrong choices", "If I could go back"]},
        {"title": "焦虑来源", "title_en": "Sources of anxiety", "angles": ["同龄人压力", "年龄", "钱", "健康"], "angles_en": ["Peer pressure", "Age", "Money", "Health"]},
        {"title": "自信从哪来", "title_en": "Where confidence comes from", "angles": ["专业能力", "外表", "家庭", "经历过失败"], "angles_en": ["Expertise", "Appearance", "Family", "Surviving failure"]},
        {"title": "自卑时刻", "title_en": "Insecurity moments", "angles": ["跟别人比", "被否定", "能力不足", "外貌焦虑"], "angles_en": ["Comparing", "Being rejected", "Impostor syndrome", "Body image"]},
        {"title": "犯错之后", "title_en": "After making mistakes", "angles": ["道歉", "补救", "原谅自己", "长记性"], "angles_en": ["Apologizing", "Fixing it", "Self-forgiveness", "Learning"]},
        {"title": "最感谢的人", "title_en": "People you're grateful for", "angles": ["家人", "朋友", "陌生人", "曾经的自己"], "angles_en": ["Family", "Friends", "Strangers", "Past self"]},
        {"title": "人生转折点", "title_en": "Life turning points", "angles": ["选择", "意外", "贵人", "放弃"], "angles_en": ["Decisions", "Unexpected events", "Helpers", "Letting go"]},
        {"title": "写给十年后的自己", "title_en": "Letter to future self", "angles": ["职业", "家庭", "想成为什么样的人", "想记住什么"], "angles_en": ["Career", "Family", "Who you want to be", "What to remember"]},
        # ===== 10. 健康·养生 (10) =====
        {"title": "体检报告", "title_en": "Health check scares", "angles": ["不敢看", "结节", "指标异常", "改生活习惯"], "angles_en": ["Too scared to look", "Nodules", "Abnormal results", "Lifestyle changes"]},
        {"title": "中医vs西医", "title_en": "Chinese vs Western medicine", "angles": ["感冒怎么治", "调理", "中药副作用", "信哪个"], "angles_en": ["Cold treatment", "Preventive care", "Herbal side effects", "Which to trust?"]},
        {"title": "脱发焦虑", "title_en": "Hair loss anxiety", "angles": ["发际线", "植发", "米诺地尔", "接受它"], "angles_en": ["Hairline", "Transplants", "Minoxidil", "Acceptance"]},
        {"title": "减肥/健身故事", "title_en": "Weight loss & fitness", "angles": ["成功", "反弹", "节食还是运动", "身体变化"], "angles_en": ["Success", "Yo-yo dieting", "Diet vs exercise", "Body changes"]},
        {"title": "保健品吃不吃", "title_en": "Supplements", "angles": ["维生素", "蛋白粉", "智商税", "医生的建议"], "angles_en": ["Vitamins", "Protein powder", "Scams", "Doctor's advice"]},
        {"title": "久坐/腰椎/颈椎", "title_en": "Sedentary health", "angles": ["腰疼", "颈椎病", "人体工学椅", "站起来走走"], "angles_en": ["Back pain", "Neck issues", "Ergonomic chairs", "Stand up and walk"]},
        {"title": "视力/眼睛", "title_en": "Eye health", "angles": ["近视手术", "干眼症", "蓝光眼镜有用吗", "护眼习惯"], "angles_en": ["LASIK", "Dry eyes", "Blue light glasses", "Eye care habits"]},
        {"title": "牙齿/口腔", "title_en": "Dental health", "angles": ["洗牙", "智齿", "美白", "看牙贵"], "angles_en": ["Teeth cleaning", "Wisdom teeth", "Whitening", "Dental costs"]},
        {"title": "心理健康", "title_en": "Mental health", "angles": ["心理咨询", "抑郁症", "情绪管理", "自我关怀"], "angles_en": ["Therapy", "Depression", "Emotional regulation", "Self-care"]},
        {"title": "疫苗接种", "title_en": "Vaccination", "angles": ["流感疫苗", "HPV", "带状疱疹", "犹豫"], "angles_en": ["Flu shots", "HPV", "Shingles", "Hesitancy"]},
        # ===== 11. 教育·学习 (10) =====
        {"title": "学英语", "title_en": "Learning English", "angles": ["方法", "坚持不下去", "看美剧", "用不上"], "angles_en": ["Methods", "Can't stick with it", "Watching shows", "No real use"]},
        {"title": "考研/考公/留学", "title_en": "Exam mania", "angles": ["为什么考", "卷吗", "值得吗", "没考上后来呢"], "angles_en": ["Why take them?", "Competition", "Worth it?", "Life after failing"]},
        {"title": "线上课程/网课", "title_en": "Online courses", "angles": ["买了不上", "哪个平台好", "免费资源", "学完的成就感"], "angles_en": ["Bought but didn't take", "Best platforms", "Free resources", "Finishing feels good"]},
        {"title": "学一门新技能", "title_en": "Learning new skills", "angles": ["什么技能", "时间不够", "为什么学", "AI时代学什么"], "angles_en": ["Which skill?", "No time", "Why learn?", "What to learn in AI era?"]},
        {"title": "教育孩子方式", "title_en": "Parenting & education", "angles": ["鸡娃", "快乐教育", "兴趣班", "内卷"], "angles_en": ["Tiger parenting", "Happy education", "Extracurriculars", "Rat race"]},
        {"title": "学历重要吗", "title_en": "Is degree important?", "angles": ["第一学历", "名校光环", "能力vs文凭", "非全"], "angles_en": ["First degree", "Prestige", "Ability vs diploma", "Part-time degrees"]},
        {"title": "最受益的一堂课", "title_en": "Most valuable lesson", "angles": ["学校的", "生活的", "别人的教训", "自己悟出来的"], "angles_en": ["From school", "From life", "Others' mistakes", "Self-realized"]},
        {"title": "自学能力", "title_en": "Self-learning", "angles": ["怎么学", "资源在哪", "坚持", "遇到不懂怎么办"], "angles_en": ["How to learn", "Where to find resources", "Staying consistent", "When stuck"]},
        {"title": "应试教育回忆", "title_en": "Exam system memories", "angles": ["高考", "月考排名", "作弊故事", "走出考场"], "angles_en": ["Gaokao", "Monthly rankings", "Cheating stories", "Walking out of the exam hall"]},
        {"title": "知识改变命运吗", "title_en": "Does knowledge change destiny?", "angles": ["身边的故事", "阶层流动", "寒门", "读书无用论"], "angles_en": ["Real stories", "Social mobility", "Humble beginnings", "Is school useless?"]},
        # ===== 12. 家乡·家庭 (10) =====
        {"title": "家乡vs城市", "title_en": "Hometown vs city life", "angles": ["逃离北上广", "返乡", "乡愁", "城市孤独"], "angles_en": ["Leaving big cities", "Moving back", "Nostalgia", "Urban loneliness"]},
        {"title": "过年回家", "title_en": "Going home for holidays", "angles": ["抢票", "催婚催生", "同学聚会", "走亲戚"], "angles_en": ["Ticket rush", "Marriage pressure", "Class reunions", "Family visits"]},
        {"title": "父母变老了", "title_en": "Parents getting older", "angles": ["发现", "陪伴时间", "健康", "养老选择"], "angles_en": ["Realizing it", "Time together", "Health", "Elderly care"]},
        {"title": "原生家庭", "title_en": "Family of origin", "angles": ["影响", "和解", "摆脱", "理解"], "angles_en": ["Influence", "Reconciliation", "Breaking away", "Understanding"]},
        {"title": "兄弟姐妹", "title_en": "Siblings", "angles": ["独生子女", "互相照顾", "争宠", "长大后关系"], "angles_en": ["Only child", "Taking care", "Competing", "Adult relationships"]},
        {"title": "结婚还是不婚", "title_en": "Marriage or not?", "angles": ["催婚压力", "恐婚", "婚姻好处", "不婚的底气"], "angles_en": ["Pressure to marry", "Fear of marriage", "Benefits", "Confidence to stay single"]},
        {"title": "要不要孩子", "title_en": "To have kids or not?", "angles": ["生育焦虑", "养娃成本", "丁克", "二胎"], "angles_en": ["Fertility anxiety", "Cost of raising kids", "DINK", "Second child"]},
        {"title": "家族故事", "title_en": "Family stories", "angles": ["爷爷奶奶", "老照片", "家谱", "家风"], "angles_en": ["Grandparents", "Old photos", "Family tree", "Family values"]},
        {"title": "年夜饭/团圆", "title_en": "Reunion dinners", "angles": ["谁做饭", "吃什么", "酒桌规矩", "远程团圆"], "angles_en": ["Who cooks?", "What's on the table?", "Table rules", "Virtual reunions"]},
        {"title": "离开家的那天", "title_en": "The day you left home", "angles": ["上大学", "工作", "出国", "父母送你"], "angles_en": ["Going to college", "Starting work", "Going abroad", "Parents seeing you off"]},
        # ===== 13. 城市·出行 (10) =====
        {"title": "共享单车/电动车", "title_en": "Ride-sharing & e-bikes", "angles": ["涨价了吗", "乱停", "电动车新规", "最后一公里"], "angles_en": ["Price hikes", "Parking chaos", "New e-bike rules", "Last mile"]},
        {"title": "堵车/限行", "title_en": "Traffic & restrictions", "angles": ["北京/上海", "车牌摇号", "为什么不买车", "坐地铁"], "angles_en": ["Beijing/Shanghai", "License plate lottery", "Why no car?", "Taking the subway"]},
        {"title": "外卖延迟/配送", "title_en": "Delivery delays", "angles": ["雨天", "催单", "给不给差评", "小哥不容易"], "angles_en": ["Rainy days", "Chasing orders", "To rate or not?", "Delivery riders"]},
        {"title": "菜市场vs生鲜APP", "title_en": "Wet markets vs grocery apps", "angles": ["价格", "新鲜度", "体验感", "哪个方便"], "angles_en": ["Price", "Freshness", "Experience", "Convenience"]},
        {"title": "快递/包裹", "title_en": "Package delivery", "angles": ["丢件", "驿站", "快递柜", "退货"], "angles_en": ["Lost packages", "Collection points", "Lockers", "Returns"]},
        {"title": "小区/邻里", "title_en": "Neighborhood life", "angles": ["物业", "业委会", "团购群", "电梯里遇到"], "angles_en": ["Property management", "Owners committee", "Group buying", "Elevator encounters"]},
        {"title": "搬家经历", "title_en": "Moving experiences", "angles": ["找房", "搬家师傅", "东西太多", "新家适应期"], "angles_en": ["Apartment hunting", "Movers", "Too much stuff", "Settling in"]},
        {"title": "便利店/超市", "title_en": "Convenience stores & supermarkets", "angles": ["全家vs7-11", "深夜", "一人食", "超市自有品牌"], "angles_en": ["FamilyMart vs 7-11", "Late night", "Solo meals", "Store brands"]},
        {"title": "公园/城市绿地", "title_en": "Parks & green spaces", "angles": ["散步", "跑步", "野餐", "发呆"], "angles_en": ["Walking", "Running", "Picnics", "Zoning out"]},
        {"title": "城市地标/打卡", "title_en": "City landmarks", "angles": ["游客vs本地人", "多久没去过了", "第一次去", "推荐给朋友"], "angles_en": ["Tourists vs locals", "When did you last go?", "First time", "Recommending to friends"]},
        # ===== 14. 文化·观察 (10) =====
        {"title": "南北差异", "title_en": "North vs south China", "angles": ["饮食", "性格", "气候", "刻板印象"], "angles_en": ["Food", "Personality", "Climate", "Stereotypes"]},
        {"title": "方言/口音", "title_en": "Dialects & accents", "angles": ["会说不会写", "普通话vs方言", "地方梗", "外地人听不懂"], "angles_en": ["Speak but can't write", "Mandarin vs dialect", "Local humor", "Outsiders lost"]},
        {"title": "流行语/梗", "title_en": "Internet slang & memes", "angles": ["最近在说", "梗的来源", "用错了", "过时了"], "angles_en": ["Trending now", "Origin story", "Using it wrong", "So last year"]},
        {"title": "国潮/传统文化", "title_en": "Chinese trends & tradition", "angles": ["汉服", "新中式", "博物馆热", "马面裙"], "angles_en": ["Hanfu", "Neo-Chinese style", "Museum boom", "Horse-face skirts"]},
        {"title": "演唱会/音乐节", "title_en": "Concerts & festivals", "angles": ["买票难", "现场体验", "音乐节穿搭", "哪个值得去"], "angles_en": ["Ticket wars", "Live experience", "Festival fashion", "Which ones are worth it?"]},
        {"title": "电影评分", "title_en": "Movie ratings", "angles": ["豆瓣评分", "烂片高分的", "被低估的", "打分标准"], "angles_en": ["Douban scores", "Overrated", "Underrated", "Rating criteria"]},
        {"title": "综艺套路", "title_en": "Reality show patterns", "angles": ["剧本感", "CP炒作", "冲突剪辑", "为什么还看"], "angles_en": ["Scripted feel", "Shipping", "Drama editing", "Why we still watch"]},
        {"title": "短视频刷多了", "title_en": "Short video addiction", "angles": ["时间黑洞", "注意力下降", "信息碎片", "戒断方法"], "angles_en": ["Time sink", "Attention span", "Information fragmentation", "Detox methods"]},
        {"title": "文化差异", "title_en": "Cultural differences", "angles": ["出国才发现的", "西方vs东方", "刻板印象", "适应过程"], "angles_en": ["Noticed abroad", "East vs West", "Stereotypes", "Adaptation"]},
        {"title": "怀旧/老物件", "title_en": "Nostalgia & old things", "angles": ["全城消失的80/90后记忆", "老照片", "童年玩具", "以前的东西质量好"], "angles_en": ["90s nostalgia", "Old photos", "Childhood toys", "Things were built better"]},
        # ===== 15. 社会·敏感 (10) =====
        {"title": "性别平等", "title_en": "Gender equality", "angles": ["职场", "家庭分工", "婚恋市场", "刻板印象"], "angles_en": ["Workplace", "Family roles", "Dating market", "Stereotypes"]},
        {"title": "贫富差距", "title_en": "Wealth gap", "angles": ["身边的故事", "机会不平等", "心态", "怎么看"], "angles_en": ["Real stories", "Unequal opportunities", "Mindset", "Perspective"]},
        {"title": "网络暴力", "title_en": "Online harassment", "angles": ["键盘侠", "被网暴经历", "人肉", "如何应对"], "angles_en": ["Keyboard warriors", "Being targeted", "Doxxing", "How to respond"]},
        {"title": "信息茧房", "title_en": "Information bubbles", "angles": ["只看自己想看的", "算法推荐", "跨出舒适区", "独立思考"], "angles_en": ["Confirmation bias", "Algorithm feeds", "Step out", "Critical thinking"]},
        {"title": "内卷/躺平", "title_en": "Involution vs lying flat", "angles": ["职场", "教育", "生活", "真躺还是说说"], "angles_en": ["Workplace", "Education", "Lifestyle", "Real or just talk?"]},
        {"title": "消费降级", "title_en": "Trading down", "angles": ["平替", "不买了", "省钱妙招", "生活质量变化"], "angles_en": ["Dupe culture", "Stopping spending", "Saving tricks", "Quality of life changes"]},
        {"title": "食品安全", "title_en": "Food safety", "angles": ["外卖", "预制菜", "添加剂", "信任危机"], "angles_en": ["Delivery food", "Pre-made meals", "Additives", "Trust issues"]},
        {"title": "环境保护", "title_en": "Environment", "angles": ["垃圾分类", "限塑令", "极简", "个人能做什么"], "angles_en": ["Waste sorting", "Plastic bans", "Minimalism", "What can I do?"]},
        {"title": "养老/老龄化", "title_en": "Aging population", "angles": ["养老金", "延迟退休", "养老社区", "父母养老"], "angles_en": ["Pensions", "Delayed retirement", "Retirement communities", "Parents' care"]},
        {"title": "社会时钟", "title_en": "Social clock", "angles": ["多大该做什么", "落后了", "30岁焦虑", "有自己的节奏"], "angles_en": ["What age to do what", "Falling behind", "30s anxiety", "Your own pace"]},
        # ===== 16. 趣味·脑洞 (10) =====
        {"title": "如果明天是世界末日", "title_en": "If tomorrow were the last day", "angles": ["做什么", "见谁", "还上班吗", "后悔什么"], "angles_en": ["What to do", "Who to see", "Still go to work?", "Regrets"]},
        {"title": "超能力选什么", "title_en": "Which superpower?", "angles": ["隐身", "时间停止", "读心术", "飞行"], "angles_en": ["Invisibility", "Time stop", "Mind reading", "Flying"]},
        {"title": "穿越到古代", "title_en": "Time travel to ancient China", "angles": ["哪个朝代", "带什么", "能活几天", "最想见谁"], "angles_en": ["Which dynasty", "What to bring", "How long would you survive?", "Who to meet"]},
        {"title": "中了彩票", "title_en": "Winning the lottery", "angles": ["多少钱", "先干嘛", "告诉谁", "会变吗"], "angles_en": ["How much?", "First thing", "Who to tell", "Would you change?"]},
        {"title": "和动物交换身体", "title_en": "Swap bodies with an animal", "angles": ["猫", "鸟", "鱼", "动物园里的"]},
        {"title": "荒岛求生带三样东西", "title_en": "Three items on a desert island", "angles": ["实用派", "浪漫派", "生存狂", "奇葩答案"], "angles_en": ["Pragmatic", "Romantic", "Survivalist", "Wild answers"]},
        {"title": "平行世界的你", "title_en": "Alternate universe you", "angles": ["另一个选择", "同一个人吗", "想对他说什么", "羡慕吗"], "angles_en": ["Different choices", "Same person?", "What to say", "Jealous?"]},
        {"title": "最奇怪的习惯", "title_en": "Weirdest habits", "angles": ["吃的", "睡前的", "工作时的", "别人觉得奇怪的"], "angles_en": ["Eating", "Bedtime", "At work", "Others find weird"]},
        {"title": "一觉醒来失忆了", "title_en": "Wake up with amnesia", "angles": ["谁是你", "怎么找回记忆", "想记住什么", "重新开始"], "angles_en": ["Who are you?", "Recovering memories", "What to remember", "Starting over"]},
        {"title": "和名人交换一天", "title_en": "Swap lives with a celebrity", "angles": ["活着还是历史", "为什么是他", "做什么", "换回来吗"], "angles_en": ["Living or historical", "Why them?", "What to do", "Would you switch back?"]},
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
    """轮选常青话题（每天换一个，保证每日不同）"""
    from datetime import date
    today = date.today()
    day_of_year = today.timetuple().tm_yday + week_offset
    idx = (day_of_year - 1) % len(SEASONAL_TOPICS["evergreen"])
    pick = SEASONAL_TOPICS["evergreen"][idx]
    # 角度也按天轮换
    angle_idx = (day_of_year - 1) % len(pick["angles"])
    return {
        "title": pick["title"],
        "title_en": pick.get("title_en", pick["title"]),
        "angle": pick["angles"][angle_idx],
        "angle_en": pick.get("angles_en", pick["angles"])[angle_idx % len(pick.get("angles_en", pick["angles"]))],
        "type": "经典话题",
        "type_en": "Classic Topic",
    }
