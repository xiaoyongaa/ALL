#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import os,sys,re,json,shutil
path=os.path.abspath(__file__)
print(path)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
print(path)


#l={"backend":"www.oldboy.org","server":"192.168.1.1","weight":"1","maxconn":"2"}

#os.remove("E:\修改配置文件\conf\haproxy.cnf.txt")
