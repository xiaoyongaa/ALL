#面向对象有三大特性，封装，继承，多态
class p:
    def __init__(self,name,sex,age,zhan):
        self.name=name
        self.sex=sex
        self.age=age
        self.zhan=zhan
    def caoconxiulian(self):
        zhan=int(self.zhan)-200
        print(zhan)

cangjing=p("仓井","女","18","1000")
print(cangjing.zhan)
cangjing.caoconxiulian()