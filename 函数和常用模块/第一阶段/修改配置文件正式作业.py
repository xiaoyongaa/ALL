import json
import os
import shutil
##########把配置文件的空格全部去掉########
with open("haproxy.cnf.txt","r") as old,open("haproxy.cnf.add.txt","w") as add:
        for i in old:
            if i.strip():
                add.write(i)
with open("haproxy.cnf.add.txt","r") as a,open("haproxy.cnf.txt","w") as old:
        shutil.copy("haproxy.cnf.add.txt","haproxy.cnf.txt")
#############把配置文件的空格全部去掉##########
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

#获取模块
def huoqu():
    flag=True
    li=[]
    while flag:
        choose=input("（按b返回上一级选择,按q退出整个程序）请输入你要获取的backend记录：")
        if choose=="b" or choose=="B":
            print("你选择了返回")
            break
        elif choose=="q" or choose=="Q":
            print("你选择了退出")
            return "f"
        with open("haproxy.cnf.txt","r") as f:
            key="backend"+" "+choose
            fla=True
            for i in f:
                if i.strip()==key:
                    fla=False
                    continue
                if i.strip().startswith("backend") and fla==False:
                    fla=True
                    break
                if fla==False:
                    print(i.strip())
#获取模块


#增加模块
def add():
    flag=True
    now_list=[]
    with open("haproxy.cnf.txt","r") as old,open("haproxy.cnf.now.txt","w") as new:
                            for i in old:
                                new.write(i.strip()+"\n")
    while flag:
        choose=input("（按b返回上一级选择,按q退出整个程序）请输入你要新增的记录：")
        choose=choose.strip()
        #print("输入格式如backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}})
        if choose=="b" or choose=="B":
            print("你选择了返回")
            break
        elif choose=="q" or choose=="Q":
            print("你选择了退出")
            return "f"
        c=json.loads(choose)
        if  type(c) is dict:
            print("你输入的格式正确")
            backend=c.get("backend") #获取的backend的value
            key1="backend"+" "+backend
            record=c.get("record")   #获取的record的value
            #print(record)
            server=record.get("server")
            maxconn=record.get("maxconn")
            weight=record.get("weight")
            server=str(server)
            maxconn=str(maxconn)
            weight=str(weight)
            key2="server"+" "+server+" "+server+" "+"weight"+" "+weight+" "+"maxconn"+" "+maxconn
            if os.path.exists("haproxy.cnf.now.txt"):  #判断源文件里面是否存在
                with open("haproxy.cnf.now.txt","r") as new:
                    new=new.read()
                    if key1 in new:
                        print("存在这个backend")
                        #backend存在，recond存在或者不存在
                        with open("haproxy.cnf.now.txt","r") as new:
                            fla=True
                            for i in new:
                                if i.strip()==key1:
                                    fla=False
                                    continue
                                if i.strip().startswith("backend") and fla==False:
                                    fla=True
                                    break
                                if fla==False:
                                    now_list.append(i.strip())
                            if key2 in now_list:        #判断record的值是否存在源文件里
                                print("存在这个backend，并且record也存在，无需添加")
                            else:
                                print("存在这个backend，但是不存在record，需要添加,添加成功！")
                                now_list.append(key2.strip())    #新的record增加到列表
                                with open("haproxy.cnf.now.txt","r") as new,open("haproxy.cnf.now2.txt","w") as new2:
                                    fla=True
                                    for i in new:
                                        if i.strip().startswith(key1):
                                            fla=False
                                            new2.write(i)  #写入新文件操作
                                            for line in now_list:  #写入now_list
                                                new2.write("\t"+line+"\n")
                                            continue
                                        if i.strip().startswith("backend") and  fla==False:
                                            fla=True
                                            new2.write(i)
                                            continue
                                        if i.strip() and fla==True:
                                            new2.write(i)
                                shutil.copy("haproxy.cnf.now2.txt","haproxy.cnf.now.txt")  #还原配置
                                shutil.copy("haproxy.cnf.now2.txt","haproxy.cnf.txt")      #还原真正线上配置
                        flag=False
                        break
                     #backend存在，recond存在或者不存在
                    else:
                        print("不存在，需要添加,添加成功")
                        with open("haproxy.cnf.txt","r") as old,open("haproxy.cnf.now.txt","w") as new:
                            for i in old:
                                new.write(i)
                        new_a=open("haproxy.cnf.now.txt","a")
                        key2="server"+" "+server+" "+server+" "+"weight"+" "+weight+" "+"maxconn"+" "+maxconn
                        new_a.write("\n"+key1+"\n"+"\t"+key2+"\n")
                        new_a.close()
                        shutil.copy("haproxy.cnf.now.txt","haproxy.cnf.txt")
            else:
                with open("haproxy.cnf.txt","r") as old:
                    old=old.read()
                    if key1 in old:
                        print("存在这个backend，不需要添加")
                        #backend存在，recond存在或者不存在
                        with open("haproxy.cnf.now.txt","r") as new:
                            fla=True
                            for i in new:
                                if i.strip()==key1:
                                    fla=False
                                    continue
                                if i.strip().startswith("backend") and fla==False:
                                    fla=True
                                    break
                                if fla==False:
                                    now_list.append(i.strip())
                            if key2 in now_list:        #判断record的值是否存在源文件里
                                print("存在这个backend，并且record也存在，无需添加")
                            else:
                                print("存在这个backend，但是不存在record，需要添加,添加成功！")
                                now_list.append(key2.strip())    #新的record增加到列表
                                with open("haproxy.cnf.now.txt","r") as new,open("haproxy.cnf.now2.txt","w") as new2:
                                    fla=True
                                    for i in new:
                                        if i.strip().startswith(key1):
                                            fla=False
                                            new2.write(i)  #写入新文件操作
                                            for line in now_list:  #写入now_list
                                                new2.write("\t"+line+"\n")
                                            continue
                                        if i.strip().startswith("backend") and  fla==False:
                                            fla=True
                                            new2.write(i)
                                            continue
                                        if i.strip() and fla==True:
                                            new2.write(i)
                                shutil.copy("haproxy.cnf.now2.txt","haproxy.cnf.now.txt")  #还原配置
                                shutil.copy("haproxy.cnf.now2.txt","haproxy.cnf.txt")      #还原真正线上配置
                        flag=False
                        break
                     #backend存在，recond存在或者不存在
                    else:
                        print("不存在，需要添加,添加成功")
                        with open("haproxy.cnf.txt","r") as old,open("haproxy.cnf.now.txt","w") as new:
                            for i in old:
                                new.write(i)
                        new_a=open("haproxy.cnf.now.txt","a")
                        key2="server"+" "+server+" "+server+" "+"weight"+" "+weight+" "+"maxconn"+" "+maxconn
                        new_a.write("\n"+key1+"\n"+"\t"+key2+"\n")
                        new_a.close()
                        shutil.copy("haproxy.cnf.now.txt","haproxy.cnf.txt")
        else:
            print("你输入的格式不正确，请重新输入字典格式的新增记录")
#增加模块


#删除模块
def delete():
    now_list=[]
    flag=True
    with open("haproxy.cnf.txt","r") as old ,open("haproxy.cnf.delete.txt","w") as new:
        for i in old:
            new.write(i)
    while flag:
        choose=input("（按b返回上一级选择,按q退出整个程序）请输入你要删除的记录：")
        choose=choose.strip()
        #print("输入格式如backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}})
        if choose=="b" or choose=="B":
            print("你选择了返回")
            break
        elif choose=="q" or choose=="Q":
            print("你选择了退出")
            return "f"
        c=json.loads(choose) #json序列化，自动把用户输入的字符串，换成列表或者字典格式
        if  type(c) is dict:
            print("你输入的格式正确")
            backend=c.get("backend")  #获取了backend的值
            record=c.get("record")    #获取了record的值
            server=record.get("server")
            weight=record.get("weight")
            maxconn=record.get("maxconn")
            server=str(server)
            weight=str(weight)
            maxconn=str(maxconn)
            record=str(record)
            backend=str(backend)
            key1="backend"+" "+backend
            key2="server"+" "+server+" "+server+" "+"weight"+" "+weight+" "+"maxconn"+" "+maxconn
            with open("haproxy.cnf.txt","r") as old:
                old=old.read()
                if key1 in  old:
                    print("你要删除的backend在配置文件里，开始删除")
                    with open("haproxy.cnf.delete.txt","r") as d:
                        fla=True
                        for i in d:
                            if i.strip()==key1:
                                fla=False
                                continue
                            if i.strip().startswith("backend") and fla==False:
                                flag=True
                                break
                            if fla==False:
                                now_list.append(i.strip())
                        print(now_list)
                        long=len(now_list)
                        print(long)
                        if key2 in now_list:
                            print("需要删除的记录在record里面")
                            if long==1 or long==0:
                                print("这个backend只有一个实例，全部删除")
                                with open("haproxy.cnf.delete.txt","r") as d,open("haproxy.cnf.delete2.txt","w") as new2:
                                    f=True
                                    for i in d:
                                        if i.strip()==key1:
                                            f=False
                                            continue
                                        if i.strip().startswith("backend") and  f==False:
                                            f=True
                                            new2.write(i)
                                            continue
                                        if i.strip() and f==True:
                                            new2.write(i)
                                shutil.copy("haproxy.cnf.delete2.txt","haproxy.cnf.delete.txt")  #还原配置
                                shutil.copy("haproxy.cnf.delete2.txt","haproxy.cnf.txt")      #还原真正线上配置
                                flag=False
                                break

                            else:
                                print("这个backend有多个实例，指定删除")
                                now_list.remove(key2)  #删除指定的实例之后拿到的数据#{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
                                with open("haproxy.cnf.delete.txt","r") as d,open("haproxy.cnf.delete2.txt","w") as new2:
                                    f=True
                                    for i in d:
                                        if i.strip()==key1:
                                            f=False
                                            #print(i)
                                            new2.write(i)
                                            for i in now_list:
                                                new2.write("\t"+i+"\n")
                                        if i.strip().startswith("backend") and f==False:
                                            f=True
                                            new2.write(i)
                                            continue
                                        if i.strip()and f==True:
                                            new2.write(i)
                                shutil.copy("haproxy.cnf.delete2.txt","haproxy.cnf.delete.txt")  #还原配置
                                shutil.copy("haproxy.cnf.delete2.txt","haproxy.cnf.txt")      #还原真正线上配置
                                flag=False
                                break
                        else:
                            print("需要删除的记录不在record里面")
                            flag=False
                            break
                else:
                    print("你要删除的backend不在配置文件里，无法删除")
        else:
            print("你输入的格式不正确，请重新输入字典格式的新增记录")
#删除模块

#修改模块
def xiugai():
    now_list=[]
    flag=True
    with open("haproxy.cnf.txt","r") as old ,open("haproxy.cnf.xiugai.txt","w") as new:
        for i in old:
            new.write(i)
    while flag:
        choose=input("（按b返回上一级选择,按q退出整个程序）请选择你要修改的项目，1，修改backend  2.修改record: ")
        choose=choose.strip()
        if choose=="1":
            print("你选择了修改backend")
            backend=input("请输入要修改的backend(格式：列如:test.oldboy.org): ")
            backend_xiugai=input("请输入修改完成后的backend(格式：列如:new.oldboy.org): ")
            backend=backend.strip()
            backend_xiugai=backend_xiugai.strip()
            key1="backend"+" "+backend   #要修改的源backend
            key2="backend"+" "+backend_xiugai  #修改好之后的backend
            with open("haproxy.cnf.xiugai.txt","r") as x: #读取haproxy.cnf.xiugai.txt里面的内容，判断key1是否在里面
                x=x.read()
                if key1 in x:
                    print("这个backdend存在，可以修改,修改完毕")
                    with open("haproxy.cnf.xiugai.txt","r") as f,open("haproxy.cnf.xiugai2.txt","w") as f1:
                        flg=True
                        for i in f:
                            if i.strip()==key1:
                                flg=False
                                f1.write(i.replace(key1,key2))     #修改动作
                                continue
                            if i.strip().startswith("backdend") and flg==False:
                                flg=True
                                f1.write(i)
                                continue
                            if flg==True:
                                f1.write(i)
                            if flg==False:
                                f1.write(i)
                    shutil.copy("haproxy.cnf.xiugai2.txt","haproxy.cnf.xiugai.txt")  #还原配置
                    shutil.copy("haproxy.cnf.xiugai2.txt","haproxy.cnf.txt")      #还原真正线上配置
                    flag=False
                    break
                else:
                    print("这个backend不存在，无法修改")
        #修改backend功能结束###########################
        ########修改record功能开始######################
        elif choose=="2":
            li=[]
            print("你选择了修改record")
            backend=input("请输入你要修改的backend(格式:列如:test.oldboy.org): ")
            backend=backend.strip()
            key1="backend"+" "+backend
            with open("haproxy.cnf.xiugai.txt","r") as old:
                 old=old.read()
                 if key1 in old:
                     print("你要修改的backend在配置文件里面，可以修改record")
                     record=input("输入你要修改的record:格式列如:{serve: 100.1.7.9,weight: 20 maxconn: 30}: ")
                     new_record=input("输入你要修改成新的record：")
                     record=json.loads(record)
                     new_record=json.loads(new_record)
                     #拼接原来的record
                     server=record.get("server")
                     weight=record.get("weight")
                     maxconn=record.get("maxconn")
                     server=str(server)
                     weight=str(weight)
                     maxconn=str(maxconn)
                     #拼接新的record
                     new_server=new_record.get("server")
                     new_weight=new_record.get("weight")
                     new_maxconn=new_record.get("maxconn")
                     new_server=str(new_server)
                     new_weight=str(new_weight)
                     new_maxconn=str(new_maxconn)
                     ########################################
                     ###########
                     key2="server"+" "+server+" "+server+" "+"weight"+" "+weight+" "+"maxconn"+" "+maxconn  #输入
                     key3="server"+" "+new_server+" "+new_server+" "+"weight"+" "+new_weight+" "+"maxconn"+" "+new_maxconn
                     ##############
                     with open("haproxy.cnf.xiugai.txt","r") as old:
                          fla=True
                          for i in old: #取出指定的backend下的record值
                              if i.strip()==key1:
                                  fla=False
                                  continue
                              if i.strip().startswith("backend") and fla==False:
                                  fla=True
                                  break
                              if fla==False:
                                  li.append(i.strip())
                     if key2 in li:
                         print("这个record存在，可以修改")
                         li.remove(key2)
                         li.append(key3)
                         with open("haproxy.cnf.xiugai.txt","r") as old,open("haproxy.cnf.xiugai2.txt","w") as new:
                             fal=True
                             for i in old:
                                 if i.strip()==key1:
                                     fal=False
                                     #print(i)
                                     new.write(i)
                                     continue
                                 if i.strip().startswith("backend") and fal==False:
                                     fal=True
                                     #写入当前行
                                     new.write(i)
                                     continue
                                 if fal==True:
                                     new.write(i)
                                 if fal==False:
                                     new.write(i.replace(key2,key3))
                         shutil.copy("haproxy.cnf.xiugai2.txt","haproxy.cnf.xiugai.txt")  #还原配置
                         shutil.copy("haproxy.cnf.xiugai2.txt","haproxy.cnf.txt")      #还原真正线上配置
                         flag=False
                         break
                     else:
                         print("这个record不存在，不可以修改")
                 else:
                     print("你要修改的backend不在配置文件里面，无法修改record")
#修改模块



main()

