#callable()判断某个值是否为函数，不是为False，如果是就为True
#def f1():
    #asdas
#f2=123
#print(callable(f1))
#print(callable(f2))
#r=chr(65)  #已知ASIIC码是65，求实际数字是多少
#print(r)

#n=ord("A")  #已知实际数字是A，求ASSIC码是多少
#rint(n)
#随机验证码
#生成随机数
'''
import random
i=random.randrange(1,100)
print(i)
#65-90 ASSIC码对应A-Z
i=random.randrange(65,90)
i=chr(i)
print(i)
'''
import random  #导入随机模块
li=[]           #定义个空列表
for i in range(6):   #定义循环6次，产生6位的随机验证码
    r=random.randrange(0,5)    #定义产生随机数0-5之间
    if r==1 or r==4:      #如果随机数字是1或者4，那就添加数字到列表
        temp=random.randrange(0,9)
        li.append(str(temp))
    else:                  #如果不是，那就添加字母到列表
        temp=random.randrange(65,91)
        temp=chr(temp)
        li.append(temp)
print(li) #打印当前的列表
li="".join(li)  #字符串的拼接
print(li)


