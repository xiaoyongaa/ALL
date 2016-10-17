import socket
ip_port=("10.139.100.23",9309)

s=socket.socket()


s.connect(ip_port)

cmd="ss"
s.send(bytes(cmd,encoding="utf-8"))



shou=s.recv(2056)
print(str(shou,encoding="utf-8"))