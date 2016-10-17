from back.code import g
class p(g):
    def f1(self):
        print("before")
        super(p,self).f1()   #主动执行父类的f1方法
        print("after")


