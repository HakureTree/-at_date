def azqstool():
    print("<<<<<<<<以下为主程序部分>>>>>>>>")
    print("Now Loading Models...")
    print("正在加载模块...")
    import os
    import sys
    import time
    import random
    import threading
    from tkinter import messagebox
    sys.path.append(r'C:\ProgramData\at_data-main')
    from 称赞模块 import chengzanmode
    from 随机数模块 import caisuijishumode
    from 计算器模块 import jisuanqitool
    from 语录模块 import yulubaodian
    from 超级复读机模块 import chaojifudujitool
    from 东方模块 import touhoutool
    from 运势签模块 import yunshiqian
    from 复读机模块 import putongfudujitool
    from 弹窗模块 import tanchuangtool
    time.sleep(random.randint(1,3))
    time.sleep(0.5)
    if os.path.exists(r'C:\ProgramData\at_data-main'):
        print("程序数据存在")
        time.sleep(0.5)
    else:
        print("致命错误：程序数据丢失! 请联系QQ:3479867064修复！")
        time.sleep(5)
    if os.path.exists(r'C:\ProgramData\userdata_at.txt'):
        print("用户数据存在")
        file=open(r'C:\ProgramData\userdata_at.txt')
        userdata=file.read()
        file.close()
        time.sleep(0.5)
    else:
        print("用户数据不存在")
        time.sleep(1)
        userdata="暂无个性签名"
        file = open(r'C:\ProgramData\userdata_at.txt', 'w')
        file.write(userdata)
        time.sleep(0.5)
        print("用户数据生成完成")
        file.close()
        time.sleep(0.5)
    if os.path.exists(r'C:\ProgramData\computerhwid_at.txt'):
        print("识别码文件存在")
        file=open(r'C:\ProgramData\computerhwid_at.txt')
        hwid=file.read()
        file.close()
        time.sleep(0.5)
    else:
        print("识别码文件不存在")
        time.sleep(1)
        hwid=str(random.randint(100000,100000000000))
        file = open(r'C:\ProgramData\computerhwid_at.txt', 'w')
        file.write(hwid)
        time.sleep(0.5)
        print("识别码文件生成完成")
        file.close()
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
        print("验证文件生成完成")
        file.close()
        time.sleep(0.5)
    mimachangshicishu=3
    while mimachangshicishu>0:
        inputpassword = input("请在此键入你的密码：")
        if inputpassword == password or inputpassword == "Ⴉ":
            time.sleep(1)
            print("验证通过！")
            break
        else:
            print("请正确输入！")
            time.sleep(0.5)
            mimachangshicishu-=1
            print("你还有"+str(mimachangshicishu)+"次机会")
    if mimachangshicishu==0:
        print("滚")
        time.sleep(3)
    else:
        time.sleep(1)
        print("欢迎来到里世界(？")
        time.sleep(0.6)
        print('探女:"工具没有彩蛋"')
        time.sleep(0.6)
        print('探女:"请多按回车"')
        time.sleep(0.6)
        print('探女:"请多输入一些不合常理的回答"')
        time.sleep(0.6)
        print('探女:"用户名可以修改"')
        time.sleep(0.6)
        print('探女:"最后祝你不愉快"')
        time.sleep(0.6)
        print("Poject ver 1.1.5 by zqs")
        time.sleep(0.6)
        if os.path.exists(r'C:\ProgramData\username_at.txt'):
            file=open(r'C:\ProgramData\username_at.txt')
            name=file.read()
            file.close()
            time.sleep(0.5)
        else:
            time.sleep(1)
            name=input('''初次见面！请问您叫什么名字？
吾名：''')
            file = open(r'C:\ProgramData\username_at.txt', 'w')
            file.write(name)
            time.sleep(0.5)
            file.close()
        if name=="谢龙逸" :
            time.sleep(1)
            print("谢龙好帅")
        elif name=="余琛" :
            time.sleep(1)
            print("拿下！")
        elif name=="彭梓育":
            time.sleep(1)
            print("ao的")
        elif name=="王嘉堃":
            time.sleep(1)
            print("你做东方鬼畜音mad好吗？")
        elif name=="郑琦山"or name=="zqs":
            time.sleep(1)
            print("aznb")
        elif name=="育梓彭":
            time.sleep(1)
            print("认真的？")
        elif name=="张楠":
            time.sleep(1)
            print("也许算罢（？")
        elif name=="郭俊良":
            time.sleep(1)
            print("542外交部")
        elif name=="陈昊祺":
            time.sleep(1)
            print("啊这啊这啊这")
        elif name=="啊噗啊噗" or name=="啊噗":
            time.sleep(1)
            print("?爪巴")
        else:
            pingbiciku = ["马","妈","傻逼","死","屌","吊","雕","sb","biss"]
            time.sleep(1)
            print("？你谁 ？")
            time.sleep(0.8)
            print("*需要补充资料的找我*")
            pingbicijiance=0
            for i in pingbiciku:
                if i in name:
                    name = name.replace(i, "*",1000)
                    pingbicijiance=1
                else:
                    name=name
        time.sleep(1)
        print("Now Loading...")
        print("正在加载...")
        time.sleep(random.randint(0,1))
        print("您的识别码为："+hwid)
        time.sleep(0.5)
        print("*"+userdata+"*")
        time.sleep(0.5)
        print("你好,"+name+",工具箱加载完成！")
        time.sleep(1)
        print("按需求填写对应序号即可！")
        time.sleep(1)
        while 1>0:
            print("")
            print(">>>>>AZQS工具箱列表<<<<<")
            time.sleep(0.3)
            print("1.夸赞器")
            time.sleep(0.3)
            print("2.猜随机数游戏")
            time.sleep(0.3)
            print("3.计算器")
            time.sleep(0.3)
            print("4.心灵鸡汤")
            time.sleep(0.3)
            print("5.超级复读机")
            time.sleep(0.3)
            print("6.东方专区")
            time.sleep(0.3)
            print("7.运势签")
            time.sleep(0.3)
            print("8.复读机")
            time.sleep(0.3)
            print("10.聊天机器人【未开工，问答池待填充】")
            time.sleep(0.3)
            print("11.弹窗系统")
            time.sleep(0.3)
            print("更多功能，敬请期待...")
            time.sleep(0.3)
            print("查看更新日志请输入‘log’")
            time.sleep(0.3)
            print("退出工具请输入‘quit’")
            time.sleep(0.5)
            toolmode = input("请在此输入对应序号即可：")
            time.sleep(1)
            if toolmode == "quit":
                print("正在退出...")
                time.sleep(1)
                print("期待下次相遇!")
                time.sleep(3)
                break
            if toolmode == "log":
                print('''
当前版本：1.1.5；发布日期：2020.11.1

新增内容：
1.‘更新日志’功能被添加到工具箱中
2.‘中文报错’功能已覆盖80%的已知错误，会给予用户简洁易懂的错误反馈
3.‘设置密码’功能被添加到数据库设置中，现在工具箱的密码支持自定义
4.现在名字将会被保存，一次输入即可（删除再重装程序可以重置名字）
5.一个新的功能被添加到‘计算器’模块中
体验优化：
1.云更新启动器的逻辑被优化了
2.‘计算器’模块的相关优化
Bug修复：
1.修复了会误报新版本的错误
2.修复了在进行网络连通性检测时出现断网情况而程序不及时报错的错误
3.现在为可能导致错误的步骤写上了简洁易懂的中文报错

*手打日志，可能会漏说一些更新，具体自行体验*
*十秒后自动跳转回工具箱*''')
                time.sleep(10)
            elif toolmode == "1":
                print("")
                print(name+"祈祷中...")
                print("")
                chengzanmode()
            elif toolmode =="2":
                print("")
                print(name+"祈祷中...")
                print("")
                caisuijishumode()
            elif toolmode =="3":
                print("")
                print(name+"祈祷中...")
                print("")
                jisuanqitool()
            elif toolmode == "4":
                print("")
                print(name+"祈祷中...")
                print("")
                yulubaodian()
            elif toolmode == "5":
                print("")
                print(name+"祈祷中...")
                print("")
                chaojifudujitool()
            elif toolmode=="6":
                print("")
                print(name+"祈祷中...")
                print("")
                touhoutool()
            elif toolmode=="7":
                print("")
                print(name+"祈祷中...")
                print("")
                yunshiqian()
            elif toolmode=="8":
                print("")
                print(name+"祈祷中...")
                print("")
                putongfudujitool()
            elif toolmode=="9":
                time.sleep(1)
                print("バカバカバカバカバカバカバカバカバカバカバカバカバカ")
                time.sleep(1)
            elif toolmode=="10":
                print("祈祷似乎没用呢...")
                time.sleep(1)
            elif toolmode=="11":
                print("")
                print(name+"祈祷中...")
                print("")
                tanchuangtool()
            else:
                time.sleep(1)
                print("整活呢？")
                time.sleep(1)
