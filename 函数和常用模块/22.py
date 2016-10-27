import socket
hostname=socket.gethostname()  #获取本机的主机名
ip=socket.gethostbyname(hostname)  #获取本机ip地址
print(hostname,ip)