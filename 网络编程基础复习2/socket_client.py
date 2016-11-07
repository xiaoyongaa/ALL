import socket
import pickle
ip_port=("127.0.0.1",9999)
sk=socket.socket()
sk.connect(ip_port)

falg=True
while falg:
    shou=sk.recv(1024)
    shou=pickle.loads(shou)
    if shou.get("stat")=="ok":
        while falg:
            inp=input(">>:").strip()
            if len(inp)==0:continue
            if inp=="exit":
                falg=False
                break
            sk.sendall(bytes(inp,encoding="utf-8"))



sk.close()