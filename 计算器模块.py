import sys
import time
import random
import threading
from tkinter import messagebox
def jisuanqitool():
    time.sleep(2)
    while 1>0:
        print("<<<<<<无限制位数计算器>>>>>>")
        time.sleep(1)
        print("①加法")
        time.sleep(0.5)
        print("②减法")
        time.sleep(0.5)
        print("③乘法")
        time.sleep(0.5)
        print("④除法")
        time.sleep(0.5)
        print("⑤圆面积计算(π取3.14)")
        time.sleep(0.5)
        print("退出请输入‘quit’")
        time.sleep(0.5)
        jisuanqimode = input("请输入你需要模式的对应编号：")
        if jisuanqimode == "quit":
            time.sleep(1)
            print("退出计算器中...")
            time.sleep(1)
            break
        elif jisuanqimode == "1":
            time.sleep(0.5)
            print("加法模式！")
            time.sleep(1)
            jisuanqidiyiweishu = float(input("请输入加数："))
            time.sleep(1)
            jisuanqidierweishu = float(input("请输入另一个加数："))
            time.sleep(1)
            print("计算结果为："+str(jisuanqidiyiweishu+jisuanqidierweishu))
            time.sleep(1)
        elif jisuanqimode == "2":
            time.sleep(0.5)
            print("减法模式！")
            time.sleep(1)
            jisuanqidiyiweishu = float(input("请输入被减数："))
            time.sleep(1)
            jisuanqidierweishu = float(input("请输入减数："))
            time.sleep(1)
            print("计算结果为："+str(jisuanqidiyiweishu-jisuanqidierweishu))
            time.sleep(1)
        elif jisuanqimode == "3":
            time.sleep(0.5)
            print("乘法模式！")
            time.sleep(1)
            jisuanqidiyiweishu = float(input("请输入乘数："))
            time.sleep(1)
            jisuanqidierweishu = float(input("请输入另一个乘数："))
            time.sleep(1)
            print("计算结果为："+str(jisuanqidiyiweishu*jisuanqidierweishu))
            time.sleep(1)
        elif jisuanqimode == "4":
            time.sleep(0.5)
            print("除法模式！")
            time.sleep(1)
            jisuanqidiyiweishu = float(input("请输入被除数："))
            time.sleep(1)
            jisuanqidierweishu = float(input("请输入除数："))
            time.sleep(1)
            print("计算结果为："+str(jisuanqidiyiweishu/jisuanqidierweishu))
            time.sleep(1)
        elif jisuanqimode == "5":
            time.sleep(0.5)
            print("除法模式！")
            time.sleep(1)
            jisuanqidiyiweishu = float(input("请输入圆的半径(仅数字):"))
            time.sleep(1)
            print("计算结果为："+str(3.14*jisuanqidiyiweishu*jisuanqidiyiweishu))
            time.sleep(1)
        else:
            time.sleep(1)
            print("请正确使用计算器！")
