import paramiko
ip_port=("10.0.0.25",22)
transport=paramiko.Transport(ip_port)
transport.connect(username="root",password="1")

sftp=paramiko.SFTPClient.from_transport(transport)
#sftp.put("G:\电影\CHN-067_onekeybatch.mp4","/CHN-067_onekeybatch.mp4")
#sftp.get("/root/.ssh/id_rsa","F:\key\id_rsa")



