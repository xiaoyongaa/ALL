import socket
ip_port=("127.0.0.1",9999)
s=socket.socket() #买手机
s.bind(ip_port)  #绑定手机卡
s.listen(5)   #开机接听


while True:
    conn,addr=s.accept()   #开始接收
    #conn.sendall(bytes("hello",encoding="utf-8"))
    while True:
        try:
            shou=conn.recv(1024)  #第一次收
            print(shou.decode())
            if str(shou,encoding="utf-8")=="q":break
            conn.sendall(shou)  #第二次发

        except Exception as ex:
            print(ex)









