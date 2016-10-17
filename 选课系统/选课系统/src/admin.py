import pickle
import os
import sys
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
os.chdir(path)

class teacher:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
        self.momeny=0
        self.stat=0
    def chaping(self):
        self.momeny=self.momeny-100
        msg="差评成功,{name}老师扣钱100块!!!".format(name=self.name)
        print(msg)
    def delete(self):
        self.stat=1

if os.path.exists("db/teacher.txt"):
    pass
else:
    alex=teacher("1.ALEX","男","28")
    wusir=teacher("2.wusir","男","29")
    oldboy=teacher("3.oldboy","男","33")
    pickle.dump([alex,wusir,oldboy],open("db/teacher.txt","wb"))

class kecheng:
    def __init__(self,name,time,cash,laoshi,obj):
        self.name=name
        self.time=time
        self.cash=cash
        self.laoshi=laoshi
        self.obj=obj
        self.stat=0
    def shangke(self):
        self.obj.momeny=self.cash+self.obj.momeny
        msg="上课{name}成功,{laoshi}老师成功获取{cash}元!!!".format(name=self.name,laoshi=self.obj.name,cash=self.cash)
        print(msg)
    def delete(self):
        self.stat=1
if os.path.exists("db/kecheng.txt"):
    pass
else:
    all_teacher=pickle.load(open("db/teacher.txt","rb"))  #读取老师信息
    jitangke=kecheng("1.鸡汤课","2016/9/28",100,all_teacher[0].name,all_teacher[0])
    python=kecheng("2.python自动化开发","2016/9/29",500,all_teacher[1].name,all_teacher[1])
    linux=kecheng("3.linux运维","2016/9/30",600,all_teacher[2].name,all_teacher[2])
    pickle.dump([jitangke,python,linux],open("db/kecheng.txt","wb")) #保存课程信息






