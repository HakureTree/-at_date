import sys
import time
import random
import threading
from tkinter import messagebox
def chengzanmode():
    time.sleep(2)
    chengzan=str(input("请输入你要称赞的对象："))
    pingbiciku = ["马","妈","傻逼","死","屌","吊","雕","sb","biss"]
    pingbicijiance=0
    for i in pingbiciku:
        if i in chengzan:
            chengzan = chengzan.replace(i, "*",1000)
            pingbicijiance=1
    print(chengzan+"好帅")
    time.sleep(2)
