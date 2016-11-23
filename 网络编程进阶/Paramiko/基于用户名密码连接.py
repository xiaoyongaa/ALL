import paramiko目录
ssh=paramiko目录.SSHClient()

ssh.set_missing_host_key_policy(paramiko目录.AutoAddPolicy())

ssh.connect(hostname="10.0.0.25",port=22,username="root",password="1")



stdin,stdout,sederr=ssh.exec_command("ls")
#esult=stdout.read()


#esult=str(result,encoding="utf-8")
#rint(result)
#rint(stdin)

ssh.close()