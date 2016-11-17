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


def consume(ip):  #消费队列
    #print("消费者者模式")
    #print(ip)
    connection=pika.BlockingConnection(pika.ConnectionParameters(host=ip))
    channel=connection.channel()
    channel.queue_declare(queue="cmd")
    def callback(ch,method,properties,body):
        cmd=str(body,encoding="utf-8")
        print(cmd)
        #ch.close()
        producer(cmd,ch)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,queue="cmd",no_ack=True)
    channel.start_consuming()



def producer(cmd,ch):  #生产队列
     stat=os.system(cmd)
     if stat==0:
         result=os.popen(cmd).read()
         print(result)
         ch.queue_declare(queue="result")
         ch.basic_publish(exchange="",routing_key="result",body=result)
         ch.close()
         main()
     else:
         result="你输入的命令不正确,请重新输入!!"
         print(result)
         ch.queue_declare(queue="result")
         ch.basic_publish(exchange="",routing_key="result",body=result)
         ch.close()
         main()










def main():
    res=get_ip(path)
    if res.startswith("ok"):
        ip=res.replace("ok","")
        res=consume(ip)



if __name__=="__main__":
    main()









