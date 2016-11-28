#!/application/python3.5/bin/python3.5
import paramiko
import sys
import os
import socket
import getpass
from paramiko.py3compat import u

# windows does not have termios...
#判断主机为linux还是windows
try:
    import termios   #判断主机为linux还是windows
    import tty
    has_termios=True
    print("this is linux")
except Exception as ex:
    has_termios=False
    print("this is windows")
#判断主机为linux还是windows


def linux_windows_choose(chan):
    if has_termios==True:
        linux_shell(chan)
    else:
        windows_shell(chan)



def linux_shell(chan):
    print("linux shell")
    import select
    oldtty=termios.tcgetattr(sys.stdin)  #获取原系统tty属性
    tab_falg=False
    try:
        # 放置特殊字符应用在当前终端，如此设置，将所有的用户输入均发送到远程服务器
        tty.setraw(sys.stdin.fileno())    # 这是为原始模式，不认识所有特殊符号
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        #记录日志
        with open("/root/baoleiji.log","a+") as log:
            #记录日志
            while True:
                readable, writeable, error = select.select([chan, sys.stdin, ],[],[],1)
                if chan in readable:
                    try:
                        result=str(chan.recv(1024),encoding="utf-8")
                        if len(result)==0:break
                        if tab_falg==True:   #如果输入的tab按键的话，把结果写入日志
                            if result.startswith("\r\n"):
                                pass
                            else:
                                log.write(result)
                                log.flush()
                            tab_falg=False
                        sys.stdout.write(result)
                        sys.stdout.flush()
                    except Exception as ex:
                        print(ex,"linu_shell mode ")
                elif sys.stdin in readable:
                    inp=sys.stdin.read(1)
                    if inp=="\t":   #判断用户输入的是否是tab符号
                        tab_falg=True
                    else:
                        if ord(inp)==13:
                            log.write("\n")   #写入记录
                            log.flush()     #刷新
                        else:
                            log.write(inp)   #写入记录
                            log.flush()     #刷新
                    chan.send(inp)
    finally:
        termios.tcsetattr(sys.stdin,termios.TCSADRAIN, oldtty)   # 还原系统终端属性


def windows_shell(chan):
    print("windows shell")



def run():
    host_list=[{"host":"192.168.1.10","username":"root","port":"22","password":"1","auth_id":"p"},
           {"host":"192.168.1.11","username":"root","port":"22","password":"1","auth_id":"r"},
           {"host":"192.168.1.12","username":"root","port":"22","password":"103","auth_id":"p"},
           ]
    for key,i in enumerate(host_list,1):
        print(key,i)
    mun=int(input("num:"))
    try:
        infor=host_list[mun-1]
        print(infor)
        username=infor.get("username")
        hostname=infor.get("host")
        auth_id=infor.get("auth_id")
        print(auth_id)
        password=infor.get("password")
        port=int(infor.get("port"))
        print(username,hostname,password,port)
        tran=paramiko.Transport((hostname,port))  #验证ip+端口
        tran.start_client()  #创建客户端
        if auth_id=="p":
            tran.auth_password(username,password) #验证用户名和密码
        else:
            #秘钥登录
            print("ras login")
            default_path=os.path.join(os.environ["HOME"],".ssh","id_rsa")
            print(default_path)
            new_path=input("please input rsa path:").strip()
            if len(new_path)==0:
                print("default rsa login")
                key_path=default_path
                key=paramiko.RSAKey.from_private_key_file(key_path)
            else:
                key_path=new_path
                key=paramiko.RSAKey.from_private_key_file(key_path)
            tran.auth_publickey(username, key)
        chan=tran.open_session()  #打开一个通道
        chan.get_pty()  #获取一个终端
        chan.invoke_shell()  #激活终
        print(username)
        linux_windows_choose(chan)
        chan.close()
        tran.close()
    except Exception as ex:
        print(ex)
        run()




if __name__=="__main__":
    run()