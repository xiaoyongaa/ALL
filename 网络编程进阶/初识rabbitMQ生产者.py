import pika

# # ######################### 生产者 #########################
#
# connection = pika.BlockingConnection(pika.ConnectionParameters(
#         host="10.0.0.25"))
# channel = connection.channel()
#
# channel.queue_declare(queue='hello')
#
# channel.basic_publish(exchange='',
#                       routing_key='hello',
#                       body='Hello World!')
# print(" [x] Sent 'Hello World!'")
# connection.close()

connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))   #创建链接
channel=connection.channel() #创建频道
channel.queue_declare(queue="hello")  #创建hello队列。没有就创建。有就忽略

channel.basic_publish(exchange="",routing_key="hello",body="hello world")   #生产消息





connection.close()



