import os
import shutil
msg=["1.登录","2.注册"]
k={"key":"g"}
u={"user":"g"}
p={"pas":"g"}
eam={"e":"g"}
pho={"p":"g"}



def mian():
    print("欢迎来到用户管理程序：")
    falg=True
    while falg:
        for i in msg:
            print(i)
        choose=input("请输入你要选择的功能：")
        choose=choose.strip()
        if choose=="1":
            print("你选择了登录")
            r=login()
            if r=="q":
                print("你选择了退出")
                falg=False
                break
        elif choose=="2":
            print("你选择了注册")
            r=zhuche()
            if r=="f":
                falg=False
                break
        elif choose=="q":
            exit("你选择了退出")

#注册模块
def zhuche():
    flag=True
    while flag:
        li=[]
        u=[]
        print("按q退出程序，按b返回上一级菜单")
        user=input("请输入用户名：")
        if user=="q":
            print("你选择了退出，退出程序")
            flag=False
            return "f"
            break
        elif user=="b":
             print("你选择了返回上一级菜单")
             flag=False
             break
        pas=input("请输入密码：")
        emil=input("请输入邮箱地址：")
        phone=input("请输入电话：")
        huiyuan=input("是否开通会员权限,选择(y/n)：")
        user=user.strip()
        pas=pas.strip()
        emil=emil.strip()
        phone=phone.strip()

        if huiyuan=="y":
            huiyuan="y"
        elif huiyuan=="n":
            huiyuan="n"
        else:
            print("你输入的会员权限格式不正确，请重新输入")
            continue
        infor=user+"|"+pas+"|"+emil+"|"+phone+"|"+huiyuan
        if  os.path.exists("db.txt"):
            with open("db.txt","r") as db:
                for i in db:
                    li.append(i.strip().split("|"))
            for i in li:
               u.append(i[0])
            if user in u:
                print("这个用户已经存在，不需要注册")
            else:
                print("这个用户不存在，需要注册,注册完毕")
                with open("db.txt","a") as db:
                    db.write(infor+"\n")
        else:
            with open("db.txt","a") as db:
                db.write(infor+"\n")
            print("这个用户不存在，需要注册,注册完毕")
#注册模块





#验证装饰器模块
#判断账户是否存在，且账户密码是否正确
#def authon(fun):
    #def inner(*args,**kwargs):
#注册模块


def authon(fun):
    def inner(*args,**kwargs):
        flag=True
        li=[]
        us=[]
        us_pas=[]
        us_pas2=[]
        while flag:
            user=input("请输入用户名：")
            pas=input("请输入密码：")
            user=user.strip()
            pas=pas.strip()
            with open("db.txt","r") as db:
                for i in db:
                    li.append(i.strip().split("|"))
            for i in li:
                us.append(i[0])
            if user in us:    #验证用户是否存在
                #print("用户存在")
                key=user+"|"+pas+"|"+"y"
                key2=user+"|"+pas+"|"+"n"
                with open("db.txt","r") as db:
                    for i in db:
                        us_pas.append(i.strip().split("|"))
                for i in us_pas:
                    us_pas2.append(i[0]+"|"+i[1]+"|"+i[-1])
                if key in us_pas2:
                    #print("欢迎会员登录")
                    #获取邮箱电话
                     with open("db.txt","r") as db:
                        for i in db:
                            if i.strip().startswith(user+"|"+pas):
                                li.append(i.strip().split("|"))
                        for i in li:
                            eamil=i[2]
                            phone=i[3]
                    ###
                        k["key"]="y"
                        u["user"]=user
                        p["pas"]=pas
                        eam["e"]=eamil
                        pho["p"]=phone
                elif key2 in us_pas2:
                    #print("欢迎普通用户登录")
                    #获取邮箱电话
                     with open("db.txt","r") as db:
                        for i in db:
                            if i.strip().startswith(user+"|"+pas):
                                li.append(i.strip().split("|"))
                        for i in li:
                            eamil=i[2]
                            phone=i[3]
                    #######################
                        k["key"]="n"
                        u["user"]=user
                        p["pas"]=pas
                        eam["e"]=eamil
                        pho["p"]=phone
                else:
                    print("密码不正确，请重新输入")
                    continue
            #######################
                r=fun(*args,**kwargs)
                return r
            ######################
            else:
                print("用户不存在，请先注册")
                flag=False
                break
    return inner
        #验证装饰器模块
#总登录入口
#是否是会员用户
@authon
def login():
    flag=True
    while flag:
        user=u.get("user")
        key=k.get("key")
        if key=="n":
            print("欢迎你用户%s，普通用户回来"%user)
            r=normal_login()
            if r=="b":
                flag=False
                break
        elif key=="y":
            print("欢迎你%s，VIP用户回来"%user)
            r=vip_login()
            if r=="b":
                flag=False
                break

#总登录入口

##普通用户模块
def normal_login():
    user=u.get("user")
    pas=p.get("pas")
    eamil=eam.get("e")
    phone=pho.get("p")
    li=[]
    flag=True
    msg=["1.修改密码","2.查看本地用户信息"]
    while flag:
        for i in msg:
            print(i)
        choose=input("请输入你要执行的操作：")
        choose=choose.strip()
        if choose=="b":
            return "b"
        elif choose=="q":
            exit("你已经退出")
        if choose=="1":
            print("你选择了修改密码")
            newpas=input("请输入你要修改的密码：")
            newpas=newpas.strip()
            new_infor=user+"|"+newpas+"|"+eamil+"|"+phone+"|"+"n"
            old_infor=user+"|"+pas+"|"+eamil+"|"+phone+"|"+"n"
            with open("db.txt","r") as old,open("db.xiugai.txt","w") as new:
                for i in old:
                    if i.strip()==old_infor:
                        n=i.strip().replace(old_infor,new_infor)
                        print(n)
                        new.write(n+"\n")
                        continue
                    new.write(i)
                print("修改完毕")
            shutil.copy("db.xiugai.txt","db.txt")
            flag=False
            break
        elif choose=="2":
            print("你选择了查看本地用户信息")
            msg='''
            ++++++++++++
            用户名:%s
            密码:%s
            邮箱:%s
            电话:%s
            是否是会员:否
            +++++++++++
            '''%(user,pas,eamil,phone)
            print(msg)
            #flag=False
            break
#普通用户模块

##vip用户模块
def vip_login():
    user=u.get("user")
    pas=p.get("pas")
    eamil=eam.get("e")
    phone=pho.get("p")
    li=[]
    flag=True
    msg=["1.修改密码","2.查看本地用户信息","3.普通用户的操作"]
    while flag:
        for i in msg:
            print(i)
        choose=input("请输入你要执行的操作：")
        choose=choose.strip()
        if choose=="b":
            flag=False
            return "b"
            break
        elif choose=="q":
            exit("你选择了退出")
        if choose=="1":
            print("你选择了修改密码")
            newpas=input("请输入你要修改的密码：")
            newpas=newpas.strip()
            new_infor=user+"|"+newpas+"|"+eamil+"|"+phone+"|"+"y"
            old_infor=user+"|"+pas+"|"+eamil+"|"+phone+"|"+"y"
            with open("db.txt","r") as old,open("db.xiugai.txt","w") as new:
                for i in old:
                    if i.strip()==old_infor:
                        n=i.strip().replace(old_infor,new_infor)
                        new.write(n+"\n")
                        continue
                    new.write(i)
                print("修改完毕")
            shutil.copy("db.xiugai.txt","db.txt")
            flag=False
            break
        elif choose=="2":
            print("你选择了查看本地用户信息")
            msg='''
            ++++++++++++
            用户名:%s
            密码:%s
            邮箱:%s
            电话:%s
            是否是会员:是
            +++++++++++
            '''%(user,pas,eamil,phone)
            print(msg)
            #flag=False
            break
        elif choose=="3":
            print("你选择了普通用户的操作")
            normal_caozuo()
        else:
            print("你输入的选择编号不合法，请重新输入")
#vip模块

#vip操作普通用户
def normal_caozuo():
    flag=True
    msg=["1.删除普通用户","2.增加普通用户","3.修改普通用户密码","4.查看所有普通用户,并搜索普通用户信息","5.提高普通用户权限"]
    while flag:
        for i in msg:
            print(i)
        choose=input("请输入你要操作的项目：")
        choose=choose.strip()
        if choose=="b":
            falg=False
            break
        elif choose=="q":
            exit("你选择了退出")
        if choose=="1":
            print("你选择了删除用户：")
            delete_user()
        elif choose=="2":
            print("你选择了增加用户：")
            adduser()
        elif choose=="3":
            print("你选择了修改普通用户密码：")
            xiugaipass()
        elif choose=="4":
            print("查看所有普通用户,并搜索普通用户信息")
            find()
        elif choose=="5":
            print("提高普通用户权限")
            addvip()
        else:
            print("你选择的操作选项不正确，请重新输入")
#vip操作普通用户


#删除普通用户
def delete_user():
    falg=True
    u=[]
    u2=[]
    with open("db.txt","r") as db:
        for i in db:
            if i.strip().endswith("n"):
                u.append(i.strip().split("|"))
        for i in u:
           u2.append(i[0])
    print("你可以选择删除的当前普通用户",u2)
    while falg:
        user=input("请输入你要删除的普通用户：")
        user=user.strip()
        if user=="b":
            falg=False
            break
        elif user=="q":
            exit("你选择了退出")
        if user in u2:
            print("你要删除的用户合法，是普通用户,删除完毕！！！")
            with open("db.txt","r") as db,open("db.delete.txt","w") as deldte:
                for i in db:
                    if i.strip().startswith(user):
                        continue
                    deldte.write(i)
            shutil.copy("db.delete.txt","db.txt")
            falg=False
            break
        else:
            print("你要删除的用户不合法，是vip用户，无法删除，请重新选择")
#删除普通用户


#####增加用户
def adduser():
    flag=True
    while flag:
        li=[]
        u=[]
        print("按q退出程序，按b返回上一级菜单")
        user=input("请输入用户名：")
        if user=="q":
            exit("你选择了退出，退出程序")
        elif user=="b":
             print("你选择了返回上一级菜单")
             flag=False
             break
        pas=input("请输入密码：")
        emil=input("请输入邮箱地址：")
        phone=input("请输入电话：")
        #huiyuan=input("是否开通会员权限,选择(y/n)：")
        user=user.strip()
        pas=pas.strip()
        emil=emil.strip()
        phone=phone.strip()
        infor=user+"|"+pas+"|"+emil+"|"+phone+"|"+"n"
        if  os.path.exists("db.txt"):
            with open("db.txt","r") as db:
                for i in db:
                    li.append(i.strip().split("|"))
            for i in li:
               u.append(i[0])
            if user in u:
                print("这个用户已经存在，不需要注册")
            else:
                print("这个用户不存在，需要注册,注册完毕")
                with open("db.txt","a") as db:
                    db.write(infor+"\n")
        else:
            with open("db.txt","a") as db:
                db.write(infor+"\n")
            print("这个用户不存在，需要注册,注册完毕")
#####增加用户


###修改普通用户的密码
def xiugaipass():
    falg=True
    u=[]
    u2=[]
    xiugaiuser=[]
    with open("db.txt","r") as db:
        for i in db:
            if i.strip().endswith("n"):
                u.append(i.strip().split("|"))
        for i in u:
           u2.append(i[0])
    print("你可以选择修改密码的当前普通用户",u2)
    while falg:
        user=input("请输入你要修改密码的普通用户：")
        new_pas=input("请选择要修改的密码：")
        user=user.strip()
        new_pas=new_pas.strip()
        if user in u2:
            print("你选择的用户可以被修改密码")
            with open("db.txt","r") as db:
                for i in db:
                    if i.strip().startswith(user):
                        xiugaiuser.append(i.strip().split("|"))
                print(xiugaiuser)
                for i in xiugaiuser:
                    pas=i[1]
                    eamil=i[2]
                    phone=i[3]
            old_infor=user+"|"+pas+"|"+eamil+"|"+phone+"|"+"n"
            new_infor=user+"|"+new_pas+"|"+eamil+"|"+phone+"|"+"n"
            with open("db.txt","r") as old,open("db.xiugaipass.txt","w") as new:
                for i in old:
                    if i.strip()==old_infor:
                        n=i.strip().replace(old_infor,new_infor)
                        new.write(n+"\n")
                        continue
                    new.write(i)
                print("修改完毕")
            shutil.copy("db.xiugaipass.txt","db.txt")
            flag=False
            break

        else:
            print("你选择的用户不是普通用户，请重新选择")
###修改普通用户的密码


###查看模块
def find():
    falg=True
    u=[]
    u2=[]
    u3=[]
    xiugaiuser=[]
    with open("db.txt","r") as db:
        for i in db:
            if i.strip().endswith("n"):
                u.append(i.strip().split("|"))
                u3.append(i.strip())
        for i in u:
           u2.append(i[0])
    print("你可以选择查看信息的普通用户",u2)
    while falg:
        user=input("请输入你要查看信息的普通用户：")
        user=user.strip()
        if user in u2:
            print("你选择的用户可以被查看")
            with open("db.txt","r") as db:
                for i in db:
                    if i.strip().startswith(user):
                        xiugaiuser.append(i.strip().split("|"))
                for i in xiugaiuser:
                    pas=i[1]
                    eamil=i[2]
                    phone=i[3]
            #old_infor=user+"|"+pas+"|"+eamil+"|"+phone+"|"+"n"
            msg='''
            ++++++++++++
            用户名:%s
            密码:%s
            邮箱:%s
            电话:%s
            是否是会员:否
            +++++++++++
            '''%(user,pas,eamil,phone)
            print(msg)
            falg=False
            break
###查看模块




####提高普通用户的权限
def addvip():
    falg=True
    u=[]
    u2=[]
    xiugaiuser=[]
    with open("db.txt","r") as db:
        for i in db:
            if i.strip().endswith("n"):
                u.append(i.strip().split("|"))
        for i in u:
           u2.append(i[0])
    print("你可以选择提升vip权限普通用户",u2)
    while falg:
        user=input("请输入你要提升权限的普通用户：")
        user=user.strip()
        with open("db.txt","r") as db:
                for i in db:
                    if i.strip().startswith(user):
                        xiugaiuser.append(i.strip().split("|"))
                print(xiugaiuser)
                for i in xiugaiuser:
                    pas=i[1]
                    eamil=i[2]
                    phone=i[3]
        old_infor=user+"|"+pas+"|"+eamil+"|"+phone+"|"+"n"
        new_infor=user+"|"+pas+"|"+eamil+"|"+phone+"|"+"y"
        with open("db.txt","r") as old,open("db.addvip.txt","w") as new:
                for i in old:
                    if i.strip()==old_infor:
                        n=i.strip().replace(old_infor,new_infor)
                        new.write(n+"\n")
                        continue
                    new.write(i)
                print("修改完毕")
        shutil.copy("db.addvip.txt","db.txt")
        flag=False
        break
####提高普通用户的权限




mian()

