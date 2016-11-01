#durable   消息不丢失
import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))  #创建链接
channel=connection.channel()  #创建rabbitMQ频道
channel.queue_declare(queue="hello")  #创建hello名字的队列
channel.basic_publish(exchange="",routing_key="hello",body="hello dkjsadj", properties=pika.BasicProperties(delivery_mode=2,))  #做持久化
connection.close()

