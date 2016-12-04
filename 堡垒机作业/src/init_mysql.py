import os
import sys
import pymysql
import hashlib
#数据库ip地址
#数据库端口
#数据库用户名
#数据库密码
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
key=hashlib.md5(bytes("007",encoding="utf-8"))
if os.path.exists(path+"\conf\mysql_connect.txt"):
    os.remove(path+"\conf\mysql_connect.txt")


class init_mysql():
    def connect_mysql(self):
        mysql_ip=input("please input mysql connect ip:").strip()
        mysql_port=input("please input mysql connect port(按回车默认是3306端口):")
        if len(mysql_port)==0:
            mysql_port="3306"
        else:
            mysql_port=int(mysql_port)
        mysql_user=input("please input mysql connect user:").strip()
        mysql_password=input("please input mysql connect password:").strip()
        try:
            connect=pymysql.connect(host=mysql_ip,port=int(mysql_port),user=mysql_user,passwd=mysql_password)
            print("connect mysql is success!!")
            self.mysql_ip=mysql_ip
            self.mysql_port=mysql_port
            self.mysql_user=mysql_user
            self.mysql_password=mysql_password
            self.connect=connect
            return True
        except Exception as ex:
            print(ex)
            print("input error")
            main()

    def connect_mysql_conf(slef):
        print("conf model")
        #key.update(bytes(slef.mysql_password,encoding="utf-8"))
        #slef.mysql_password=key.hexdigest()
        with open(path+"\conf\mysql_connect.txt","a+") as conf:
             conf.write("mysql_ip="+slef.mysql_ip+"\n")
             conf.write("mysql_port="+slef.mysql_port+"\n")
             conf.write("mysql_user="+slef.mysql_user+"\n")
             conf.write("mysql_password="+slef.mysql_password)
        print("conf is write success!!")
        return True

    def create_databases(self):
        print("create databases")
        try:
            cursor=self.connect.cursor(cursor=pymysql.cursors.DictCursor)
            #sql="select * from baoleiji.baoleiji_user"
            sql="create database baoleiji character set utf8"
            sql_baoleiji="create table baoleiji.baoleiji_user(id int not null primary key auto_increment,name char(16) not null unique,passworld varchar(32) not null)"
            sql_host_ip="create table baoleiji.host_ip(id int not null primary key auto_increment,hostname varchar(32) not null unique,ip_address varchar(32) not null unique,port int not null)"
            sql_host_user="create table baoleiji.host_user(id int not null primary key auto_increment,username varchar(32) not null,passworld varchar(32) not null,auth_id varchar(32) not null)"
            sql_host_user_to_ip="create table baoleiji.host_ip_to_host_user(host_ip_id int not null,host_user_id int not null,constraint host_ip_id foreign key (host_ip_id) references baoleiji.host_ip(id),constraint host_user_id foreign key (host_user_id) references baoleiji.host_user(id))"
            sql_baoleiji_user_host="create table baoleiji.user_to_ip(baoleiji_user_id int not null,host_ip_id int not null,constraint baoleiji_user_id foreign key (baoleiji_user_id) references baoleiji.baoleiji_user(id),constraint host foreign key (host_ip_id) references baoleiji.host_ip(id))"
            sql_baoleiji_user_host2="create table baoleiji.user_to_user(baoleiji_user_id int not null,host_user_id int not null,constraint b foreign key (baoleiji_user_id) references baoleiji.baoleiji_user(id),constraint h foreign key (host_user_id) references baoleiji.host_user(id))"
            cursor.execute(sql)
            cursor.execute(sql_baoleiji)
            cursor.execute(sql_host_ip)
            cursor.execute(sql_host_user)
            cursor.execute(sql_host_user_to_ip)
            cursor.execute(sql_baoleiji_user_host)
            cursor.execute(sql_baoleiji_user_host2)
            #data=cursor.fetchall()
            #print(data)
            self.connect.commit()
            cursor.close()
            self.connect.close()
            return True
        except Exception as ex:
            print(ex)


    def main(self):
        result=self.connect_mysql()
        if result==True:
            result=self.connect_mysql_conf()  #把链接数据库配置写进配置文件
            if result==True:
                result=self.create_databases()
                if result==True:
                    print("create database is complete!!")
                    print("数据库所有表创建完毕,现在可以执行登录脚本进行登录了！")




if __name__ == '__main__':
    obj=init_mysql()
    obj.main()
