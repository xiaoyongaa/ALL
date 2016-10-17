class f:
    def __iter__(self):
        yield "xiaoyong"
        yield 2



obj=f()
for i in obj:   #对象要经过__iter__函数加工，才能被迭代
    print(i)



#对象之所以能被循环。是因为内部有__iter__迭代函数进行加工
#出现yield就是生成器