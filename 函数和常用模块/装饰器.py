def outer(func):#外圈第一层函数
    def inner():#第二层函数
        print("log")
        func()
        print("log")
    return inner #第一层函数的返回值 赋值给f1
#@+函数名
#功能
#1，自动执行outer函数并且将其下面的函数名f1当做参数传递
#将outer函数的返回值，重新赋值给f1
@outer
def f1():
    print("F1")



'''
def f1():
    print("dsad")


def f2(a):
    a()


f2(f1)
'''
