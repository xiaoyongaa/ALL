import socket
import json
import hashlib
import os
import sys
import time
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
os.chdir(path)
jiami=hashlib.md5()  #创建加密对象
ip_port=("127.0.0.1",9009)
s=socket.socket()
s.connect(ip_port)




def longin():
    flag=True
    while flag:
        user=input("欢迎登陆FTP,请输入用户名:").strip()
        if len(user)==0:
            print("输入的用户名不能为空,重新输入")
            continue
        s.sendall(bytes(user,encoding="utf-8"))  #发送用户信息
        user_tag=s.recv(1024)
        if user_tag.decode()=="ok":
            print("用户名验证成功")
        else:
            print(user_tag.decode())
            continue
        password=input("请输入密码：").strip()
        if len(password)==0:
            print("密码不能为空")
            continue
        user_infor={"user":user,"password":password}
        s.sendall(bytes(json.dumps(user_infor),encoding="utf-8"))  #发送了账号和密码
        longin_stat=s.recv(2048)
        str_longin_stat=str(longin_stat,encoding="utf-8")
        if str_longin_stat=="ok":
            msg="用户名密码正确,欢迎{name}用户成功登录！".format(name=user)
            print(msg)
            return "ok"
        elif str_longin_stat=="no":
            msg="密码不正确,欢迎{name}用户登录失败！".format(name=user)
            print(msg)

def cmd():
    falg=True
    while falg:
        c=input("请输入你要执行的命令:")
        if len(c)==0:continue
        if c.startswith("put") or c.startswith("get"):
            c=str(c)
            c=c.split()
            if len(c)==2:
                print("你用的命令是ftp下载或者上传功能")
                stat=c[0]
                if stat=="put":
                    print("你选择了上传功能")
                    #put方法
                    path=c[-1]   #put的路径
                    put(path)
                elif stat=="get":
                    print("你选择了下载功能")
                    path=c[-1]   #get的路径
                    get(path)
                    #get方法
            else:
                print("你输入的FTP命令不正确")
        else:
            putong_cmd(c)

def get(path):
    print("这是get")
    falg=True
    stat="get"
    while falg:
        stat_infor={"stat":stat,"cmd":"none"}
        s.sendall(bytes(json.dumps(stat_infor),encoding="utf-8"))
        shou=s.recv(1024)
        if shou.decode()=="ok":  #确认服务端收到,下载发送路径
            s.sendall(bytes(path,encoding="utf-8"))  #发送下载路径
            stat=s.recv(1024)
            str_stat=str(stat,encoding="utf-8")   #获取服务qi是否有下载文件的状态码
            if str_stat=="ok":
                print("服务器有该下载文件，可以下载")
                stat="ok"
                s.sendall(bytes(stat,encoding="utf-8"))
                ####接收服务器端包的信息
                file_infor=s.recv(1024)
                str_file_infor=str(file_infor,encoding="utf-8")
                dict_file_infor=json.loads(str_file_infor)
                file_name=dict_file_infor.get("name")
                file_size=dict_file_infor.get("size")
                file_size=int(file_size)
                print(file_name,file_size)
                stat="ok"  #确认服务器已经收到包信息了
                s.sendall(bytes(stat,encoding="utf-8"))
                if os.path.exists(file_name):
                    print("存在该文件，需要断点续传")
                    stat="send"
                    s.sendall(bytes(stat,encoding="utf-8"))  #发送断点续传的信息
                    stat=s.recv(1024)
                    if stat.decode()=="ok":
                        print("服务端已经确认，现在开始发送信息")
                        new_file_size=os.stat(file_name).st_size
                        infor={"size":new_file_size}
                        s.sendall(bytes(json.dumps(new_file_size),encoding="utf-8"))
                        ##开始接收
                        new_file_size=int(new_file_size)
                        count=new_file_size
                        with open(file_name,"ab") as client:
                            while count<file_size:
                                shou=s.recv(1024)
                                count=count+len(shou)
                                client.write(shou)
                            range_chu()
                            print("下载完成！！！！")
                            break

                else:
                    stat="first"
                    s.sendall(bytes(stat,encoding="utf-8"))
                    ##开始接收
                    count=0
                    with open(file_name,"wb") as client:
                        while count<file_size:
                            shou=s.recv(1024)
                            count=count+len(shou)
                            client.write(shou)
                        range_chu()
                        print("下载完成！！！！")
                        break
            else:
                print("服务器没有有该下载文件，无法下载,请重新输入路径")
                break

        else:
            print(shou.decode())
            break


def put(path):
    print("这是put")
    stat="put"
    stat_infor={"stat":stat,"cmd":"none"}
    s.sendall(bytes(json.dumps(stat_infor),encoding="utf-8"))
    shou=s.recv(1024)
    if shou.decode()=="ok":
        falg=True
        while falg:
            if os.path.exists(path):
                print("你要上传的路径存在")
                file_size=os.stat(path).st_size
                list_file_name=path.split("\\")
                file_name=list_file_name[-1]
                file_infor={"name":file_name,"size":file_size}
                print(file_infor)
                s.sendall(bytes(json.dumps(file_infor),encoding="utf-8"))  #发送文件信息消息
                shou=s.recv(1024)
                if shou.decode()=="ok":
                    print("确认服务器端收到文件信息,现在开始上传")
                    shou=s.recv(1024)
                    if shou.decode()=="first":
                        with open(path,"rb") as file:
                            for i in file:
                                s.sendall(i)
                            print("上传完成！！！！")
                            range_chu()
                            break
                    elif shou.decode()=="sencod":
                        print("你要上传的文件存在，需要校验完整性,要断点续传.")
                        stat="ok"
                        s.sendall(bytes(stat,encoding="utf-8"))
                        shou=s.recv(1024)
                        str_shou=str(shou,encoding="utf-8")
                        dict_shou=json.loads(str_shou)
                        print(type(dict_shou),dict_shou)
                        size=dict_shou.get("size")
                        size=int(size)
                        print(size)
                        with open(path,"rb") as new:
                            new.seek(size)
                            for i in new:
                                s.sendall(i)
                            range_chu()
                            print("断点续传完成！！！！")
                            break
            else:
                print("你要上传的路径不存在，请重新输入路径")
                break

def putong_cmd(c):  #普通命令方法
    print("你输入的命令是普通命令")
    falg=True
    while falg:
        stat="putong"
        stat_infor={"stat":stat,"cmd":c}
        s.sendall(bytes(json.dumps(stat_infor),encoding="utf-8"))  #发送命令到服务端
        ####粘包问题
        shou=s.recv(1024)
        str_shou=str(shou,encoding="utf-8")
        list_shou=str_shou.split("|")
        if str_shou.startswith("Ready"):
            stat="start"
            s.sendall(bytes(stat,encoding="utf-8"))
            long=list_shou[-1]
            long=int(long)
            print(long)
            count=0
            msg=b""
            while count<long:
                shou=s.recv(1024)
                count=count+len(shou)
                msg=msg+shou
            ####粘包问题
            print(msg.decode())
            break
        else:
            print(shou.decode())
            break

def useradd():
    falg=True
    while falg:
        #发消息
        user=input("如果你没有账号,那请输入你要注册的姓名(如果有就按q退出注册,直接登录):").strip()
        if user=="q":
            print("你已经退出注册")
            s.sendall(bytes("q",encoding="utf-8"))
            return "q"

        if len(user)==0:
            print("名字不能为空")
            continue
        s.sendall(bytes(user,encoding="utf-8"))  #发送user字符串
        user_stat=s.recv(1024)
        if user_stat.decode()=="yes":
            #print("可以创建密码和配额")
            password=input("请输入密码：").strip()
            #if password=="q":exit("你已经退出注册")
            if len(password)==0:
                print("密码不能为空")
                continue
            max=input("请输入磁盘配额：").strip()
            #if max=="q":exit("你已经退出注册")
            if len(max)==0:
                print("磁盘配额不能为空")
                continue
            if not max.isdigit():
                print("配额容量请输入数字")
                continue
            user_infor={"user":user,"password":password,"max":max}
            s.sendall(bytes(json.dumps(user_infor),encoding="utf-8"))
            msg="成功创建用户{name}!!!!".format(name=user)
            print(msg)
        else:
            print("该用户已经存在,无法创建")



def main():
    falg=True
    print("欢迎进入FTP系统")
    msg=["1.注册","2.登录"]
    while falg:
        for i in msg:
            print(i)
        choose=input("请选择你要执行的操作：").strip()
        if choose=="1":
            stat="1"
            s.sendall(bytes(stat,encoding="utf-8"))
            result=useradd()
            if result=="q":
                print("退出注册，现在开始登陆FTP")
                result=longin()
                if result=="ok":
                    cmd()

        elif choose=="2":
            print("现在开始登陆FTP")
            stat="2"
            s.sendall(bytes(stat,encoding="utf-8"))
            result=longin()
            if result=="ok":
                cmd()

        else:
            print("你输入的操作格式不正确")




#生成连续的数
def range_chu():
    for i in range(0,101):
        time.sleep(0.1)
        rate=i/100
        mun=int(rate*100)
        mum="\r{n}{m}%".format(n="="*mun,m=mun)
        sys.stdout.write(mum)
main()


s.close()