#s1="i am {0},age {1}".format(*"a",1)
#print(s1)
'''
l={"name":"a","age":"2222"}
s1="i am {name},age{age}".format(**l)
print(s1)
'''
'''
b=1
def show():
    a=123
    print(locals())  #显示局部变量
    print(globals())  #显示全局变量
show()
'''
#s="xiao21yong"

#s=hash(s)
#print(s)
#iter()  #创建迭代器
'''
n="你们"
n=bytes(n,encoding="utf-8")
print(len(n))
'''
#n="你们"
#for i in n:
    #print(i)
'''
max() 最大值
min()最小值
sum()求和
'''
#iter() next()
'''
a=97
n=chr(a)
print(n)

b="b"
b=ord(b)
print(b)
'''
'''
li=[1,2,3]
#li.reverse()
li=reversed(li)
print(list(li))
'''
'''
r=round(1.8)  #四舍五入
print(r)
'''
'''
l1=["alex",11,22,33]
l2=["is",11,22,33]
l3=["sb",11,22,33]

z=zip(l1,l2,l3)
print(type(z))
z=list(z)
print(z)
z=z[0]
print(type(z))
z=" " .join(z)
print(z)


#key=l1[0]+" "+l2[0]+" "+l3[0]
#print(key)
'''
'''
n=bin(1)
print(n)
n=dir("da")
print(n)
'''
'''
s="你好"
b=bytes(s,encoding="utf-8")
print(b)

s=str(b,encoding="utf-8")
print(s)
'''








