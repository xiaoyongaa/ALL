import socket
ip_port=("127.0.0.1",9999)
s=socket.socket()  #创建socket对象


s.connect(ip_port)  #链接服务端ip

shou=s.recv(1024)
print(shou.decode())
while True:
    inp=input("root#")
    s.sendall(bytes(inp,encoding="utf-8"))
    shou=s.recv(1024)
    print(shou.decode())
s.close()