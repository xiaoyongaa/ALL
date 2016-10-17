age=9
name=["Minglong","minghu","jack",22,age,23,3,4,5,7,87,89,9,9,4]
print(name)
print(name[0:2])   #列表的切片，直接取多个元素，知道下标号码就行
print(name[2:5])   #取jack和age变量
print(name[-5:])   #取最后5个值
name[0]="xxxxx"    #修改其中的一个元素
print(name)
name.insert(1,"mingmao")  #插入一个元素
print(name)
name.append("haha")    #往列表的最后追加一个值
print(name)
name.remove("haha")    #删除一个元素
print(name)
#练习题需求
#写一个列表，列表里包含本组所有成员的名字，往中间位置插入2个临组成员的名字，然后取出第3-8的人的列表
#删除第七个人
#把刚才加入的那2个其它组的人一次性删除
#把组长的名字加上组长备注
n=["Alex",3,5,7,8,9,"jack",1,3,0,9,5,"Rain",1,3,4,7,1,"Eric",1,5,78,3423,4231,"Monica","Fiona",9,4,5,6,1,3]
n.insert(3,4)
n.insert(4,5)
print(n)
print(n[3:8])
n.remove("Monica")
print(n)
del n[3:5]
print(n)
print(n[::2])   #取步长
#print("Alex" in n)
'''
if "Alex" in n:      #断的字符串Alex是否在n列表内
    print("ok")
print(n.count(9))    #统计这n列表一共有几个元素9
需求把9改成99999
'''
if 9 in n:
    print("9在n列表里面")
    c=n.count(9)
    for i in range(c):
        weizhi=n.index(9)
        n[weizhi]="99999"
    print(n)
else:
    print("9不在n列表里面")
#n.reverse() #倒着排序
#print(n)
#name2=["x","e","r"]
#n.extend(name2)   #合并列表方法，扩展表
#print(n)
#n.pop()  #默认删除最后一位
#print(n)
#v=n.copy()
#print(v)
import  copy
#v=copy.deepcopy(n)  #深copy
#print(v)
#找出有多少个9，把它改成999
#找出有多少个34，把它删除
l=[1,2,3,4,5,9,[9,2,34,9],34,34,5,3,1,9]
print(l)
c=l.count(9)
c2=l.count(34)
for i in range(c):
    weizhi=l.index(9)
    l[weizhi]="999"
for i in range(c2):
    l.remove(34)
print(l)
le=l[6]
c=le.count(9)
c2=le.count(34)
for i in range(c):
    weizhi=le.index(9)
    le[weizhi]=999
for i in range(c2):
    le.remove(34)
print(l)






























