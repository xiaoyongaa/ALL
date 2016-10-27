import socket
import pickle
ip_port=("127.0.0.1",9999)
sk=socket.socket()
sk.connect(ip_port)

while True:
    #发
    data=input(">>:").strip()
    if len(data)==0:continue
    sk.sendall(bytes(data,encoding="utf-8"))  #发消息
    #接收消息
    shou=sk.recv(1024)
    shou=pickle.loads(shou)
    stat=shou.get("stat")
    if stat=="ok":
        print("收到消息")
        data=shou.get("data")
        print(data)
    else:
        print("没有收到消息。。")

sk.close()