#li=[11,22,33,44,55,66]
#r=filter(lambda a:a>33,li)
#print(list(r))
def func():
    print(1111)
    yield 1
    print(2222)
    yield 2
    yield 3

re=func()
r1=re.__next__()  #j进入函数找到yield，获取yield后面的数据
print(r1)
r1=re.__next__()  #
print(r1)
r1=re.__next__()  #
print(r1)
r1=re.__next__()  #
print(r1)