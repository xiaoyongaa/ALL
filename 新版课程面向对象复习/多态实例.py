#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong

class am():
    def __init__(self,name):
        self.name=name
    def talk(self,obj):
        obj.talk()

    @staticmethod
    def t(a):
        a.talk()



class cat(am):
    def __init__(self,name):
        super(cat,self).__init__(name)  #先继承 后改变 新式类
        self.name=name
        print(self.name)

    def talk(self):

        print("mao")

class dog(am):
    def talk(self):
        print("wang ")


obj=cat("cat")
#u=dog("dog")
# o=am("c")
# o.talk(obj)

h=am("dsadasdsad")
#obj.talk()
am.t(obj)

