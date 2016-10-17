class f:
    j=111111
    def __init__(self,conunt):
        self.count=conunt
    @property   #取值
    def p(self):
        a1,a2=divmod(self.count,10)
        if a2==0:
            print(a1)
        else:
            a1=a1+1
            print(a1)
    @p.setter  #设置赋值
    def p(self,value):
        print(value)
    @p.deleter #删除
    def p(self):
        print("del")
        pass

# f.j=66666666
# print(f.j)

obj=f(101)
obj.p
obj.p=1
del obj.p
#完全伪造成字段的功能了
'''
这些方法都是由对象调用
具有方法的写作形式
具有字段访问形式
属性只是伪造了字段的那种访问形式而已
'''