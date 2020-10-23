import sys
import time
import random
import threading
from tkinter import messagebox
def touhoutool():
    time.sleep(2)
    while 1>0:
        print("<<<<<<东方专区>>>>>>")
        time.sleep(1)
        print("①什么是东方？")
        time.sleep(0.5)
        print("②东方正作表")
        time.sleep(0.5)
        print("③东方曲推荐")
        time.sleep(0.5)
        print("④东方官方书籍")
        time.sleep(0.5)
        print("⑤我有其他关于东方的疑问")
        time.sleep(0.5)
        print("离开请输入‘quit’")
        time.sleep(0.5)
        touhoumode=input("请输入你需要了解的对应编号：")
        if touhoumode=="1":
            time.sleep(1)
            print("《东方Project》，简称东方，是日本人ZUN所制作的一系列同人游戏、相关作品。它以及其二次创作所构成的覆盖游戏、动画、漫画、音乐、文学等诸多方面的领域")
            time.sleep(1)
        elif touhoumode=="2":
            time.sleep(1)
            print("目前东方官方游戏作品主要有两种")
            time.sleep(1)
            print("弹幕射击类（stg）与 格斗类（ftg）")
            time.sleep(1)
            print("   《东方正作表》    ")
            time.sleep(0.5)
            print("旧作：")
            time.sleep(0.5)
            print("th01 东方灵异传 (打砖块)")
            time.sleep(0.5)
            print("th02 东方封魔录 (stg)")
            time.sleep(0.5)
            print("th03 东方梦时空 (stg)")
            time.sleep(0.5)
            print("th04 东方幻想乡 (stg)")
            time.sleep(0.5)
            print("th05 东方怪绮谈 (stg)")
            time.sleep(0.5)
            print("新作：")
            time.sleep(0.5)
            print("th06 东方红魔乡 (stg)")
            time.sleep(0.5)
            print("th07 东方妖妖梦 (stg)")
            time.sleep(0.5)
            print("th07.5 东方萃梦想 (ftg)")
            time.sleep(0.5)
            print("th08 东方永夜抄 (stg)")
            time.sleep(0.5)
            print("th09 东方花映冢 (stg)")
            time.sleep(0.5)
            print("th09.5 东方文花帖 (stg)")
            time.sleep(0.5)
            print("th10 东方风神录 (stg)")
            time.sleep(0.5)
            print("th10.5 东方绯想天 (ftg)")
            time.sleep(0.5)
            print("th11 东方地灵殿 (stg)")
            time.sleep(0.5)
            print("th12 东方星莲船 (stg)")
            time.sleep(0.5)
            print("th12.3 东方非想天则 (ftg)")
            time.sleep(0.5)
            print("th12.5 东方文花帖ds (stg)")
            time.sleep(0.5)
            print("th12.8 东方三月精 (stg)")
            time.sleep(0.5)
            print("th13 东方神灵殿 (stg)")
            time.sleep(0.5)
            print("th13.5 东方心绮楼 (ftg)")
            time.sleep(0.5)
            print("th14 东方辉针城 (stg)")
            time.sleep(0.5)
            print("th14.3 弹幕天邪鬼 (stg)")
            time.sleep(0.5)
            print("th14.5 东方深秘录 (ftg)")
            time.sleep(0.5)
            print("th15 东方绀珠传 (stg)")
            time.sleep(0.5)
            print("th15.5 东方凭依华 (ftg)")
            time.sleep(0.5)
            print("th16 东方天空璋 (stg)")
            time.sleep(0.5)
            print("th16.5 秘封噩梦日记 (stg)")
            time.sleep(0.5)
            print("th17 东方鬼形兽 (stg)")
            time.sleep(0.5)
            print("th17.5 东方刚欲异闻 (ftg)")
        elif touhoumode=="3":
            time.sleep(1)
            print("东方曲推荐")
            time.sleep(1)
            print("官方（遵循THBwiki第八回东方人气投票数据排名前20歌曲）：")
            time.sleep(0.5)
            print('''                輝く針の小人族 ～ Little Princess
            偶像に世界を委ねて ～ Idoratrize World
            今宵は飄逸なエゴイスト (Live ver) ~ Egoistic Flowers
            神々が恋した幻想郷
            幽雅に咲かせ、墨染の桜 ～ Border of Life
            ハルトマンの妖怪少女
            亡き王女の為のセプテット
            ピュアヒューリーズ ～ 心の在処
            竹取飛翔 ～ Lunatic Princess
            砕月
            月まで届け、不死の煙
            童祭 ～ Innocent Treasures
            感情の摩天楼 ～ Cosmic Mind
            少女綺想曲 ～ Dream Battle
            少女さとり ～ 3rd eye
            上海紅茶館 ～ Chinese Tea
            信仰は儚き人間の為に
            幽霊楽団 ～ Phantom Ensemble
            六十年目の東方裁判 ～ Fate of Sixty Years''')
            time.sleep(1)
            print("同人（优秀社团/个人名称）")
            time.sleep(0.5)
            print('''                stack
            魂音泉
            幽閉サテライト
            たま
            交響アクティブNEETs
            Sing, R. Sing!''')
            time.sleep(1)
            print("              待补充...")
            time.sleep(1)
        elif touhoumode =="4":
            time.sleep(1)
            print("目前由zun编写的书籍如下：")
            time.sleep(0.5)
            print("《东方文花帖》")
            time.sleep(0.5)
            print("《东方香霖堂》")
            time.sleep(0.5)
            print("《东方儚月抄》")
            time.sleep(0.5)
            print("《东方求闻史记》")
            time.sleep(0.5)
            print("《东方求闻口授》")
            time.sleep(0.5)
            print("《魔理沙的弹幕回忆》")
            time.sleep(1)
        elif touhoumode=="5":
            time.sleep(1)
            print("如果还有不懂的地方可以前往以下网址：")
            time.sleep(0.5)
            print("THBwiki-专业性的东方poject百科：https://thwiki.cc/")
            time.sleep(0.5)
            print('''入坑指南：
https://www.bilibili.com/video/BV1Cf4y1U7cH/?spm_id_from=333.788.videocard.0''')
            time.sleep(0.5)
            print('''故事线/设定介绍①（推荐）：
https://www.bilibili.com/video/BV1cJ411W7Bn/?spm_id_from=333.788.videocard.2''')
            time.sleep(0.5)
            print('''故事线/设定介绍②：
https://space.bilibili.com/11007230/channel/detail?cid=1261''')
        elif touhoumode=="quit":
            time.sleep(1)
            print("正在离开幻想乡...")
            time.sleep(0.5)
            print("欢迎再来！")
            time.sleep(2)
            break
        else:
            print("你是⑨吗？怎么话都说不清楚？")
