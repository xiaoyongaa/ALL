#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
class s():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def y(self):
        print("学习")




class y(s):
    def __init__(self,name,age):
        #s.__init__(self,name,age)   #先继承下父类，然后重新构造  经典类写法
        super(y,self).__init__(name,age)  #新式类
        self.name=name
        self.age=age

    def b(self):
        print(self.name)






obj=s("xiaoyong","25")
obj.y()
#
obj2=y("sad","100")
obj2.b()