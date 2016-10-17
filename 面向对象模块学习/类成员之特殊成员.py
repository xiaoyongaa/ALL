class f:
    def __init__(self,name):
        self.name=name
    #def __del__(self):   #析构方法
        #pass
    def __call__(self, *args, **kwargs):
        print("call")
    def __str__(self):
        return "名字是{name}".format(name=self.name)
# o=f()
# print(o.__class__)
# o() #对象后面加括号,执行call方法
obj=f("xiaoyong")
print(obj)

ret=obj.__dict__  #把对象里面的字段全部取出来，放在字典里面###非常重要
print(ret)