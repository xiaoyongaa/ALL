import socket
import select
ip_port=("127.0.0.1",9999)
sk=socket.socket()
sk.connect(ip_port)
shou=sk.recv(1024)
print(shou.decode())
while True:
    inp=input(">>>")
    sk.sendall(bytes(inp,encoding="utf-8"))
    shou=sk.recv(1024)
    print(shou.decode())
sk.close()