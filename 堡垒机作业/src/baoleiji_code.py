import os
import sys
import re
import hashlib
import json
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)

class baoleiji():
    def __init__(self):   #初始化方法，获取mysql的链接信息
        with open(path+"\conf\mysql_connect.txt","r") as conf:
            data=conf.read()
        mysql_ip_list=re.findall(r"mysql_ip=.*",data)
        mysql_port_list=re.findall(r"mysql_port=.*",data)
        mysql_user_list=re.findall(r"mysql_user=.*",data)
        mysql_password_list=re.findall(r"mysql_password=.*",data)
        mysql_ip=mysql_ip_list[-1]
        mysql_port=mysql_port_list[-1]
        mysql_user=mysql_user_list[-1]
        mysql_password=mysql_password_list[-1]
        mysql_ip=re.sub("mysql_ip=","",mysql_ip)
        mysql_port=re.sub("mysql_port=","",mysql_port)
        mysql_user=re.sub("mysql_user=","",mysql_user)
        mysql_password=re.sub("mysql_password=","",mysql_password)
        infor={"mysql_ip":mysql_ip,"mysql_port":mysql_port,"mysql_user":mysql_user,"mysql_password":mysql_password}
        self.infor=infor

    def login_baoleiji(self):
        print(self.infor)


obj=baoleiji()

obj.login_baoleiji()

