#filter()
#map()
#大于22的，小于22的不要
'''
def f1(args):
    new=[]
    for i in args:
        if i>=22:
            new.append(i)
    return new  #返回结果为筛选后的

li=[1,2,3,4,5,6,22,321,123,22,3213,94902,1,0]
r=f1(li)
print(r)
'''
'''
li=[1,2,3,4,5,6,22,321,123,22,3213,94902,1,0]

r=filter(lambda a:a>=22,li)  #filter,循环第二个参数，让循环的元素执行函数，如果元素符合判断试，就为True
print(list(r))
'''
'''
li=[11,22,33,44,55]
def f1(a):
    l=[]
    for i in a:
        #r=i+100
        l.append(i+100)
    return l

r=f1(li)
print(list(r))
'''
#map(函数，可以迭代的对象（可以for循环的东西)
'''
li=[11,22,33,44,55]
r=map(lambda a:a+100,li)
print(list(r))
'''
li=[11,22,33,44,55]


r=map(lambda a:a+100,li)
print(list(r))









