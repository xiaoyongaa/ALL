import socket
ip_port=("127.0.0.1",9999)
sk=socket.socket()
sk.connect(ip_port)
falg=True
while falg:
    shou=sk.recv(1024)
    print(shou.decode())
    while falg:
        inp=input(">>>:").strip()
        if len(inp)==0:continue
        if inp=="q":
            falg=False
            break
        sk.sendall(bytes(inp,encoding="utf-8"))



