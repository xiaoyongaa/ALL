#python的作用域在执行之前已经确定
# name="alex"
# def f1():
#     print(name)
#
#
# def f2():
#     name="dssdasd"
#     f1()
#
#
# f2()
# li=[lambda:x for x in range(10)]
# print(li)
#
#
# res=li[0]()
# print(res)
li=[]
for i in range(10):
    def f1():
        return i
    li.append(f1)

print(li[0]())