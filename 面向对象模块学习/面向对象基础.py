#函数式编程
'''
def mail(meage):
    print(meage)
mail("ok")
'''

#面向对象编程
#面向对象有2个基本概念：类，对象
class F:
    #类里面的函数叫做方法
    def mail(self,meage):
        print(meage)
print(type(F))
#要想调用函数（类里面的方法）
#调用需要2步，1创建对象名字 2通过对象的方法去执行mail函数
#创建对象名字
obi=F()   #obi是个对象
print(type(obi))
obi.mail("ok")   #通过对象的方法去执行mail函数