#成员修饰符
#私有的成员
#只能自己类本身进行访问
class f:
    __c=123
    def __init__(self,name):
        self.__name=name     #加2个下划线变成私有的成员
    def show(self):
        print(self.__name)
    @staticmethod
    def g():
        print(f.__c)

obj=f("xiaoyong")
#print(obj._f__name)  #强制查看私有成员
#obj.show()
#print(obj.__name)
#obj.g()
f.g()
'''
四 成员修饰符
私有
之一类自己本身成员可以访问
公有
都能访问
'''
