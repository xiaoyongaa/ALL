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

    def put(self,old,remote):
        sftp=paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(old,remote)
    def get(self,remote,locat):
        sftp=paramiko.SFTPClient.from_transport(self.transport)
        sftp.get(remote,locat)



obj=SSH_conecct("192.168.1.10","22","root","1")
obj.connect()

#res=obj.cmd("ifconfig")

#obj.put("G:\phpcms_v9.6.0_UTF8.zip","/root/phpcms_v9.6.0_UTF8.zip")

obj.get("/root/install.log.syslog","G:\log\install.log.syslog")