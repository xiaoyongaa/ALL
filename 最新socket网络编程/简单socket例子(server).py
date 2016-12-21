#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import socket,os,pickle
ip_port=("127.0.0.1",9999)
server=socket.socket()
server.bind(ip_port)
server.listen()   #监听端口

def connect():
    while True:
        conn,addr=server.accept()
        while True:
            try:
                print("等待")
                 #等待电话打进来
                print("电话来了")
                data=conn.recv(1024)   #服务器接收
                print("接收到了")
                cmd=str(data,encoding="utf-8")
                stat=os.system(cmd)
                print(stat)
                print(cmd)
                if stat==0:
                    print("命令正确")
                    s="ok"
                    conn.send(bytes(s,encoding="utf-8"))
                    stat=str(conn.recv(1024),encoding="utf-8")
                    if stat=="ok":
                        result=bytes(os.popen(cmd).read(),encoding="utf-8")  #命令的结果数据包
                        infor={"stat":"ready","size":len(result)}
                        infor=pickle.dumps(infor)
                        conn.sendall(infor)  #发送开始传输和包的一共字节大小
                        stat=str(conn.recv(1024),encoding="utf-8")
                        if stat=="go":
                            conn.sendall(result)
                else:
                    print("命令不正确,请重新输入")
                    s="no"
                    conn.send(bytes(s,encoding="utf-8"))
                    continue
            except Exception as ex:
                print(addr,ex)
                break
    server.close()




connect()


