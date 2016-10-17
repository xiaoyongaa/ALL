old={
    "#1":8,
    "#2":4,
    "#4":2,
}
new={
    "#1":4,
    "#2":4,
    "#3":2,
}
'''
old={5,4,2}
new={4,4,2}
n=old.difference(new)     #删除的值
print(n)                  #删除的值
n=new.difference(old)     #增加的值
print(n)                   #增加的值
n=new.intersection(old)    #更新的值
print(n)
'''
old=set(old.keys())
print(old)

old=set(old)
print(old)