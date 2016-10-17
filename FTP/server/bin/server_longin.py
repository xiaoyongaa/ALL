import socketserver
import json
import hashlib
import os
import sys
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
os.chdir(path)
ip_port=("127.0.0.1",9009)
quan_user=["1"]
class ftp_server(socketserver.BaseRequestHandler):
    def handle(self):
        falg=True
        conn=self.request
        while falg:
            try:
                stat=conn.recv(1024)
                if str(stat,encoding="utf-8")=="1":
                    reslut=self.zhuche()
                    if reslut=="q":
                        reslut=self.login()  #登陆验证接口
                        if reslut=="ok":
                            self.cmd()
                elif str(stat,encoding="utf-8")=="2":
                     reslut=self.login()  #登陆验证接口
                     if reslut=="ok":
                        self.cmd()
            except Exception as ex:
                print(ex)
                break

    def cmd(self):    #执行命令方法
        falg=True
        conn=self.request
        while falg:
            try:
                cmd=conn.recv(1024)  #服务端接收到命令
                str_cmd=str(cmd,encoding="utf-8")
                dict_str_cmd=json.loads(str_cmd)
                stat=dict_str_cmd.get("stat")
                if stat=="putong":
                    self.putong_cmd(dict_str_cmd)
                elif stat=="put":
                    self.put()
                elif stat=="get":
                    self.get()



            except Exception as ex:
                print(ex)
                break

    def get(self):
        falg=True
        conn=self.request
        print("这是下载方法")
        while falg:
            try:
                stat="ok"
                conn.sendall(bytes(stat,encoding="utf-8"))  #发送确认收到的消息
                path=conn.recv(1024)
                str_path=str(path,encoding="utf-8")
                if os.path.exists(str_path):
                    print("这个路径存在，可以下载")
                    stat="ok"
                    conn.sendall(bytes(stat,encoding="utf-8"))
                    stat=conn.recv(1024)
                    str_stat=str(stat,encoding="utf-8")
                    if str_stat=="ok":
                        print("服务器有该下载文件，现在开始下载")
                        list_path=str_path.split("\\")
                        file_name=list_path[-1]
                        file_size=os.stat(str_path).st_size
                        file_infor={"name":file_name,"size":file_size}
                        conn.sendall(bytes(json.dumps(file_infor),encoding="utf-8"))
                        stat=conn.recv(1024)
                        stat=str(stat,encoding="utf-8")
                        if stat=="ok":
                            stat=conn.recv(1024)
                            stat=str(stat,encoding="utf-8")
                            if stat=="first":
                                print("现在开始给客户端下载")
                                with open(str_path,"rb") as server:
                                    for i in server:
                                        conn.sendall(i)
                                print("发送完毕！！")
                                break
                            else:
                                print("现在开始断点续传")
                                stat="ok"
                                conn.sendall(bytes(stat,encoding="utf-8"))
                                #接收新容量
                                new_size=conn.recv(1024)
                                str_new_size=str(new_size,encoding="utf-8")
                                str_new_size=int(str_new_size)
                                with open(str_path,"rb") as server:
                                    server.seek(str_new_size)
                                    for i in server:
                                        conn.sendall(i)
                                print("发送完毕！！")
                                break


                    else:
                        print("服务器没有有该下载文件，无法下载,请重新输入路径")
                        break


                else:
                    print("这个路径不存在，无法下载")
                    stat="no"
                    conn.sendall(bytes(stat,encoding="utf-8"))
                    break

            except Exception as ex:
                print(ex)
                break



    def put(self):
        conn=self.request
        print("现在是上传模块")
        stat="ok"
        conn.sendall(bytes(stat,encoding="utf-8"))
        falg=True
        while falg:
            try:
                pass
                shou=conn.recv(1024)  #收到文件内容消息
                str_shou=str(shou,encoding="utf-8")
                dict_shou=json.loads(str_shou)
                print(dict_shou,type(dict_shou))
                name=dict_shou.get("name")
                size=dict_shou.get("size")
                print(name,size)
                stat="ok"
                conn.sendall(bytes(stat,encoding="utf-8"))  #发送确认收到文件内容消息
                if os.path.exists(name):
                    print("你要上传的文件存在，需要校验完整性，判断是否要断点续传")
                    stat="sencod"
                    conn.sendall(bytes(stat,encoding="utf-8"))  #
                    now_szie=os.stat(name).st_size
                    now_name=name
                    now_infor={"name":now_name,"size":now_szie}
                    shou=conn.recv(1024)
                    if shou.decode()=="ok":
                        print("客户端准备好了。可以开始发送新文件信息了")
                        conn.sendall(bytes(json.dumps(now_infor),encoding="utf-8"))   #发送断点续传的文件信息
                        now_szie=int(now_szie)
                        count=now_szie
                        with open(name,"ab") as new:
                            while count<size:
                                shou=conn.recv(1024)
                                count=count+len(shou)
                                print(len(shou))
                                new.write(shou)
                            print("recv sucess!")
                            print("上传完成！！！！")
                            break

                else:
                    stat="first"
                    conn.sendall(bytes(stat,encoding="utf-8"))  #
                    count=0
                    with open(name,"wb") as new:
                        while count<size:
                            shou=conn.recv(1024)
                            count=count+len(shou)
                            print(len(shou))
                            new.write(shou)
                        print("recv sucess!")
                        print("上传完成！！！！")
                        break
            except Exception as ex:
                print(ex)
                break

    def putong_cmd(self,dict_str_cmd):   #普通命令方法
        print("只执行普通命令")
        cmd=dict_str_cmd.get("cmd")
        cmd=str(cmd)
        falg=True
        conn=self.request
        while falg:
            try:
                res=os.system(cmd)
                if res==0:
                    if cmd.startswith("cd"):
                        cmd=cmd+"&"+"dir"
                        print("输入的命令是切换目录命令")
                        print(cmd)
                        result=os.popen(cmd).read()
                        print(result)
                        conn.sendall(bytes(result,encoding="utf-8"))
                        break
                    else:
                        print("输入的命令正确")
                        result=os.popen(cmd).read()
                        ####粘包问题
                        long=len(bytes(result,encoding="utf-8"))
                        ready_tag="Ready|{long}".format(long=long)
                        print(ready_tag)
                        conn.sendall(bytes(ready_tag,encoding="utf-8"))
                        shou=conn.recv(1024)
                        if shou.decode()=="start":
                            ####粘包问题
                            print(result)
                            conn.sendall(bytes(result,encoding="utf-8"))
                            break
                else:
                    print("输入的命令格式不正确")
                    result="输入的命令格式不正确"
                    conn.sendall(bytes(result,encoding="utf-8"))
                    break
            except Exception as ex:
                print(ex)
                break

    def login(self):  #登陆验证方法
        jiami=hashlib.md5(bytes("d312",encoding="utf-8"))  #创建加密对象
        flag=True
        while flag:
            try:
                conn=self.request
                user=conn.recv(2048)#接收用户名密码信息
                str_user=str(user,encoding="utf-8")
                if os.path.exists("db/"+str_user):
                    print("该用户存在，可以登陆")
                    user_tag="ok"
                    conn.sendall(bytes(user_tag,encoding="utf-8"))  #发送用户名ok的字符串
                    user_infor=conn.recv(2048)
                    dict_user_infor=json.loads(user_infor.decode())
                    user=dict_user_infor.get("user")
                    password=dict_user_infor.get("password")
                    jiami.update(bytes(password,encoding="utf-8"))  #保存的对象加密密码
                    password=jiami.hexdigest()  #成功加密密码
                    os.chdir("db/"+user)
                    old=json.load(open("dict_user_infor","r+"))
                    old_user=old.get("user")
                    old_password=old.get("password")
                    os.chdir(path)
                    print(user,password,old_user,old_password)
                    if user==old_user and password==old_password:
                        msg="欢迎{name}，通过验证,成功登陆".format(name=user)
                        print(msg)
                        longin_stat="ok"
                        conn.sendall(bytes(longin_stat,encoding="utf-8"))
                        quan_user[0]=user
                        return "ok"
                    else:
                        longin_stat="no"
                        conn.sendall(bytes(longin_stat,encoding="utf-8"))
                else:
                    print("该用户不存在，请输入正确的用户名")
                    msg="该用户不存在，请输入正确的用户名"
                    conn.sendall(bytes(msg,encoding="utf-8"))
            except Exception as ex:
                print(ex)
                break

    def zhuche(self):
        jiami=hashlib.md5(bytes("d312",encoding="utf-8"))  #创建加密对象
        conn=self.request  #创建连线
        falg=True
        while falg:
            try:
                user=conn.recv(1024)  #受到user
                str_user=str(user,encoding="utf-8")
                if str_user=="q":
                    return "q"
                if os.path.exists("db/"+str_user):
                    print("该用户已经存在")
                    user_tag="no"
                    conn.sendall(bytes(user_tag,encoding="utf-8"))
                else:
                    print("该用户不存在，可以创建")
                    user_tag="yes"
                    conn.sendall(bytes(user_tag,encoding="utf-8"))
                    user_infor=conn.recv(2048)
                    dict_user_infor=json.loads(user_infor.decode())
                    user=dict_user_infor.get("user")
                    max=dict_user_infor.get("max")
                    password=dict_user_infor.get("password")
                    print(type(password),password)
                    jiami.update(bytes(password,encoding="utf-8"))  #保存的对象加密密码
                    password=jiami.hexdigest()  #成功加密密码
                    print(type(password),password)
                    dict_user_infor={"user":user,"password":password,"max":max}
                    self.add_infor(dict_user_infor)
            except Exception as ex:
                print(ex)
                break
    def add_infor(self,dict_user_infor):
            user=dict_user_infor.get("user") #拿到了用户名
            os.chdir("db/")
            os.mkdir(user)
            os.chdir(user)
            json.dump(dict_user_infor,open("dict_user_infor","w"))
            os.chdir(path)
            os.chdir("home/")
            os.mkdir(user)
            os.chdir(path)


if __name__=="__main__":
    server=socketserver.ThreadingTCPServer(ip_port,ftp_server)
    server.serve_forever()
