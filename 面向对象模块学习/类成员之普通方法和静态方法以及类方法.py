class pro:
    c="中国"
    def __init__(self):
        self.name="xiaoyong"
     #普通方法,由对象去调用。方法属于类
    def show(self):
        print(self.name)
    @staticmethod
    #静态方法属于类。和对象没关系。由类调用执行,静态方法，等于普通函数
    def f1():
        print("ok")
    @classmethod  #类方法,传参至少有cls,把类名自动传递到函数内
    def f2(cls):
        print(cls)
        #cls类名




#pro.f2()#pro.f1()
'''
所有的方法属于类
1.普通方法:至少有个self，对象执行
2.静态方法：任意参数，类执行
3.类方法：至少有一个cls。类执行

'''