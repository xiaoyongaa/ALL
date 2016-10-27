import socket
ip_port=("127.0.0.1",9999)
sk=socket.socket() #买手机

sk.bind(ip_port)  #绑定ip和端口  绑定电话卡

sk.listen(5)  #最多挂起多少个链接  设置最多接多少个电话

conn,addr=sk.accept()  #等待电话接收请求


