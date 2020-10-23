import sys
import time
import random
import threading
from tkinter import messagebox
def caisuijishumode():
    time.sleep(2)
    suijishuzuixiao=int(input("请输入随机数的最小值（仅整数）: "))
    suijishuzuida=int(input("请输入随机数的最大值（仅整数）: "))
    time.sleep(1)
    print("随机数生成中...")
    suijishu=random.randint(suijishuzuixiao,suijishuzuida)
    time.sleep(2)
    print("随机数生成完成!")
    suijishuchance = int(input("输入你想要尝试的次数(仅整数)："))
    while suijishuchance > 0 :
        time.sleep(1)
        suijishuanswer = int(input("来猜一个数吧(仅整数)："))
        if suijishuanswer > suijishu:
            time.sleep(0.5)
            print("你猜的数大了！")
            suijishuchance -= 1
            time.sleep(0.5)
            print("你还有"+str(suijishuchance)+"次机会！")
        elif suijishuanswer < suijishu:
            time.sleep(0.5)
            print("你猜的数小了！")
            suijishuchance -= 1
            time.sleep(0.5)
            print("你还有"+str(suijishuchance)+"次机会！")
        elif suijishuanswer == suijishu:
            time.sleep(0.5)
            print("猜中了！")
            break
    if suijishuchance == 0:
        time.sleep(1)
        print("你个⑨东西")
        time.sleep(2)
    else:
        time.sleep(1)
        print("《合理》")
        time.sleep(2)
