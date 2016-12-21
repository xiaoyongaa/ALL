class c1:
    def f2(self):
        print("c1")
        pass
class c2:
    def f2(self):
        print("c2")
        pass
class c3(c1,c2):  #第一个优先级最高
    def f3(self):
        pass

obj=c3()
obj.f2()
