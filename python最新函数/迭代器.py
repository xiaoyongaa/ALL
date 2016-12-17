#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
from collections import Iterable,Iterator
# a=[i+2 for i in range(10000000000)]
# for i in a:
#     print(i)
li=[1,2,3]  #迭代对象
li=iter(li)  #迭代器
print(type(li),li)
print(li.__next__())
for i in li:
    print(i,type(i))
# print(li.__next__())  #迭代器

# b=(i+2 for i in range(10))  #生成器
# print(b,type(b))  #只有迭代器有__next__方法
# print(b.__next__()) #只有迭代器有__next__方法
# res=isinstance(li,Iterable)
# print(res)
# while True:
#     i=b.__next__()
#     print(i)

# print(b,type(b))
# for i in b:
#     print(i)