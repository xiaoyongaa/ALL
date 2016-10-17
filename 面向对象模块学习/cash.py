class c1:
    def f1(self):
        print("f1")
class c2(c1):
    def f1(self):
        super(c2,self).f1()
        print("f2")



obj2=c2()
print(obj2.f1())
