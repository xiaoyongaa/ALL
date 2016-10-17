import json
import os
import shutil
flag=True
msg=["1.获取ha记录","2.增加ha记录","3.删除ha记录","4.修改ha记录"]


#主入口
def main():
    #主界面
    flag=True
    while flag:
        for i in msg:
            print(i)
        choose=input("请输入你要选择的操作：")
        choose=choose.strip()
        if choose=="1":
            print("你选择了获取记录")
            f=huoqu()
            if f=="f":
             flag=False
             break
        elif choose=="2":
            print("你选择了增加记录")
            f=add()
            if f=="f":
             flag=False
             break
        elif choose=="3":
            print("你选择了删除记录")
            f=delete()
            if f=="f":
             flag=False
             break
        elif choose=="4":
            print("你选择了修改记录")
            f=xiugai()
            if f=="f":
             flag=False
             break
        elif choose=="q" or choose=="Q":
            print("你选择了退出")
            flag=False
            break
#主入口

#查询模块
def huoqu():
    flag=True
    while True:
        backend=input("请输入你要查询的backend记录: ")
        backend
        key1="backend"+" "+backend
        old=open("haproxy.cnf.txt","r").read()
        if key1 in old:
            print("你所找的backend在配置文件里")

        else:
            print("你所找的backend不在在配置文件里，请重新输入")







main()



