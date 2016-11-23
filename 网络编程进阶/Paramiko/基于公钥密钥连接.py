import paramiko目录
private_key=paramiko目录.RSAKey.from_private_key_file("F:\key\id_rsa")

ssh=paramiko目录.SSHClient()

ssh.set_missing_host_key_policy(paramiko目录.AutoAddPolicy())

ssh.connect(hostname='10.0.0.25', port=22, username='root',pkey=private_key)