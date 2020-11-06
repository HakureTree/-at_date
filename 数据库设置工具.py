def datasetting():
    import os
    import shutil
    import sys
    import time
    import random
    import threading
    from tkinter import messagebox
    print('''┏━━━━━━━━━━━━━━━━━━━━━━━━━━┒
    ┃||||||||AZQS工具箱||||||||┃
    ┃||||||||数据库设置||||||||┃
    ┖━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
    time.sleep(0.5)
    while 1>0:
        print("<<<<<<数据库相关>>>>>>")
        time.sleep(0.5)
        print("① >重置识别码(请勿使用)<")
        time.sleep(0.5)
        print("② >个性签名<")
        time.sleep(0.5)
        print("③ >删除软件<")
        time.sleep(0.5)
        print("④ >设置密码<")
        print("'quit' >退出程序<")
        time.sleep(0.5)
        datasettingmode=input("请输入您需要的模式：")
        time.sleep(0.5)
        if datasettingmode=="1":
            print("该功能暂不开放！")
            time.sleep(0.5)
            #if os.path.exists(r'C:\ProgramData\computerhwid_at.txt'):
                #print("识别码文件存在")
                #time.sleep(0.5)
                #file=open(r'C:\ProgramData\computerhwid_at.txt')
                #hwid=file.read()
                #print("你当前的识别码为："+str(hwid))
                #hwidresetdecide=input("是否重置识别码？（回复“是”或“否”）：")
                #if hwidresetdecide=="是":
                    #time.sleep(1)
                    #hwid = str(random.randint(100000,100000000000))
                    #file = open(r'C:\ProgramData\computerhwid_at.txt', 'w')
                    #file.write(hwid)
                    #time.sleep(0.5)
                    #print("识别码重置完成")
                    #time.sleep(0.5)
                    #print("您的识别码已修改为："+str(hwid))
                    #time.sleep(3)
                #elif hwidresetdecide=="否":
                    #time.sleep(1)
                    #print("我们将不会修改你的识别码！")
                    #time.sleep(0.5)
                #else:
                    #print("请正确输入！")
            #else:
                #print("识别码文件不存在")
                #time.sleep(1)
                #hwid=str(random.randint(100000,100000000000))
                #file = open(r'C:\ProgramData\computerhwid_at.txt', 'w')
                #file.write(hwid)
                #time.sleep(0.5)
                #print("识别码文件生成完成")
        elif datasettingmode=="2":
            if os.path.exists(r'C:\ProgramData\userdata_at.txt'):
                print("个性签名文件存在")
                file=open(r'C:\ProgramData\userdata_at.txt')
                userdate=file.read()
                file.close()
                time.sleep(0.5)
            else:
                print("个性签名文件不存在")
                time.sleep(1)
                userdate="*暂无个性签名*"
                file = open(r'C:\ProgramData\userdata_at.txt', 'w')
                file.write(userdate)
                time.sleep(0.5)
                print("个性签名生成完成")
                file.close()
                time.sleep(0.5)
            userdate=input("请输入您的个性签名：")
            pingbiciku = ["马","妈","傻逼","死","屌","吊","雕","sb","biss"]
            pingbicijiance=0
            for i in pingbiciku:
                if i in userdate:
                    userdate = userdate.replace(i, "*",1000)
                    pingbicijiance=1
                else:
                    userdate=userdate
            file = open(r'C:\ProgramData\userdata_at.txt', 'w')
            file.write(userdate)
            time.sleep(0.5)
            print("个性签名已同步")
            file.close()
            time.sleep(3)
        elif datasettingmode=="3":
            hwidresetdecide=input("您确定删除azqs工具箱与其附属组件？（回复“是”或“否”）：")
            if hwidresetdecide=="是":
                time.sleep(0.5)
                print("正在开始删除程序...")
                if os.path.exists(r'C:\ProgramData\at_data-main'):
                    shutil.rmtree(r"C:\ProgramData\at_data-main")
                    time.sleep(0.5)
                    print("数据文件已删除")
                else:
                    time.sleep(0.5)
                    print("数据文件不存在")
                if os.path.exists(r'C:\ProgramData\at_ver-main'):
                    shutil.rmtree(r"C:\ProgramData\at_ver-main")
                    time.sleep(0.5)
                    print("版本文件1已删除")
                else:
                    time.sleep(0.5)
                    print("版本文件1不存在")
                if os.path.exists(r'C:\ProgramData\checkver.txt'):
                    os.remove(r"C:\ProgramData\checkver.txt")
                    time.sleep(0.5)
                    print("版本文件2已删除")
                else:
                    time.sleep(0.5)
                    print("版本文件2不存在")
                if os.path.exists(r'C:\ProgramData\at_data-main.zip'):
                    os.remove(r"C:\ProgramData\at_data-main.zip")
                    time.sleep(0.5)
                    print("数据压缩包已删除")
                else:
                    time.sleep(0.5)
                    print("数据压缩包不存在")
                if os.path.exists(r'C:\ProgramData\at_ver-main.zip'):
                    os.remove(r"C:\ProgramData\at_ver-main.zip")
                    time.sleep(0.5)
                    print("版本压缩包已删除")
                else:
                    time.sleep(0.5)
                    print("版本压缩包不存在")
                if os.path.exists(r'C:\ProgramData\userdata_at.txt'):
                    os.remove(r"C:\ProgramData\userdata_at.txt")
                    time.sleep(0.5)
                    print("用户数据1已删除")
                else:
                    time.sleep(0.5)
                    print("用户数据1不存在")
                if os.path.exists(r'C:\ProgramData\username_at.txt'):
                    os.remove(r"C:\ProgramData\username_at.txt")
                    time.sleep(0.5)
                    print("用户数据2文件已删除")
                else:
                    time.sleep(0.5)
                    print("用户数据2不存在")
                if os.path.exists(r'C:\ProgramData\password_at.txt'):
                    os.remove(r"C:\ProgramData\password_at.txt")
                    time.sleep(0.5)
                    print("验证文件已删除")
                else:
                    time.sleep(0.5)
                    print("验证文件不存在")
                time.sleep(0.5)
                print("已将azqs工具箱从您的计算机中移除")
                time.sleep(5)
                quit()
            elif hwidresetdecide=="否":
                time.sleep(0.5)
                print("我们将不会删除你的文件！")
                time.sleep(3)
            else:
                print("请正确输入！")
        elif datasettingmode=="4":
            print("正在检查验证文件...")
            time.sleep(0.5)
            if os.path.exists(r'C:\ProgramData\password_at.txt'):
                print("验证文件存在")
                file=open(r'C:\ProgramData\password_at.txt')
                password=file.read()
                file.close()
                time.sleep(0.5)
            else:
                print("验证文件不存在")
                time.sleep(1)
                password="542nb"
                file = open(r'C:\ProgramData\password_at.txt', 'w')
                file.write(password)
                time.sleep(0.5)
                print("验证文件生成完成，默认密码为：542nb")
                file.close()
                time.sleep(0.5)
            resetpassword=input("请输入你的新密码：")
            time.sleep(0.5)
            password=resetpassword
            print("正在写入密码中...")
            os.remove(r"C:\ProgramData\password_at.txt")
            file=open(r'C:\ProgramData\password_at.txt','w')
            file.write(password)
            print("密码写入完成！")
            file.close()
            time.sleep(0.5)
            print("密码更新完成！")
            time.sleep(3)
        elif datasettingmode=="quit":
            print("正在退出...")
            time.sleep(3)
            break
        else:
            print("请正确输入！")
    #备用密码为：Ⴉ
