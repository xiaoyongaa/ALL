#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
list_1="dssadasdbbbbbbbb"
list_2="asdkkasd"
h=set(list_1)
h2=set(list_2)
print(h,h2)



g=h.intersection(h2)  #求交集
print(g)


u=h.union(h2)  #求并集
print(u)


#求差集  h里面有,h2里面没有的
d=h.difference(h2)
print(d)

#求子集
b=h.issubset(h2)
print(b)

#父集
print(h.issuperset(h2))


#
list_3="asdkb"

print(h.issubset(list_3))



#把2个集合里面都没有的取出来

print(h.symmetric_difference(h2))









