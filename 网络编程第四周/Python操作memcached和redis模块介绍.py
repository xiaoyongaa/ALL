'''
1.安装软件
2.本地安装模块

'''

# import memcache
# memcache_ip=["10.0.0.25:12000"]
#
# # #set方法永远不会报错
# mc=memcache.Client(memcache_ip,debug=True)
# mc.set("foo","bar")   #设置一个键值对
# ret=mc.get("foo")  #取出
# print(ret)
#
# #增加键值对方法
# #mc.add("fo",1)
# #假设增加的重复。就报错
#
# #修改键值对方法
# mc.replace("foo",123)
# ret=mc.get("foo")
# print(ret)
# #修改键值对方法 #假设修改的重复。就报错
#
# #set方法永远不会报错
# mc.set("foo","aaaaa")
# ret=mc.get("foo")
# mc.set_multi({"foo":111,"gggg":2222})
# ret=mc.get("foo")
# print(ret)
# #存在就修改。不存在就添加


##
import memcache
memcache_ip=["10.0.0.25:12000"]
mc=memcache.Client(memcache_ip,debug=True)
v = mc.gets('product_count')
mc.cas('product_count', "8919")
# ...
# 如果有人在gets之后和cas之前修改了product_count，那么，下面的设置将会执行失败，剖出异常，从而避免非正常数据的产生
mc.cas('product_count', "899")
#v=mc.gets("foo")
#mc.cas("foo","12222222")
