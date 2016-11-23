import paramiko目录
ip_port=("10.0.0.25",22)
transport=paramiko目录.Transport(ip_port)   #创建个transport对象
transport.connect(username="root",password="1")   #

ssh=paramiko目录.SSHClient()
ssh._transport=transport

stdin,stdout,stderr=ssh.exec_command("ls")
print(stdout.read().decode())

#print(stdout.read())


ssh.close()
#transport.close()