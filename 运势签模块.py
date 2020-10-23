import sys
import time
import random
import threading
from tkinter import messagebox
def yunshiqian():
    time.sleep(2)
    print("<<<<<<☯运势签☯>>>>>>")
    time.sleep(1)
    print("使用这个功能来预测你今天的运势吧！")
    yunshiqianjieguo = 0
    time.sleep(1)
    yunshiqianxuyuan=input("说出你想说的话：")
    pingbiciku = ["马","妈","傻逼","死","屌","吊","雕","sb","biss"]
    pingbicijiance=0
    for i in pingbiciku:
        if i in yunshiqianxuyuan:
            pingbicijiance=1
    if pingbicijiance==1:
        print("你有毛病？别乱许愿！")
    else:
        time.sleep(1)
        print("少女折寿中...")
        time.sleep(2)
        yunshiqianjieguo = random.randint(1,100)
        print("你抽中了：")
        time.sleep(2)
        if yunshiqianjieguo>=1 and yunshiqianjieguo<7:
            print("☯上上签☯")
        elif yunshiqianjieguo>=7 and yunshiqianjieguo<20:
            print("☯上签☯")
        elif yunshiqianjieguo>=20 and yunshiqianjieguo<40:
            print("☯吉签☯")
        elif yunshiqianjieguo>=40 and yunshiqianjieguo<70:
            print("☯良签☯")
        elif yunshiqianjieguo>=70 and yunshiqianjieguo<95:
            print("☯平签☯")
        elif yunshiqianjieguo>=95 and yunshiqianjieguo<100:
            print("今天你有点厄厄，要不考虑再来一签？")
        else:
            print("?不知道是什么力量让签全部不见了")
        time.sleep(1)
        print("最好是以第一次的结果为准(当然你想多抽几次我也拦不住你的hh)")
        time.sleep(1)
        print("仅供参考娱乐罢，祝你每天开心~")
        time.sleep(1)
