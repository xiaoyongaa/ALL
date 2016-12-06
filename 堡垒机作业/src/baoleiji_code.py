import os
import paramiko
import socket
import sys
import re
import hashlib
import pymysql
from paramiko.py3compat import u
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
                key=hashlib.md5(bytes("007",encoding="utf-8"))
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


    def longin(self):
        print("这里是登录模块")
        falg=True
        mysql_ip=self.infor.get("mysql_ip")
        mysql_port=int(self.infor.get("mysql_port"))
        mysql_user=self.infor.get("mysql_user")
        mysql_password=self.infor.get("mysql_password")
        while falg:
            username=input("请输入你要登录的姓名:").strip()
            password=input("请输入你要登录的密码:").strip()
            if len(username)==0 or len(password)==0:
                print("用户名或密码不能为空,重新输入")
                continue
            connect=pymysql.connect(host=mysql_ip,port=mysql_port,user=mysql_user,passwd=mysql_password)
            cursor=connect.cursor(cursor=pymysql.cursors.DictCursor)
            sql="select name from baoleiji.baoleiji_user where name='{name}'".format(name=username)
            cursor.execute(sql)
            data=cursor.fetchall()
            print(data)
            if data==():
                #print("该用户未注册,请重新输入(按b返回上一级菜单)")
                choose=input("该用户未注册,请重新输入(按回车继续输入，按b返回上一级菜单):")
                if choose=="b":
                    self.login_baoleiji()
            else:
                print("存在该用户")
                key=hashlib.md5(bytes("007",encoding="utf-8"))
                key.update(bytes(password,encoding="utf-8"))
                password=key.hexdigest()
                print(password)
                sql2="select passworld from baoleiji.baoleiji_user where name='{name}'".format(name=username)
                cursor.execute(sql2)
                table_passworld=cursor.fetchall()
                table_passworld=table_passworld[-1].get("passworld")
                if password==table_passworld:
                    print("账户名密码正确，登录成功！！")
                    self.loging_username=username
                    self.login()
                else:
                    choose=input("账户名或者密码错误，登录失败!!(按回车继续输入，按b返回上一级菜单):")
                    if choose=="b":
                        self.login_baoleiji()
            connect.commit()
            connect.close()
            cursor.close()

    def login(self):
        flag=True
        msg="欢迎{user}登录!!".format(user=self.loging_username)
        print(msg)
        msg=["1.添加主机信息","2.选择当前登录用户的主机进行操作","3.查看当前用户的操作纪录","4.返回上一级菜单","5.退出堡垒机"]
        try:
            while flag:
                for i in msg:
                    print(i)
                choose=input("请输入你要操作的编号:").strip()
                if len(choose)==0:continue
                if choose=="1":
                    print("添加主机信息")
                    self.add_host_infor()
                elif choose=="2":
                    print("选择当前登录用户的主机进行操作")
                    self.check_loging_user()
                elif choose=="3":
                    print("查看当前用户的操作纪录")
                elif choose=="4":
                     self.login_baoleiji()
                elif choose=="5":
                    print("退出堡垒机")
                    exit()
                else:
                    print("你的选择不正确,请重新输入!")
        except Exception as ex:
            print(ex)

    def add_host_infor(self):
        print("添加主机模块")
        falg=True
        msg=["1.添加主机用户名,ip地址,端口","2.添加用来登录的系统用户名和密码","3.绑定主机和系统用户名进行进行授权登录(重要,一定要绑定,不然登录不了主机)","4.返回上一级菜单","5.退出堡垒机"]
        try:
            while falg:
                for i in msg:
                    print(i)
                choose=input("请选择你要操作的编号:").strip()
                if len(choose)==0:continue
                if choose=="1":
                    print("你选择了添加主机用户名,ip,端口")
                    self.add_ip_port()
                elif choose=="2":
                    print("你选择了添加用来登录的系统用户名和密码")
                    self.add_user_passworld()
                elif choose=="3":
                    print("绑定主机和系统用户名进行进行授权登录(重要,一定要绑定,不然登录不了主机)")
                    self.grant()
                elif choose=="4":
                    print("返回上一级菜单")
                    self.login()
                elif choose=="5":
                    print("退出堡垒机")
                    exit()
                else:
                    print("你的选择不正确,请重新输入!")
        except Exception as ex:
            print(ex)

    def  add_ip_port(self):
         mysql_ip=self.infor.get("mysql_ip")
         mysql_port=int(self.infor.get("mysql_port"))
         mysql_user=self.infor.get("mysql_user")
         mysql_password=self.infor.get("mysql_password")
         print("现在添加主机名和ip地址端口")
         flag=True
         while flag:
             hostname=input("请输入主机名:").strip()
             ip_addr=input("请输入ip地址:").strip()
             port=input("请输入端口(按回车默认端口22)：").strip()
             if len(hostname)==0 or len(ip_addr)==0:
                 print("你输入的用户名和ip地址不能为空")
                 continue
             else:
                 if len(port)==0:
                     port=22
                 else:
                     try:
                        port=int(port)
                     except Exception as ex:
                         print("你输入的端口号不合法重新输入")
                         continue
             try:
                 connect=pymysql.connect(host=mysql_ip,port=mysql_port,user=mysql_user,passwd=mysql_password)
                 cursor=connect.cursor(cursor=pymysql.cursors.DictCursor)
                 sql="select id from baoleiji.baoleiji_user where name='{name}'".format(name=self.loging_username)
                 cursor.execute(sql)
                 result=cursor.fetchall()
                 loging_id=result[-1].get("id")
                 add_host_ip_sql="insert into baoleiji.host_ip(hostname,ip_address,port) values('{hostname}','{ip}','{port}')".format(hostname=hostname,ip=ip_addr,port=port)
                 hangshu=cursor.execute(add_host_ip_sql)
                 last_id=cursor.lastrowid
                 add_user_to_ip_sql="insert into baoleiji.user_to_ip(baoleiji_user_id,host_ip_id) values('{bao}','{ip_id}')".format(bao=loging_id,ip_id=last_id)
                 cursor.execute(add_user_to_ip_sql)
                 connect.commit()
                 connect.close()
                 cursor.close()
                 print("添加主机名和ip地址端口成功!!!")
                 choose=input("按回车继续添加主机名和ip,按b返回上一层菜单:").strip()
                 if choose=="b":
                     self.add_host_infor()
             except Exception as ex:
                 print(ex)
                 continue

    def add_user_passworld(self):
        print("添加用户名和密码模块")
        falg=True
        while falg:
            auth_id=input("请输入系统用户认证类型:(密码(pass)或者秘钥(key)):").strip()
            if auth_id=="pass":
                print("认证类型为密码")
                user=input("请输入系统用户名:").strip()
                passworld=input("请输入系统用户名密码:").strip()
                if len(user)==0 or len(passworld)==0:
                    print("用户名或者密码不能为空,请重新输入!")
                auth_id="p"
                try:
                    self.renture_mysql_connect_obj()
                    sql="select id from baoleiji.baoleiji_user where name='{name}'".format(name=self.loging_username)
                    self.cursor.execute(sql)
                    result=self.cursor.fetchall()
                    loging_id=result[-1].get("id")
                    print(loging_id)
                    #passworld=self.md5(passworld)
                    add_host_user_sql="insert into baoleiji.host_user(username,passworld,auth_id) values('{username}','{pas}','{auth_id}')".format(username=user,pas=passworld,auth_id=auth_id)
                    self.cursor.execute(add_host_user_sql)
                    last_id=self.cursor.lastrowid
                    add_user_to_user_sql="insert into baoleiji.user_to_user(baoleiji_user_id,host_user_id) values('{bao}','{user_id}')".format(bao=loging_id,user_id=last_id)
                    self.cursor.execute(add_user_to_user_sql)
                    self.connect.commit()
                    self.cursor.close()
                    self.connect.close()
                    print("添加用户名和密码完毕!")
                    choose=input("按回车继续添加用户名和密码,按b返回上一层菜单:").strip()
                    if choose=="b":
                        self.add_host_infor()
                except Exception as ex:
                    print(ex)
                    continue
            elif auth_id=="key":
                print("认证类型为秘钥")
                user=input("请输入系统用户名:").strip()
                if len(user)==0:
                    print("用户名不能为空!")
                    continue
                auth_id="r"
                passworld="None"
                try:
                    self.renture_mysql_connect_obj()
                    passworld=self.md5(passworld)
                    add_host_user_sql="insert into baoleiji.host_user(username,passworld,auth_id) values('{username}','{pas}','{auth_id}')".format(username=user,pas=passworld,auth_id=auth_id)
                    print(add_host_user_sql)
                    self.cursor.execute(add_host_user_sql)
                    self.connect.commit()
                    self.cursor.close()
                    self.connect.close()
                    print("添加用户名完毕!")
                    choose=input("按回车继续添加用户名和密码,按b返回上一层菜单:").strip()
                    if choose=="b":
                        self.add_host_infor()
                except Exception as ex:
                    print(ex)
                    continue
            else:
                print("你输入的认证类型不正确，请重新输入!!")
                continue

    def grant(self):
        print("这里是绑定授权模块")
        flag=True
        try:
            self.renture_mysql_connect_obj()
            sql="select id from baoleiji.baoleiji_user where name='{name}'".format(name=self.loging_username)
            self.cursor.execute(sql)
            result=self.cursor.fetchall()
            loging_id=result[-1].get("id")
            sql="select * from baoleiji.host_ip where host_ip.id in (select host_ip_id from baoleiji.user_to_ip where baoleiji_user_id='{id}')".format(id=loging_id)
            sql2="select * from baoleiji.host_user where host_user.id in (select host_user_id from baoleiji.user_to_user where baoleiji_user_id='{id}')".format(id=loging_id)
            self.cursor.execute(sql)
            ip_host_list=self.cursor.fetchall()
            self.cursor.execute(sql2)
            username_list=self.cursor.fetchall()
            while flag:
                for i in ip_host_list:
                    msg="id:{id},hostname:{hostname},ip:{ip},port:{port}".format(id=i.get("id"),hostname=i.get("hostname"),ip=i.get("ip_address"),port=i.get("port"))
                    print(msg)
                choose=input("请选择要授权的主机id名:")
                if len(choose)==0:continue
                sql3="select * from baoleiji.host_ip where host_ip.id in (select host_ip_id from baoleiji.user_to_ip where baoleiji_user_id='{id}') and id='{i}'".format(id=loging_id,i=choose)
                self.cursor.execute(sql3)
                result=self.cursor.fetchall()
                if result==():
                    print("你选择的id不正确,请重新输入!!")
                    continue
                else:
                    print(result)
                    choose_id=result[-1].get("id")
                    print(choose_id)
                    f=True
                    print("你已经选择好主机id了,现在请选择需要绑定的主机系统用户名:")
                    while f:
                        for i in username_list:
                            msg="id:{id},username:{username}".format(id=i.get("id"),username=i.get("username"))
                            print(msg)
                        choose_user=input("请选择你要绑定的主机id号码:").strip()
                        if len(choose_user)==0:continue
                        sql4="select * from baoleiji.host_user where host_user.id in (select host_user_id from baoleiji.user_to_user where baoleiji_user_id='{id}') and id='{i}'".format(id=loging_id,i=choose_user)
                        self.cursor.execute(sql4)
                        result=self.cursor.fetchall()
                        if result==():
                            print("你选择的id不正确,请重新输入!!")
                            continue
                        else:
                            print("输入的id合法，现在开始绑定")
                            try:
                                host_user_id=result[-1].get("id")
                                print(choose_id,host_user_id,self.loging_username)
                                loging_username_id_sql="select id from baoleiji.baoleiji_user where name='{name}'".format(name=self.loging_username)
                                self.cursor.execute(loging_username_id_sql)
                                loging_username_id=self.cursor.fetchall()
                                loging_username_id=loging_username_id[-1].get("id")
                                print(choose_id,host_user_id,loging_username_id)
                                add_host_ip_to_host_user_sql="insert into baoleiji.host_ip_to_host_user(host_ip_id,host_user_id) values('{host_ip_id}','{id}')".format(host_ip_id=choose_id,id=host_user_id)
                                self.cursor.execute(add_host_ip_to_host_user_sql)
                                self.connect.commit()
                                self.connect.commit()
                                self.connect.close()
                                self.cursor.close()
                                print("绑定完毕!")
                                choose=input("按回车继续绑定,按b返回上一层菜单:").strip()
                                if choose=="b":
                                    self.add_host_infor()
                                else:
                                    self.grant()
                            except Exception as  ex:
                                print(ex)
                                self.grant()
        except Exception as ex:
            print(ex)
            self.add_host_infor()
        finally:
             self.connect.commit()
             self.connect.close()
             self.cursor.close()


    def  check_loging_user(self):
         print("这里是选择当前登录用户的主机进行操作模块")
         count=0
         flag=True
         try:
             sql="select id from baoleiji.baoleiji_user where name='{name}'".format(name=self.loging_username)
             self.renture_mysql_connect_obj()
             self.cursor.execute(sql)
             user_id_dic=self.cursor.fetchall()
             user_id=user_id_dic[-1].get("id")
             sql2="select * from baoleiji.host_ip where host_ip.id in (select host_ip_id from baoleiji.host_ip_to_host_user where host_ip_to_host_user.host_ip_id in (select host_ip_id from baoleiji.user_to_ip where baoleiji_user_id='{id}'))".format(id=user_id)
             self.cursor.execute(sql2)
             ip_dic=self.cursor.fetchall()
             #print(ip_dic)
             sql3="select * from baoleiji.host_user where host_user.id in (select host_user_id from baoleiji.host_ip_to_host_user where host_ip_to_host_user.host_ip_id in (select host_ip_id from baoleiji.user_to_ip where baoleiji_user_id='{id}'))".format(id=user_id)
             self.cursor.execute(sql3)
             os_user_dic=self.cursor.fetchall()
             #print(os_user_dic,len(os_user_dic))
             self.connect.commit()
             self.connect.close()
             self.cursor.close()
         except Exception as ex:
             print(ex)
             self.login()
         while flag:
             for i in ip_dic:
                msg="id:{id},hostname:{hostname},ip:{ip},port:{port}".format(id=i.get("id"),hostname=i.get("hostname"),ip=i.get("ip_address"),port=i.get("port"))
                print(msg)
             choose=input("请选择你要操作的id编号:").strip()
             if len(choose)==0:continue
             sql="select * from baoleiji.host_ip where host_ip.id in (select host_ip_id from baoleiji.host_ip_to_host_user where host_ip_to_host_user.host_ip_id in (select host_ip_id from baoleiji.user_to_ip where baoleiji_user_id='{i}')) and id='{c}'".format(i=user_id,c=choose)
             self.renture_mysql_connect_obj()
             self.cursor.execute(sql)
             result=self.cursor.fetchall()
             if result==():
                 print("你选择的id编号不在范围内,请重新输入")
                 continue
             else:
                 print("你选择的编号正确!!")
                 print(choose)
                 print(result)
                 f=True
                 while f:
                     for i in os_user_dic:
                         msg="id:{i},username:{u},passworld:{pas},auth_id:{auth}".format(i=i.get("id"),u=i.get("username"),pas=i.get("passworld"),auth=i.get("auth_id"))
                         print(msg)
                     choose2=input("你选择你要登录主机的用户:").strip()
                     sql="select * from baoleiji.host_user where host_user.id in (select host_user_id from baoleiji.host_ip_to_host_user where host_ip_to_host_user.host_ip_id in (select host_ip_id from baoleiji.user_to_ip where baoleiji_user_id='{i}')) and id='{c}'".format(i=user_id,c=choose2)
                     self.renture_mysql_connect_obj()
                     self.cursor.execute(sql)
                     result=self.cursor.fetchall()
                     if result==():
                         print("你选择的id编号用户不在范围内,请重新输入")
                         continue
                     else:
                         print("你选择的编号用户正确!!")
                         print(choose2)
                         print(result)
                         self.ip_id=int(choose)
                         self.user_id=int(choose2)
                         print("主机信息选择完毕!")
                         self.control_host()
                         self.connect.commit()
                         self.connect.close()
                         self.cursor.close()

    def control_host(self):
        print("这里是链接主机模块")
        print(self.ip_id,self.user_id)
        self.check_linux_win()
        print(self.if_os)
        self.renture_mysql_connect_obj()   #或者mysql链接对象
        sql="select id from baoleiji.baoleiji_user where name='{name}'".format(name=self.loging_username)
        self.renture_mysql_connect_obj()
        self.cursor.execute(sql)
        baoleiji_dic=self.cursor.fetchall()
        baoleiji_id=baoleiji_dic[-1].get("id")
        sql_get_ip_infor="select * from baoleiji.host_ip where host_ip.id in (select host_ip_id from baoleiji.host_ip_to_host_user where host_ip_to_host_user.host_ip_id in (select host_ip_id from baoleiji.user_to_ip where baoleiji_user_id='{i}')) and id='{c}'".format(i=baoleiji_id,c=self.ip_id)
        self.cursor.execute(sql_get_ip_infor)
        ip_dic=self.cursor.fetchall()
        sql_get_username_infor="select * from baoleiji.host_user where host_user.id in (select host_user_id from baoleiji.host_ip_to_host_user where host_ip_to_host_user.host_ip_id in (select host_ip_id from baoleiji.user_to_ip where baoleiji_user_id='{i1}')) and id='{c1}'".format(i1=baoleiji_id,c1=self.user_id)
        self.cursor.execute(sql_get_username_infor)
        user_dic=self.cursor.fetchall()
        username=user_dic[-1].get("username")
        passworld=user_dic[-1].get("passworld")
        auth_id=user_dic[-1].get("auth_id")
        ip=ip_dic[-1].get("ip_address")
        port=ip_dic[-1].get("port")
        print(username,passworld,auth_id,ip)




    def check_linux_win(self):
        try:
            import termios   #判断主机为linux还是windows
            import tty
            self.if_os="linux"
            print("this is linux")
        except Exception as ex:
            self.if_os="windows"
            print("this is windows")

    def renture_mysql_connect_obj(self):   #返回pymysql链接对象
        mysql_ip=self.infor.get("mysql_ip")
        mysql_port=int(self.infor.get("mysql_port"))
        mysql_user=self.infor.get("mysql_user")
        mysql_password=self.infor.get("mysql_password")
        connect=pymysql.connect(host=mysql_ip,port=mysql_port,user=mysql_user,passwd=mysql_password)
        cursor=connect.cursor(cursor=pymysql.cursors.DictCursor)
        self.connect=connect
        self.cursor=cursor


    def md5(self,password):
         key=hashlib.md5(bytes("007",encoding="utf-8"))
         key.update(bytes(password,encoding="utf-8"))
         password=key.hexdigest()
         return password

    def main(self):
        result=self.login_baoleiji()


obj=baoleiji()

obj.main()

