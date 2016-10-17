class f1:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
    def long(self):
        print("jdsakjdkjsadkjsakjd")
    def l(self):
        print(self.age)

class f2(f1):
    def __init__(self,age):
        self.age=age
    def show(self):
        print("fw")


obj1=f1(1)
obj2=f2("213213213213213213213")
obj1.show()
obj1.long()
obj2.l()   #f2类继承了f1类，所以f2里面的所有方法包含f1类里面的
