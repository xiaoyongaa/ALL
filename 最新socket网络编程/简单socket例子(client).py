#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import socket,pickle
ip_port=("192.168.1.10",9999)
client=socket.socket() #声明socket类型对象
client.connect(ip_port)
while True:
    inp=input("请输入你要发送的文字>>>:").strip()
    if len(inp)==0:continue
    client.send(bytes(inp,encoding="utf-8"))   #发送第一次信息
    stat=str(client.recv(1024),encoding="utf-8")
    print(stat)
    if stat=="ok":
        print("命令输入正确")
        s=bytes("ok",encoding="utf-8")
        client.send(s)
        infor=client.recv(1024)
        infor=pickle.loads(infor)
        size=int(infor.get("size"))
        stat=infor.get("stat")
        c=0
        b=bytes()  #定义一个空字节
        if stat=="ready":
            print("开始循环接收")
            stat=bytes("go",encoding="utf-8")
            client.sendall(stat)
            while True:
                if c==size:
                   break
                else:
                    shou=client.recv(1024)
                    c+=len(shou)
                    b+=shou
            print(str(b,encoding="utf-8"))
            print(len(b),size)

            # while c<size:
            #     shou=client.recv(1024)
            #     c=c+len(shou)
            #     b=b+shou  #每次增加接收的1024内容
            # print(str(b,encoding="utf-8"))

    elif stat=="no":
        print("命令输入错误,,重新输入!")
        continue
client.close()


