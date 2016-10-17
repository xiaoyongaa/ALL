import os
msg=["1.后台管理","2.登录","3.注册"]

#主入口
def main():
    flag=True
    while  flag:
        for i in msg:
            print(i)
        choose=input("请输入你要进入的模块：")
        choose=choose.strip()
        if choose=="1":
            print("你选择了后台管理")
            print("你选择了登录")
            user=input("请输入用户名：")
            pas=input("请输入密码：")
            user=user.strip()
            pas=pas.strip()
            guanli(user,pas)
        elif choose=="2":
            print("你选择了登录")
            user=input("请输入用户名：")
            pas=input("请输入密码：")
            user=user.strip()
            pas=pas.strip()
            login(user,pas)
        elif choose=="3":
            print("你选择了注册")
            zhuche()
        elif choose=="q" or choose=="quit":
            print("你选择了退出")
            flag=False
            break
#主入口

#注册
def zhuche():
    flag=True
    l=[]
    while flag:
        user=input("请输入注册的用户名：")
        pas=input("请输入注册的密码：")
        user=user.strip()
        pas=pas.strip()
        user=str(user)
        pas=str(pas)
        if user==pas:
            print("账户名和密码不能相同，请重新输入")
        else:
            if os.path.exists("db.txt"):
                with open("db.txt","r") as db:
                    for i in db:
                       l.append(i.strip().split("|"))
                l=dict(l)
                l=list(l.keys())
                if user in l:
                    print("该账户已经存在，请重新注册")
                    l=[]
                else:
                    print("该账户不存在，可以注册")
                    with open("db.txt","a+") as db:
                        db.write(user+"|"+pas+"\n")
                        print("你已经注册成功")
                        flag=False
                        break
            else:
                with open("db.txt","a+") as db:
                    db.write(user+"|"+pas+"\n")
                    print("你已经注册成功")
                    flag=False
                    break
#注册

#认证装饰器
def renzheng1(fu):
    def renzheng2(user,pas):
        li=[]
        with open("db.txt","r") as db:
           for i in db:
               li.append(i.strip().split("|"))
        li=dict(li)
        li=list(li.keys())
        if user in li:
            print("注册过的用户")
            li2=[]
            with open("db.txt","r") as db:
               for i in db:
                   li2.append(i.strip().split("|"))
            li2=dict(li2)
            pas2=li2.get(user)
            if pas==pas2:
                print("用户名密码正确，进入系统")
                r=fu(user,pas)
                return r
            else:
                print("密码错误，不能进入系统")
        else:
            print("为注册过的用户，请先注册再登录")
    return renzheng2
##


#登录
@renzheng1
def login(user,pas):
    print("进入了系统，欢迎！！！！！！！！！！")
#登录

##
@renzheng1
def guanli(user,pas):
    print("你进入了管理系统，欢迎！！！！！！！！！！！！！！！！")


main()



