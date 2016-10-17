class g:
    def g(self):
        pass


class f(g):
    def f(self):
        pass


obj=f()
r=isinstance(obj,f)  #查看一个对象是不是这个类创建的
print(r)



r=issubclass(f,g)  #判断f是不是g的子类
print(r)