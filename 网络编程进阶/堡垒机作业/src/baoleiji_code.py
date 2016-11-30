import os
import sys
import re
import hashlib
import pymysql
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
key=hashlib.md5(bytes("007",encoding="utf-8"))

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
        falg=True
        while falg:
            msg="欢迎来到堡垒机系统！！"
            print(msg)
            msg=["1:注册","2.登录"]
            for i in msg:
                print(i)
            choose=input("请选择你要执行操作的编号:").strip()
            if choose=="1":
                print("你选择了注册")
                self.zhuche()
                break
            elif choose=="2":
                print("你选择了登录")
                self.longin()
                break
            elif len(choose)==0:
                continue
            else:
                print("你输入的执行操作编号错误,请重新输入")
                continue

    def zhuche(self):
        print("注册模块")
        falg=True
        print(self.infor)
        mysql_ip=self.infor.get("mysql_ip")
        mysql_port=int(self.infor.get("mysql_port"))
        mysql_user=self.infor.get("mysql_user")
        mysql_password=self.infor.get("mysql_password")
        while falg:
            try:
                username=input("请输入你要注册的名字:").strip()
                password=input("请输入该注册用户的密码:").strip()
                if len(password)==0 or len(username)==0:
                    print("用户名或者密码不能为空,请重新输入!")
                    continue
                key.update(bytes(password,encoding="utf-8"))
                password=key.hexdigest()
                connect=pymysql.connect(host=mysql_ip,port=mysql_port,user=mysql_user,passwd=mysql_password)
                cursor=connect.cursor(cursor=pymysql.cursors.DictCursor)
                sql="insert into baoleiji.baoleiji_user(name,passworld) values('{name}','{password}')".format(name=username,password=password)
                hangshu=cursor.execute(sql)
                connect.commit()
                connect.close()
                cursor.close()
                print("注册完毕")
                choose=input("继续注册按回车,注册完毕按b返回主页面:")
                if choose=="b":
                    self.login_baoleiji()
            except Exception as ex:
                print(ex)
                print("用户名已经存在！重新输入")

    def longin(self):
        print("这里是登录模块")

    def main(self):
        result=self.login_baoleiji()


obj=baoleiji()

obj.main()

