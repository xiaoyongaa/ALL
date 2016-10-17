import socket
ip_port=("127.0.0.1",9999)
#买手机
s=socket.socket()


#直接打电话
s.connect(ip_port)

while True:
    #发消息
    send_data=input("please ").strip()
    if len(send_data)==0:
        continue
    send_data=bytes(send_data,encoding="utf8")
    #客户端发消息  s相当于服务端的conn
    s.send(send_data)
    print("----------------------------1")
    if str(send_data,encoding="utf-8")=="exit" or str(send_data,encoding="utf-8")=="EXIT":break


    #收消息
    recv_data=s.recv(1024)
    print("----------------------------2")
    recv_data=str(recv_data,encoding="utf-8")
    # if recv_data=="exit" or recv_data=="EXIT":
    #     break
    print(recv_data)
#挂电话
s.close()