import pika
import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))
channel=connection.channel()

channel.queue_declare(queue="hello")
def callback(ch,method,properties,body):
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1) #按顺序消费数据
channel.basic_consume(callback,queue="hello",no_ack=False)  #改动no_ack=False
channel.start_consuming()