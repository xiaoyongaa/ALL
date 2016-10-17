class f:
    __stat=1
    def __init__(self,c):
        self.__c=c
    def f1(self):
        print(self.__c)
    @staticmethod
    def f2():
        print(f.__stat)

class h(f):   #私有的只有本身才可以访问
    def f2(self):
        #print(self.__c)
        print(1222)


#print(f.__stat)
#obj=f("1")
#obj.f2()
f.f2()

# obj=f("1")
# obj.f1()
b=h("31231")
b.f2()
