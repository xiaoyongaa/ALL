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
    while flag:
        backend=input("请输入你要查询的backend记录: ")
        backend=backend.strip()
        if backend=="q" or backend=="quit":
            return "f"
        elif backend=="b" or backend=="b":
             break
        key1="backend"+" "+backend
        old=open("haproxy.cnf.txt","r").read()
        if key1 in old:
            print("你所找的backend在配置文件里")
            with open("haproxy.cnf.txt","r") as new:
                f=True
                for i in new:
                    if i.strip()==key1:
                        f=False
                        print(i.strip())
                        continue
                    if i.strip().startswith("backend") and f==False:
                        f=True
                        continue
                    if f==False:
                        print(i.strip())




        else:
            print("你所找的backend不在在配置文件里，请重新输入")
#查询模块


#增加模块
def add():
    flag=True
    li=[]
    ##########把配置文件的空格全部去掉########
    with open("haproxy.cnf.txt","r") as old,open("haproxy.cnf.add.txt","w") as add:
        for i in old:
            if i.strip():
                add.write(i)
    with open("haproxy.cnf.add.txt","r") as a,open("haproxy.cnf.txt","w") as old:
        shutil.copy("haproxy.cnf.add.txt","haproxy.cnf.txt")
    #############把配置文件的空格全部去掉##########
    while flag:
        choose=input("请输入你要增加记录的backend和record：")
        choose=choose.strip()
        if choose=="q" or choose=="quit":
            return "f"
        elif choose=="b" or choose=="b":
             flag=False
             break
        choose=json.loads(choose)
        backend=choose.get("backend")
        record=choose.get("record")
        server=record.get("server")
        weight=record.get("weight")
        maxconn=record.get("maxconn")
        server=str(server)
        weight=str(weight)
        maxconn=str(maxconn)
        key1="backend"+" "+backend
        key2="server"+" "+server+" "+server+" "+"weight"+" "+weight+" "+"maxconn"+" "+maxconn
        print(key2)
        add=open("haproxy.cnf.add.txt","r").read()
        if key1 in add:
            print("这个backend在配置文件里面，是已经存在的，只需要添加record")
            with open("haproxy.cnf.add.txt","r") as add:
                f=True
                for i in add:
                    if i.strip()==key1:
                        f=False
                        continue
                    if i.strip().startswith("backend") and f==False:
                        f=True
                        continue
                    if f==False:
                       li.append(i.strip())
            if  key2 in li:
                print("该record记录已经存在，无需添加")
            else:
                print("该record记录不存在，需要添加record")
                li.append(key2)
                with open("haproxy.cnf.add.txt","r") as add,open("haproxy.cnf.add2.txt","w") as add2:
                    fla=True
                    for i in add:
                        if i.strip()==key1:
                            fla=False
                            add2.write(i)
                            for i in li:
                                add2.write("\t"+i+"\n")
                            #continue
                        if i.strip().startswith("backend") and fla==False:
                            fla=True
                            add2.write(i)
                            continue
                        if fla==True:
                            add2.write(i)
                shutil.copy("haproxy.cnf.add2.txt","haproxy.cnf.add.txt")  #还原配置
                shutil.copy("haproxy.cnf.add2.txt","haproxy.cnf.txt")      #还原真正线上配置
                flag=False
                break
        else:
            print("这个backend不在配置文件里面，是新的，需要新添加backend和record")
            with open("haproxy.cnf.add.txt","a") as add:
                add.write("\n"+key1+"\n"+"\t"+key2)
            shutil.copy("haproxy.cnf.add.txt","haproxy.cnf.add2.txt")  #还原配置
            shutil.copy("haproxy.cnf.add.txt","haproxy.cnf.txt")      #还原真正线上配置
            flag=False
            break
#增加模块

#删除模块







main()



