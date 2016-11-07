import socket
import jsion
import pickle
ip_port=("127.0.0.1",9999)  #创建server端的ip和端口
sk=socket.socket()  #创建socket对象

sk.bind(ip_port)  #绑定电话卡
sk.listen(5)  #接听最大数量


while True:
    conn,addr=sk.accept()  #接听时候conn链接对象
    while True:
        try:
            stat="ok"
            data="hi"
            msg={"stat":stat,"data":data}
            conn.sendall(pickle._dumps(msg))
            shou=conn.recv(1024)
            print(shou.decode())

        except Exception as ex:
            print(ex)
            break

conn.close()

