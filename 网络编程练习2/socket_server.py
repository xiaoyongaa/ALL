import socket
import os
ip_port=("127.0.0.1",9999)

#买个手机
s=socket.socket()


#绑定电话卡
s.bind(ip_port)



#设置开机最多可以同时接听多少个电话
s.listen(5)
while True:
    #开机(阻塞)等待接听
    conn,addr=s.accept()
    while True:
        try:
            #接收客户端信息(第二步)
            shou=conn.recv(1024)
            if str(shou,encoding="utf-8")=="exit":break
            shou=str(shou,encoding="utf-8")
            re=os.system(shou)
            if re ==0:
                result=os.popen(shou).read()
                result=bytes(result,encoding="utf-8")
                ##############解决粘包问题############################
                msg="Ready|{n}".format(n=len(result))
                conn.send(bytes(msg,encoding="utf-8"))
                buding=conn.recv(1024)
                buding=str(buding,encoding="utf-8")
                if buding=="start":
                    ##############解决粘包问题############################
                    #发送给客户端信息(第三步)
                    conn.send(result)
            else:
                result="请输入正确的命令"
                conn.send(bytes(result,encoding="utf-8"))
        except Exception as ex:
            print(ex)
            break



    conn.close()