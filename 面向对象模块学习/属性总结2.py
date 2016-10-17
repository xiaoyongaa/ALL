class f:
    g=123
    def __init__(self):
        self.c=1
    def f1(self):
        print("get")
    def f2(self,value):
        print("set")
    def f3(self):
        print("delete")
    cls=property(fget=f1,fset=f2,fdel=f3)


l=f() #创建一个对象
print(l.c)
del l.cls
#完全伪造成字段的功能了
'''
这些方法都是由对象调用
具有方法的写作形式
属性就是一种特殊的方法，以字段的形式访问
具有字段访问形式
属性只是伪造了字段的那种访问形式而已
'''