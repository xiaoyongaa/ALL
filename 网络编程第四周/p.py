import paramiko目录
ssh=paramiko目录.SSHClient()
ssh.set_missing_host_key_policy(paramiko目录.AutoAddPolicy())
ssh.connect(hostname="10.0.0.25",port=22,username="root",password="1")
stdin, stdout, stderr = ssh.exec_command('df')
result=stdout.read()
result=str(result,encoding="utf-8").strip()
print(result)
