#!/application/python3.5/bin/python3.5
#-*- coding:utf-8 -*-
# Author:xiaoyong

import paramiko
import sys
import os
import socket






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
