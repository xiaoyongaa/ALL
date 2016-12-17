#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import hashlib
import os

class chayi():
    def __init__(self,old_path,new_path):
        self.old_path=old_path   #定义旧代码的目录
        self.new_path=new_path   #定义新代码的目录

    def md5(self,data):
     key=hashlib.md5(bytes("007",encoding="utf-8"))
     key.update(data)
     result=key.hexdigest()
     return result

    def old_code(self):  #求旧代码的MD5.放在集合里面
        try:
            file_list=[]
            file_md5=[]
            for root,dirs,files in os.walk(self.old_path):
                for i in files:
                    file_list.append(root+"\\"+i)
            for i in file_list:
                with open(i,"rb") as old:
                    result=self.md5(old.read())
                    u=str(i).replace(self.old_path,"")+":"+result
                    file_md5.append(u)
            a=set(file_md5)
            self.old_code_set=a   #旧代码的MD5,拿到集合
            return True
        except Exception as ex:
            print(ex)
            exit()

    def new_code(self):  #求新代码的MD5
        try:
            file_list=[]
            file_md5=[]
            for root,dirs,files in os.walk(self.new_path):
                for i in files:
                    file_list.append(root+"\\"+i)
            for i in file_list:
                with open(i,"rb") as old:
                    result=self.md5(old.read())
                    u=str(i).replace(self.new_path,"")+":"+result
                    file_md5.append(u)
            b=set(file_md5)
            self.new_code_set=b  #新代码的MD5,拿到集合
            return True
        except Exception as ex:
            print(ex)
            exit()

    def  duibi(self):
        res=self.old_code()
        if res:
            res=self.new_code()
            if res:
                  a=self.old_code_set  #老的code
                  b=self.new_code_set  #最新的code
                  c=b.difference(a)   #新代码和旧代码的MD5 求新代码有的，旧代码没有的，差集,就是要更新的代码路径
                  c=str(c).replace("{'","").replace("'}","")
                  msg="最新code下面的{p}{c}发生了更新".format(p=self.new_path,c=c)
                  print(msg)



obj=chayi("E:\\test\\","E:\\test2\\")  #前面第一个参数写旧代码路径,后面第二个路径写信代码路径，开始比较

obj.duibi()