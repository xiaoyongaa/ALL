import socket
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
    print("1")
    #接收服务端发送过来的消息
    shou=s.recv(1024)
    print(str(shou,encoding="utf-8"))
    print("2")



s.close()