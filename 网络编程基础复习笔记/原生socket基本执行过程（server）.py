import socket
ip_port=("127.0.0.1",9999)
sk=socket.socket()
sk.bind(ip_port)
sk.listen(5)


falg=True
while falg:
    conn,addr=sk.accept()
    while falg:
        try:
            conn.sendall(bytes("hi",encoding="utf-8"))
            shou=conn.recv(1024)
            print(shou.decode())
        except Exception as ex:
            print(ex)
            break

'''
sk:有新连接来了
conn:要收发消息了
'''