#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import time,datetime
#print(time.altzone)
res=time.localtime()
print(res)
# res=time.time()
# print(res)


res=time.mktime(res)
print(res)



res=time.localtime(res)
print(res)
h=time.strftime("%Y_%m_%d_%H_%M_%S",res)
print(h)



print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta(days=3))

now=datetime.datetime.now()
y=now.replace(month=1,year=1998)  #时间替换
print(y)













