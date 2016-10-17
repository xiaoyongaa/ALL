import pickle
import sys
import os
import logging
import time
import datetime
time=datetime.date.today()
time=str(time)
time=time.replace("-","_")
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
os.chdir(path)
#print(os.getcwd())
from src import admin
all_kecheng=pickle.load(open("db/kecheng.txt","rb"))
all_teacheer=pickle.load(open("db/teacher.txt","rb"))
def log(name,path,message):
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #文件输出Handler
    os.chdir(path)
    fh=logging.FileHandler(time+".log")
    fh.setLevel(logging.DEBUG)
    #指定日志格式
    formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    #Formatter注册给Handler
    fh.setFormatter(formatter)
    #Handler注册给logeer
    logger.addHandler(fh)
    ######################
    logger.info(message)
class stdent:
    def __init__(self,user,pas,sex,age,kecheng1,kecheng2,kecheng3):
        self.user=user
        self.pas=pas
        self.sex=sex
        self.age=age
        self.kecheng1=kecheng1
        self.kecheng2=kecheng2
        self.kecheng3=kecheng3
    def chaping(self):
        flag=True
        msg=["1.Alex","2.wusir","3.oldboy"]
        while flag:
            for i in msg:
                print(i)
            choose=input("目前老师是这三位，请选择老师的编号进行差评(按b返回上一层选择,按q退出整个程序)：")
            choose=choose.strip()
            if choose=="1" and all_teacheer[0].stat==0:
                print("你选择了差评Alex")
                self.kecheng1.obj.chaping()
                new=[self.kecheng1.obj,self.kecheng2.obj,self.kecheng3.obj]
                pickle.dump(new,open("db/teacher.txt","wb"))
                new=[self.kecheng1,self.kecheng2,self.kecheng3]
                pickle.dump(new,open("db/kecheng.txt","wb"))
                print("alex 现在有{c}元".format(c=self.kecheng1.obj.momeny))
            elif choose=="b":
                print("返回上一层选择")
                falg=False
                break
            elif choose=="q":
                exit("你选择了退出整个程序")
            elif choose=="2" and all_teacheer[1].stat==0:
                print("你选择了差评wusir")
                self.kecheng2.obj.chaping()
                new=[self.kecheng1.obj,self.kecheng2.obj,self.kecheng3.obj]
                pickle.dump(new,open("db/teacher.txt","wb"))
                new=[self.kecheng1,self.kecheng2,self.kecheng3]
                pickle.dump(new,open("db/kecheng.txt","wb"))
                print("wusir现在有{c}元".format(c=self.kecheng2.obj.momeny))
            elif choose=="3" and all_teacheer[2].stat==0:
                print("你选择了差评oldboy")
                self.kecheng3.obj.chaping()
                new=[self.kecheng1.obj,self.kecheng2.obj,self.kecheng3.obj]
                pickle.dump(new,open("db/teacher.txt","wb"))
                new=[self.kecheng1,self.kecheng2,self.kecheng3]
                pickle.dump(new,open("db/kecheng.txt","wb"))
                print("oldboy现在有{c}元".format(c=self.kecheng3.obj.momeny))
            else:
                print("你选择的老师已经被删除！！不在范围内，请重新输入")
    def xuanzhe_jitang(self):
        falg=True
        msg=["1.上课","2.查看已经选择的课程","3.查看上课记录","4.差评指定老师"]
        while falg:
            for i in msg:
                print(i)
            choose=input("请输入你要操作的选项(按b返回上一层选择,按q退出整个程序)：")
            choose=choose.strip()
            if choose=="1":
                print("你选择了上课，现在开始上课！")
                self.kecheng1.shangke()
                new=[self.kecheng1.obj,self.kecheng2.obj,self.kecheng3.obj]
                pickle.dump(new,open("db/teacher.txt","wb"))
                new=[self.kecheng1,self.kecheng2,self.kecheng3]
                pickle.dump(new,open("db/kecheng.txt","wb"))
                print("Alex现在有{c}元".format(c=self.kecheng1.obj.momeny))
                log("上鸡汤课成功！！","db/","上鸡汤课成功！！")
                os.chdir(path)
            elif choose=="b":
                print("返回上一层选择")
                falg=False
                break
            elif choose=="q":
                exit("你选择了退出整个程序")
            elif choose=="2":
                with open("db/jilu.txt","r") as n:
                    for i in n:
                        print(i.strip())
            elif choose=="3":
                with open("db/"+time+".log","r") as n:
                    for i in n:
                        print(i.strip())
            elif choose=="4":
                print("你选择了差评指定老师")
                self.chaping()
            else:
                print("你选择的操作编号不在范围内，请重新输入")
    def python(self):
        falg=True
        msg=["1.上课","2.查看已经选择的课程","3.查看上课记录","4.差评指定老师"]
        while falg:
            for i in msg:
                print(i)
            choose=input("请输入你要操作的选项(按b返回上一层选择,按q退出整个程序)：")
            choose=choose.strip()
            if choose=="1":
                print("你选择了上课，现在开始上课！")
                self.kecheng2.shangke()
                new=[self.kecheng1.obj,self.kecheng2.obj,self.kecheng3.obj]
                pickle.dump(new,open("db/teacher.txt","wb"))
                new=[self.kecheng1,self.kecheng2,self.kecheng3]
                pickle.dump(new,open("db/kecheng.txt","wb"))
                print("wusir现在有{c}元".format(c=self.kecheng2.obj.momeny))
                log("上python自动化开发课成功！！","db/","上python自动化开发课成功！！")
                os.chdir(path)
            elif choose=="b":
                print("返回上一层选择")
                falg=False
                break
            elif choose=="q":
                exit("你选择了退出整个程序")
            elif choose=="2":
                with open("db/jilu.txt","r") as n:
                    for i in n:
                        print(i.strip())
            elif choose=="3":
                with open("db/"+time+".log","r") as n:
                    for i in n:
                        print(i.strip())
            elif choose=="4":
                print("你选择了差评指定老师")
                self.chaping()
            else:
                print("你选择的操作编号不在范围内，请重新输入")
    def linux(self):
        falg=True
        msg=["1.上课","2.查看已经选择的课程","3.查看上课记录","4.差评指定老师"]
        while falg:
            for i in msg:
                print(i)
            choose=input("请输入你要操作的选项(按b返回上一层选择,按q退出整个程序)：")
            choose=choose.strip()
            if choose=="1":
                print("你选择了上课，现在开始上课！")
                self.kecheng3.shangke()
                new=[self.kecheng1.obj,self.kecheng2.obj,self.kecheng3.obj]
                pickle.dump(new,open("db/teacher.txt","wb"))
                new=[self.kecheng1,self.kecheng2,self.kecheng3]
                pickle.dump(new,open("db/kecheng.txt","wb"))
                print("oldboy现在有{c}元".format(c=self.kecheng3.obj.momeny))
                log("上linux运维课成功！！","db/","上linux运维课成功！！")
                os.chdir(path)
            elif choose=="b":
                print("返回上一层选择")
                falg=False
                break
            elif choose=="q":
                exit("你选择了退出整个程序")
            elif choose=="2":
                with open("db/jilu.txt","r") as n:
                    for i in n:
                        print(i.strip())
            elif choose=="3":
                with open("db/"+time+".log","r") as n:
                    for i in n:
                        print(i.strip())
            elif choose=="4":
                print("你选择了差评指定老师")
                self.chaping()
            else:
                print("你选择的操作编号不在范围内，请重新输入")
    def longin(self):
        falg=True
        all_kecheng_list=[self.kecheng1.name,self.kecheng2.name,self.kecheng3.name]
        while falg:
            for i in all_kecheng_list:
                print(i)
            choose=input("请输入你要选择的课程(按q直接退出)：")
            choose=choose.strip()
            if choose=="1" and all_kecheng[0].stat==0:
                print("你选择了鸡汤课")
                with open("db/jilu.txt","a") as n:
                    n.write("鸡汤课"+"\n")
                self.xuanzhe_jitang()
            elif choose=="2" and all_kecheng[1].stat==0:
                print("你选择了python自动化开发课")
                with open("db/jilu.txt","a") as a:
                    a.write("python自动化开发课"+"\n")
                self.python()
            elif choose=="3" and all_kecheng[2].stat==0:
                print("你选择了linux运维")
                with open("db/jilu.txt","a") as a:
                    a.write("linux运维课"+"\n")
                self.linux()
            elif choose=="q":
                exit("你选择了退出，直接退出")
            else:
                print("你选择的课程已经被删除，不在范围内，请重新输入")



zhangshang=stdent("张三","123","男","21",all_kecheng[0],all_kecheng[1],all_kecheng[2])
lisi=stdent("李四","123","男","22",all_kecheng[0],all_kecheng[1],all_kecheng[2])

zhangshang.longin()





