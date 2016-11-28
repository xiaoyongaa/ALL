#!/application/python3.5/bin/python3.5
import paramiko
ip="192.168.1.10"
username="root"
password="1"
# key_file="/root/.ssh/id_rsa"
# key=paramiko.RSAKey.from_private_key_file(key_file)

transport=paramiko.Transport((ip, 22))
transport.connect(username=username,password=password)

###########################
print(transport)
ssh=paramiko.SSHClient()  #创建ssh对象
ssh._transport=transport  #ssh里面transport字段的更新
###########################



stdin,stdout,stderr=ssh.exec_command("df")
result=str(stdout.read(),encoding="utf-8")
print(result)




############
# sftp=paramiko目录.SFTPClient.from_transport(transport)
# sftp.get("/root/mylog.txt","F:\\mylog.txt")
#################

#transport.close()