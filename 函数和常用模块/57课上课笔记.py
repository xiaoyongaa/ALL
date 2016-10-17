def myrange(arg):
    start=0
    while True:
        if start>arg:
            return
        yield start  #生成器
        start+=1


ret=myrange(3)  #迭代器
for i in ret:
    print(i)



'''
r=ret.__next__()
print(r)
r=ret.__next__()
print(r)
r=ret.__next__()
print(r)
r=ret.__next__()
print(r)
#r=ret.__next__()
#print(r)
'''



