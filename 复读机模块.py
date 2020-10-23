import sys
import time
import random
import threading
from tkinter import messagebox
def putongfudujitool():
    time.sleep(2)
    while 1>0:
        print("<<<<<<复读机>>>>>>")
        time.sleep(0.5)
        print("使用复读功能请输入‘1’")
        time.sleep(0.5)
        print("退出工具请输入‘quit’")
        fudujijueding=input("我决定输入：")
        time.sleep(1)
        if fudujijueding=="1":
            time.sleep(0.5)
            fudujineirong=input("请输入你需要复读的内容：")
            pingbiciku = ["马","妈","傻逼","死","屌","吊","雕","sb","biss"]
            pingbicijiance=0
            for i in pingbiciku:
                if i in fudujineirong:
                    fudujineirong = fudujineirong.replace(i, "*",1000)
                    pingbicijiance=1
            time.sleep(0.5)
            fudujicishu=int(input("请输入你需要复读的次数(仅整数)："))
            while fudujicishu>0:
                print(fudujineirong)
                fudujicishu-=1
        elif fudujijueding=="quit":
            time.sleep(0.5)
            print("正在退出...")
            time.sleep(1)
            break
        else:
            time.sleep(1)
            print("请说计算机话！")
            time.sleep(1)
