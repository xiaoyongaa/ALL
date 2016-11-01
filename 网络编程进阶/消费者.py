# ########################## 消费者 ##########################
import pika
# connection = pika.BlockingConnection(pika.ConnectionParameters(
#         host="10.0.0.25"))
# channel = connection.channel()
#
# channel.queue_declare(queue='hello')
#
# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)
#
# channel.basic_consume(callback,
#                       queue='hello',
#                       no_ack=True)
#
# print(' [*] Waiting for messages. To exit press CTRL+C')
# channel.start_consuming()

connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))
channel=connection.channel()
channel.queue_declare(queue="hello")



def callback(ch,method,properties,body):
    print(body)


channel.basic_consume(callback,queue="hello",no_ack=True)  #消费消息




print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
