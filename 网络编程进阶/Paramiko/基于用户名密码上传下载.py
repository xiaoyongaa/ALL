import paramiko目录
ip_port=("10.0.0.25",22)
transport=paramiko目录.Transport(ip_port)
transport.connect(username="root",password="1")

sftp=paramiko目录.SFTPClient.from_transport(transport)
#sftp.put("G:\电影\CHN-067_onekeybatch.mp4","/CHN-067_onekeybatch.mp4")
#sftp.get("/root/.ssh/id_rsa","F:\key\id_rsa")



