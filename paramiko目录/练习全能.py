import paramiko
class ssh_connect():
    def __init__(self,ip,port,username,password):
        self.ip=ip
        self.port=int(port)
        self.username=username
        self.password=password

    def connect(self):
        transport=paramiko.Transport(self.ip,self.port)
        transport.connect(username=self.username,password=self.password)
        ssh=paramiko.SSHClient()
        ssh._transport=transport
        self.ssh=ssh
        self.transport=transport

    def cmd(self,cmd):
        try:
            stdin,stdout,stderr=self.ssh.exec_command(cmd)
            result=str(stdout.read(),encoding="utf-8")
            error=str(stderr.read(),encoding="utf-8")
            if error=="":
                return result
            else:
                return error
        except Exception as  ex:
            print(ex)
            return

    def get(self,local,remote):
        try:
            sftp=paramiko.SFTPClient.from_transport(self.transport)
            sftp.get(local,remote)
        except Exception as  ex:
            print(ex)
            return

    def put(self,local,remote):
        try:
            sftp=paramiko.SFTPClient.from_transport(self.transport)
            sftp.put(local,remote)
        except Exception as  ex:
            print(ex)
            return
    def close(self):
        self.transport.close()



obj=ssh_connect("192.168.1.10","22","root","1")
obj.connect()
ret=obj.cmd("ls -alhi")
print(ret)

obj.get("/root/py/install_python.py","F:\get\install_python.py")
obj.put("F:\无锡七酷网络科技有限公司-录用通知书-WBB-沈晓勇 -201501925.pdf","/root/无锡七酷网络科技有限公司-录用通知书-WBB-沈晓勇 -20150925.pdf")

ret=obj.cmd("ldsadsads")
print(ret)

obj.close()