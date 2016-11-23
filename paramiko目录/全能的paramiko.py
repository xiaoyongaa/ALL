import paramiko


class SSH_conecct():
    def __init__(self,ip,port,username,password):
        self.ip=ip
        self.port=int(port)
        self.username=username
        self.password=password

    def connect(self):
        transport=paramiko.Transport(self.ip, self.port)
        transport.connect(username=self.username,password=self.password)
        ssh=paramiko.SSHClient()
        ssh._transport=transport
        self.transport=transport
        self.ssh=ssh

    def cmd(self,cmd):
        stdin,stdout,stderr=self.ssh.exec_command(cmd)
        result=str(stdout.read(),encoding="utf-8")
        print(result)

    def put(self):
        sftp=paramiko.SFTPClient.from_transport(self.transport)
        sftp.get("/root/2.sh","F:\\2.sh")




obj=SSH_conecct("192.168.1.10","22","root","1")
obj.connect()

#obj.cmd("ls")
obj.put()