#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import hashlib
import os
dir_path="E:\\test\\"
def md5(data):
     key=hashlib.md5(bytes("007",encoding="utf-8"))
     key.update(data)
     password=key.hexdigest()
     return password


file_list=[]
file_md5=[]
for root,dirs,files in os.walk(dir_path):
        for i in files:
            file_list.append(root.replace("E:\\test","")+"\\"+i)
print(file_list)


# for i in file_list:
#     with open(i,"rb") as old:
#         print(i)
#         result=md5(old.read())
#         u=i+":"+result
#         file_md5.append(u)
# y=set(file_md5)
# print(y,type(y))






