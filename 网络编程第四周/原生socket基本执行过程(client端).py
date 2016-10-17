import socket
ip_port=("127.0.0.1",9999)
s=socket.socket()  #创建socket对象


s.connect(ip_port)  #链接服务端ip

# shou=s.recv(1024)
# print(shou.decode())

while True:
    inp=input(">>>").strip()
    if len(inp)==0:continue
    s.sendall(bytes(inp,encoding="utf-8"))  #第一次发
    if inp=="q":break
    shou=s.recv(1024)   #第二次收
    print(shou.decode())
