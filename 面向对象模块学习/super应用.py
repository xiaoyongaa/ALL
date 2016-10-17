class c1:
    def f1(self):
        print("c1")

class c2(c1):
    def f1(self):
        super(c2,self).f1()  #我要执行当前类的父类的F1方法
        #c1.f1(self)    #我要执行当前类的父类的F1方法
        print("c2")


obj=c2()
obj.f1()