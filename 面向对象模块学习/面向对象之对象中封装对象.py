class c1:
    def __init__(self,name,age,obj):
        self.name=name
        self.age=age
        self.obj=obj
        print(name,age)

class c2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(name,age)
    def show(self):
        print(self.name)
        return 321321321321321321321
class c3:
    def __init__(self,a1):
        self.momey=123
        self.aaa=a1

obj2=c2(3,2)
obj1=c1(1,2,obj2)
obj3=c3(obj1)
print(obj3.aaa.obj.show())
