#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import hashlib
def md5(data):  #加密方法
     key=hashlib.md5(bytes("007",encoding="utf-8"))
     key.update(bytes(data,encoding="utf-8"))
     result=key.hexdigest()
     return result

s="a"
res=md5(s)
print(res)