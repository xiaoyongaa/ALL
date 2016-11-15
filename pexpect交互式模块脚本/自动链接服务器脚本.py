import paramiko  #导入paramiko 模块，需要下载
ip_port=("192.168.1.10",22)   #定义ip和端口放在元组内
transport=paramiko.Transport(ip_port)  #ip和端口放在类里面，创建transport对象。
transport.connect(username="root",password="1")  #对象中的connect方法，链接服务器的ip和密码
sftp=paramiko.SFTPClient.from_transport(transport)  #创建sftp对象
sftp.put("E:\pexpect-4.2.1.tar.gz","/root/tools/pexpect-4.2.1.tar.gz")  #上传到服务器文件，源文件，目标文件