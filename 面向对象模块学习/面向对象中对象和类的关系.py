'''
self是什么鬼？
self是一个python自动回给传值的参数，哪个对象执行方法，self就是谁
obj1.insert("sql")   self=obj1
obj2.insert("sql")   self=obj2
'''
#面向对象之构造方法
class F:
    def __init__(self,u,p,ip):
        self.u=u
        self.p=p
        self.ip=ip
    def insert(self,sql):
        print(self.u)
        pass
    def update(self,sql):
        pass
    def delete(self,sql):
        pass
    def selete(self,sql):
        pass

obj1=F("1","2","3")


obj2=F("2222","2","3")


obj2.insert("sql")