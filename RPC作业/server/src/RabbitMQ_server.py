import pika
import sys
import os
import re
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))

def get_ip(path):   #获取ip
    with open(path+"\conf\conf") as conf:
        data=conf.read()
    result=re.findall(r"\".*\"",data)
    ip=str(result[0])
    ip=ip.replace("\"","")
    infor="ok"+ip
    return infor


def producer(ip):  #生产队列
    #print("生产者模式")
    #print(ip)
    connection=pika.BlockingConnection(pika.ConnectionParameters(host=ip))  #创建链接
    channel=connection.channel()   #创建rabbitMQ频道
    channel.queue_declare(queue="cmd")
    while True:
        cmd=input("请输入你要执行的命令:").strip()
        if len(cmd)==0:continue
        channel.basic_publish(exchange="",routing_key="cmd",body=cmd)
        #channel.close()
        consume(ip,channel)


def consume(ip,channel):   #消费队列
    #print("消费队列")
    channel.queue_declare(queue="result")
    def callback(ch,method,properties,body):
        #print(body)
        result=str(body,encoding="utf-8")
        print(result)
        ch.close()
        main()
        #ch.close()
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,queue="result",no_ack=True)
    channel.start_consuming()













def main():
    res=get_ip(path)
    if res.startswith("ok"):
        ip=res.replace("ok","")
        #print(ip)
        res=producer(ip)


if __name__=="__main__":
    main()


