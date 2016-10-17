import socket
import re
ip_port=("10.0.0.25",8009)
#ip_port=("127.0.0.1",8009)
s=socket.socket()

s.connect(ip_port)


shou=s.recv(1024)
print(str(shou,encoding="utf-8"))   #第一次接收
while True:
    #发
    data=input("请输入：").strip()
    if len(data)==0:continue
    s.send(bytes(data,encoding="utf-8"))   #第二次发送
    if data=="exit":break
    #收
    shou=s.recv(1024)
    shou=str(shou,encoding="utf-8")
    if shou.startswith("Ready|"):
        res=re.search(r"[^Ready|].*",shou).group()
        res=int(res)
        start="start"
        s.sendall(bytes(start,encoding="utf-8"))  #发送给服务端我已经收到了长度
##############解决粘包问题############################
        count=0
        msg=b""
        while count<res:
            shou=s.recv(1024)
            count=len(shou)+count
            msg=msg+shou
            #m="max{m},{n}".format(m=res,n=len(shou))
            #print(m)
        #接收服务端的回应
        print(str(msg,encoding="utf-8"))
    else:
        print(shou)
s.close()