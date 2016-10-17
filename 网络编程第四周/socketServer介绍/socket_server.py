import socketserver
import os
ip_port=("127.0.0.1",8009)
class myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn=self.request
        msg="欢迎致电10086"
        conn.sendall(bytes(msg,encoding="utf-8"))  #第一次发送
        while True:
            try:
                data=conn.recv(1024)  #第二次接收
                if len(data)==0:break
                re=os.system(str(data,encoding="utf-8"))
                if re==0:
                    result=os.popen(data.decode()).read()
                    if len(result.strip())==0:
                        result="请输入正确命令!!!!!!!!!"
                        conn.sendall(bytes(result,encoding="utf-8"))
                    else:
                        long=len(bytes(result,encoding="utf-8"))
                        msg="Ready|{l}".format(l=long)
                        conn.sendall(bytes(msg,encoding="utf-8"))  #发送长度
                        tag=conn.recv(1024)
                        if tag.decode()=="start":
                            conn.sendall(bytes(result,encoding="utf-8")) #第3次发送
                else:
                    result="请输入正确命令"
                    conn.sendall(bytes(result,encoding="utf-8"))
            except Exception as ex:
                print(ex)
                break
if __name__=="__main__":
    server=socketserver.ThreadingTCPServer(ip_port,myserver)
    server.serve_forever()