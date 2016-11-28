#!/application/python3.5/bin/python3.5
import paramiko
import sys
import os
import select
import tty
import termios
from paramiko.py3compat import u
ip="192.168.1.11"
port=22
username="x"
password="1"
tran=paramiko.Transport((ip,port))
tran.start_client()
tran.auth_password(username,password)
chan=tran.open_session()  #打开一个通道
chan.get_pty()  #获取一个终端
chan.invoke_shell()  #激活
oldtty=termios.tcgetattr(sys.stdin)  #获取原系统tty属性
try:
    # 放置特殊字符应用在当前终端，如此设置，将所有的用户输入均发送到远程服务器
    tty.setraw(sys.stdin.fileno())    # 这是为原始模式，不认识所有特殊符号
    chan.settimeout(0.0)
    while True:
        readable, writeable, error = select.select([chan, sys.stdin, ],[],[],1)
        if chan in readable:
            try:
                result=str(chan.recv(1024),encoding="utf-8")
                if len(result)==0:break
                sys.stdout.write(result)
                sys.stdout.flush()
            except Exception as ex:
                print(ex)
        elif sys.stdin in readable:
            inp=sys.stdin.read(1)
            if len(inp)==0:break
            chan.send(inp)
finally:
    termios.tcsetattr(sys.stdin,termios.TCSADRAIN, oldtty)   # 还原系统终端属性




chan.close()
tran.close()