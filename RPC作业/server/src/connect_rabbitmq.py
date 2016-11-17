import sys
import re
import os
import pika
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
def start():
    msg="欢迎使用RPC程序,现在初始化rbbitMQ链接."
    print(msg)
    with open(path+"\conf\conf")  as conf:
        data=conf.read()
    old=re.findall(r"RbbitMQ_server_ip=\".*\"",data)
    old=old[0]
    print(old)
    while True:
        now_ip=input("请输入你想链接的rabbitMQ的ip地址:").strip()
        if len(now_ip)==0:continue
        now_ip="\""+str(now_ip)+"\""
        r=re.sub(old,"RbbitMQ_server_ip="+now_ip,data)
        print(r)
        with open(path+"\conf\conf","w") as conf:
            conf.write(r)
        msg="修改成功"
        print(msg)
        infor="ok"+now_ip
        return infor
def connect_rbbitmq(ip):
    try:
        connection=pika.BlockingConnection(pika.ConnectionParameters(host=ip))
        print("服务器ip正确!!!成功链接rabbitmq!!!!你现在可以启动主程序bin/RabbitMQ_server_start.py了")
    except Exception as ex:
        msg="你输入的rabbitmq的ip不正确,请重新输入!!!"
        print(msg)
        main()
def main():
    res=start()
    print(res)
    if res.startswith("ok"):
        print("检查是否连接")
        res=res.replace("ok","")
        res=res.replace("\"","")
        res=connect_rbbitmq(res)
if __name__=="__main__":
    main()