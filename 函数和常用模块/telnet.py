import telnetlib
# 配置选项
Host="10.139.100.23" # Telnet服务器IP
com="ss"
t=telnetlib.Telnet(Host,port=9609)



t.write(com+b"\n")
print(t.read_all())
