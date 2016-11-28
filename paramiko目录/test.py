#!/application/python3.5/bin/python3.5
import socket
import getpass
ip=socket.gethostbyname_ex(socket.gethostname())
#print(ip)
ip=str(ip[-1]).replace("['","")
#print(ip)
ip=ip.replace("']","")
print(ip)
