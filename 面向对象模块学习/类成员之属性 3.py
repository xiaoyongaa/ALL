class p:
    def __init__(self,c):
        self.c=c
    def f1(self):
        return 123
    def f2(self,v):
        print(v)
    def f3(self):
        print("ok")
    f=property(fget=f1,fset=f2,fdel=f3)


x=p(101)

r=x.f
print(r)

x.f="xiaoyong"


del x.f