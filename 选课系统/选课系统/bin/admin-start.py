import os
import sys
import pickle
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
os.chdir(path)
from src import admin
all_kecheng=pickle.load(open("db/kecheng.txt","rb"))
all_teacheer=pickle.load(open("db/teacher.txt","rb"))
def login():
    falg=True
    msg=["1.删除课程","2.删除老师"]
    while falg:
        for i in msg:
            print(i)
        choose=input("请选择你要删除的项目(按q退出)：")
        choose=choose.strip()
        if choose=="1":
            print("你选择了删除课程: ")
            delate_kecheng()
        elif choose=="2":
            print("你选择了删除老师")
            delate_teache()
        elif choose=="q":
            exit("你选择了退出程序")
        else:
            print("你输入的操作编号不正确，请重新输入")

def delate_kecheng():
    falg=True
    while falg:
        for i in all_kecheng:
            print(i.name)
        choose=input("请选择你要删除的课程(按b返回上一级，按q退出): ")
        choose=choose.strip()
        if choose=="1":
            print("你选择了删除鸡汤课")
            all_kecheng[0].delete()
            pickle.dump([all_kecheng[0],all_kecheng[1],all_kecheng[2]],open("db/kecheng.txt","wb"))
            msg="删除鸡汤课成功！！"
            print(msg)
        elif choose=="2":
            print("你选择了删除python自动化开发课")
            all_kecheng[1].delete()
            pickle.dump([all_kecheng[0],all_kecheng[1],all_kecheng[2]],open("db/kecheng.txt","wb"))
            msg="删除python自动化开发课成功！！"
            print(msg)
        elif choose=="3":
            print("你选择了删除linux运维课")
            all_kecheng[2].delete()
            pickle.dump([all_kecheng[0],all_kecheng[1],all_kecheng[2]],open("db/kecheng.txt","wb"))
            msg="删除linux运维课成功！！"
            print(msg)
        elif choose=="q":
            exit("你选择了退出程序")
        elif choose=="b":
            print("你选择了返回上一级")
            falg=False
            break


def delate_teache():
    falg=True
    while falg:
        for i in all_teacheer:
            print(i.name)
        choose=input("请选择你要删除的老师(按b返回上一级，按q退出): ")
        choose=choose.strip()
        if choose=="1":
            print("你选择了删除Alex")
            all_teacheer[0].delete()
            pickle.dump([all_teacheer[0],all_teacheer[1],all_teacheer[2]],open("db/teacher.txt","wb"))
            msg="删除Alex成功！!"
            print(msg)
        elif choose=="2":
            print("你选择了删除wusir")
            all_teacheer[1].delete()
            pickle.dump([all_teacheer[0],all_teacheer[1],all_teacheer[2]],open("db/teacher.txt","wb"))
            msg="删除wusir成功！！"
            print(msg)
        elif choose=="3":
            print("你选择了删除oldboy！！")
            all_teacheer[2].delete()
            pickle.dump([all_teacheer[0],all_teacheer[1],all_teacheer[2]],open("db/teacher.txt","wb"))
            msg="删除oldboy成功！！"
            print(msg)
        elif choose=="q":
            exit("你选择了退出程序")
        elif choose=="b":
            print("你选择了返回上一级")
            falg=False
            break

login()
