def outer(fu):
    def inner(*args,**kwargs):  #原来函数传参几个，装饰器的函数就要要几个传参
        print("bro")
        R=fu(*args,**kwargs)   #取得原函数的返回值
        print("after")
        return R   #原函数的返回值返回给inner
    return inner


@outer
def f1(a):
    print(a)
    return "1111111111"


@outer
def f2(a,b):
    print("F2")
    return "222222222"



