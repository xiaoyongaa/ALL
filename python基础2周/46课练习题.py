import os
def main():
    while True:
        i=input("1:登录 2:注册")
        i=i.strip()
        if i=="1":
            print("你选择了登录，请输入信息:")
            login()
        elif i=="2":
            print("你选择了注册，请输入信息")
            y=regist()
            if y=="y":
                print("注册成功")
            else:
                print("注册失败")

def regist():
    #注册
 try:
    u=input("请输入用户名:")
    p=input("请输入密码：")
    u=u.strip()
    p=p.strip()
    #用户名密码写入文件
    n=open("db.txt","a")
    u=str(u)
    p=str(p)
    n.write(u+"|"+p+"\n")
    n.close()
    n=open("db.txt").read()
 except:
    return "no"
 else:
     return "y"


def login():
    #登录
    u=input("请输入用户名:")
    p=input("请输入密码：")
    u=u.strip()
    p=p.strip()
    if os.path.exists("db.txt"):
        f=open("db.txt","r")
        for line in f:
            line=line.strip().split("|")   #重要思想去空格，去换行
            if line[0]==u and line[1]==p:
                print("你输入的账户名和密码正确")
            else:
                print("你输入的账户名和密码错误，重新输入")

main()










