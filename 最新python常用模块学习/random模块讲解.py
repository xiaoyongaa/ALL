#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import random
import string
res=random.random()
print(res)

res=random.randint(1,2)
print(res)

res=random.randrange(1,2)  #不包涵最后一位2
print(res)



t=string.ascii_letters+string.digits+string.ascii_lowercase
res=random.sample(t,6)  #从100里面随机生成2位
print(res)
#res=str(res).replace("['","").replace("']","").replace("'","").replace(",","").replace(" ","")
print(res)


