import socket
ip_port=("127.0.0.1",9999)  #元组的形式
#s就是手机
#买手机
s=socket.socket()


#买手机卡
s.bind(ip_port)   #bind里面跟一个参数是元组的形式


#开机
s.listen(5)

#等待电话
while True:
    conn,addr=s.accept()  #conn是一个客户端和服务端的链路
    while True:
        try:
            #收消息
            recv_data=conn.recv(1024)
            #if len(recv_data)==0:break
            if str(recv_data,encoding="utf-8")=="exit":break
            print("----------------------------1")
            #发消息
            msg=recv_data.upper()
            print("----------------------------2")
            conn.send(msg)
            print("----------------------------3")
        except Exception as ex:
            print(ex)
            break
    #挂电话
    conn.close()
