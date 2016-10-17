import socket
import os
ip_port=("127.0.0.1",9999)

#买手机
s=socket.socket()


#绑定电话卡
s.bind(ip_port)


#设置接听数量
s.listen(5)

while True:  #用来重复接受新的链接
    #开机接听
    conn,addr=s.accept()
    while True:  #用来基于1个链接重复收发消息
        try:
            #接收客户端的信息
            shou=conn.recv(1024)  #收消息，阻塞
            if str(shou,encoding="utf-8")=="exit":break #客户端如果退出，服务端收到exit，退出
            #############################################
            #发送信息
            shou=str(shou,encoding="utf-8")   #把接收的二进制转换成字符串
            re=os.system(shou)
            if re==0:
                result=os.popen(shou).read()
                result=bytes(result,encoding="utf-8") #转换成二进制
###################################解决粘包  #####################################################################################
                msg="Ready|{l}".format(l=len(result))
                conn.send(bytes(msg,encoding="utf-8"))
                back=conn.recv(1024)  #收到start
                if str(back,encoding="utf-8")=="start":
#####################################解决粘包####################################################################################################
                    conn.send(result)  #发送命令的结果
            ########################################################
            else:
                result="你输入的命令不正确"
                result=bytes(result,encoding="utf-8")
                conn.send(result)
        except Exception as ex:
            print("2")
            print(ex)
            break

    #关闭连接
    conn.close()