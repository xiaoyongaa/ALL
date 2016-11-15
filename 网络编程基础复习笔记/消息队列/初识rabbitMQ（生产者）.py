import pika
#r=pika.ConnectionParameters(host="10.0.0.25")  #链接范围
connection=pika.BlockingConnection(pika.ConnectionParameters(host="192.168.1.10"))
channel=connection.channel()  #获取channel函数的返回值channel对象，其实就是connection对象
channel.queue_declare(queue="hello")   #创建队列hello

channel.basic_publish(exchange="",routing_key="hello",body="hi",properties=pika.BasicProperties(delivery_mode=2))
connection.close()

