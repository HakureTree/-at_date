import sys
import time
import random
import threading
from tkinter import messagebox
def tanchuangtool():
    time.sleep(2)
    print("<<<<<<一个弹窗被生成了>>>>>>")
    tanchuangcishu=10
    while tanchuangcishu>0:
        messagebox.showinfo("╰(*°▽°*)╯","我是一个弹窗")
        tanchuangcishu-=1
    tanchuangcishu=5
    while tanchuangcishu>0:
        messagebox.showinfo("(。_。)","你是在尝试关掉我吗？")
        tanchuangcishu-=1
    messagebox.showinfo("_( ﾟДﾟ)ﾉ","陪我一会嘛......")
    tanchuangcishu=3
    while tanchuangcishu>0:
        messagebox.showinfo("(。﹏。)","而你依然想关掉我...")
        tanchuangcishu-=1
    messagebox.showinfo("┌(。Д。)┐","我不想让你离开我，强行关掉我会让程序停止运作哦！ ")
    messagebox.showinfo("╥﹏╥","但你真的下决心要让我消失...吗？")
    messagebox.showinfo("(;-;)",'''又要回归孤独了呢......
呐呐，我以后还能再见到你吗...?''')
