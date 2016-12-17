#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import time


def out(func):
    def inner(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(start-end)
        return result
    return inner  #返回内部函数整体内存地址


@out  #test1=out(test1)
def test1():
    time.sleep(1)
    print("test1")

@out  #test2=out(test2)
def test2(name):
    time.sleep(1)
    print("test2",name)
    return "Ok"


#test1()

res=test2([1,2,3])  #inner函数本体
print(res)