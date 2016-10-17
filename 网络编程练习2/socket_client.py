import socket
import re
ip_port=("127.0.0.1",9999)

#买手机
s=socket.socket()


#链接服务端
s.connect(ip_port)

while True:
    #发给服务端消息(第一步)
    fa=input("请输入:").strip()
    fa=bytes(fa,encoding="utf-8")  #转换成比特流发送
    s.send(fa)
    if str(fa,encoding="utf-8")=="exit":break
    ##############解决粘包问题############################
    buding=s.recv(1024)
    buding=str(buding,encoding="utf-8")
    if buding.startswith("Ready|"):
        res=re.search(r"[^Ready|].*",buding).group()
        res=int(res)
    start="start"
    s.send(bytes(start,encoding="utf-8"))

    ##############解决粘包问题############################
    count=0
    msg=b""
    while count<res:
        shou=s.recv(1024)
        count=len(shou)+count
        msg=msg+shou
        m="max{m},{n}".format(m=res,n=len(shou))
        print(m)
    #接收服务端的回应

    print(str(msg,encoding="utf-8"))



s.close()








