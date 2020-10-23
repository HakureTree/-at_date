import sys
import time
import random
import threading
from tkinter import messagebox
def chaojifudujitool():
    time.sleep(2)
    print("<<<<<<超级复读机>>>>>>")
    time.sleep(1)
    print("警告:该功能使用后只能靠关闭程序来结束")
    time.sleep(1)
    while 1>0:
        print("是否继续？（回答 ‘是’ 或 ‘否’）")
        time.sleep(1)
        chaojifudujijueding = input("你的决定: ")
        if chaojifudujijueding== "是":
            time.sleep(1)
            print("收到")
            time.sleep(1)
            chaojifudujineirong=input("请键入需要复读的内容(如果打不出字可以从外部打完复制黏贴进来): ")
            pingbiciku = ["马","妈","傻逼","死","屌","吊","雕","sb","biss"]
            pingbicijiance=0
            for i in pingbiciku:
                if i in chaojifudujineirong:
                    chaojifudujineirong = chaojifudujineirong.replace(i, "*",1000)
                    pingbicijiance=1
            time.sleep(2)
            while 1>0:
                print(chaojifudujineirong)
        elif chaojifudujijueding=="否":
            time.sleep(1)
            print("尊重你的决定")
            time.sleep(1)
            break
        else:
            print("你到底想怎样？")
            time.sleep(1)
