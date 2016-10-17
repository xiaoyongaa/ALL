#什么时候用面向对象？
#当函数有共同的参数，就可以使用面向对象的方式，将参数一次性封装到对象中,以后去对象中取值
#函数式编程
'''
def inster(user,pas,ip,sql):
    print(user,pas,ip,sql)
    pass
def upadte(user,pas,ip,sql):
    print(user,pas,ip,sql)
    pass
def delete(user,pas,ip,sql):
    print(user,pas,ip,sql)
    pass
def xiugai(user,pas,ip,sql):
    print(user,pas,ip,sql)
    pass
inster(1,2,3,4)
'''
#面向对象编程
#当函数有共同的参数，就可以使用面向对象的方式，将参数一次性封装到对象中,以后去对象中取值
class mysql:
    def inster(self,sql):
        user=str(print(self.u))
        pas=str(print(self.p))
        ip=str(print(self.ip))
        print(user,pas,ip,type(user),type(pas),type(ip))
        pass
    def upadte(self,sql):

        pass
    def delete(self,sql):

        pass
    def xiugai(self,sql):

        pass

obj=mysql()
obj.u="xiaoyong"
obj.p="123"
obj.ip="192.168.1.3"
obj.inster("sql")



