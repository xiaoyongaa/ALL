import paramiko
private_key=paramiko.RSAKey.from_private_key_file("F:\key\id_rsa")

ssh=paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='10.0.0.25', port=22, username='root',pkey=private_key)