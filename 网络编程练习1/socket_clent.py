import socket
import re
ip_port=("127.0.0.1",9999)

#买手机
s=socket.socket()


#链接服务端
s.connect(ip_port)

while True:
    #直接发消息
    msg=input("请输入你要发送的：").strip()
    s.send(bytes(msg,encoding="utf-8"))
    if msg=="exit":break
    #接收服务端发送过来的消息
    ###解决粘包
    shouchang=s.recv(1024)   #接收长度
    shouchang=str(shouchang,encoding="utf-8")
    if shouchang.startswith("Ready"):
        res=re.search("[^Ready|].*",shouchang).group()
        res=int(res)
        print(res)
    start="start"
    start=bytes(start,encoding="utf-8")
    s.send(start) #发送start信息
    ###解决粘包
    #####
    ##客户端基于已经收到待接收数据长度，循环接收
    #####
    size=0
    msg=b""
    while size<res:
        shou=s.recv(1024)
        msg=msg+shou
        size=size+len(shou)
        infor="msg size {n} shou size {f}".format(n=res,f=size)
        print(infor)

    ###############

    print(str(msg,encoding="utf-8"))


s.close()