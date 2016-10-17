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
new_old=set(old.keys())
new_new=set(new.keys())
add=new_new.difference(new_old) #需要增加的信息
remove=new_old.difference(new_new) #需要删除的信息
upadte=new_new.intersection(new_old)

print(add)
print(remove)
print(upadte)



