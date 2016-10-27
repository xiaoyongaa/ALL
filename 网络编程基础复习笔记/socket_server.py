import socket
import json
import pickle
ip_port=("127.0.0.1",9999)
sk=socket.socket()
sk.bind(ip_port)
sk.listen(5)

#
while True:
    conn,addr=sk.accept()  #重新接收
    try:
        #收消息
        shou=conn.recv(1024)
        print(shou.decode())  #收到消息
        #break
        #发消息
        stat="ok"
        data="fa"
        msg={"stat":stat,"data":data}
        conn.sendall(pickle.dumps(msg))  #把字典dumps保存起来发送走
    except Exception as  ex:
        print(ex)
        continue


#
conn.close()