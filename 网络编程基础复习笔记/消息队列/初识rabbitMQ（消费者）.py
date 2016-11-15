import pika

connection=pika.BlockingConnection(pika.ConnectionParameters(host="192.168.1.10"))
channel=connection.channel()

channel.queue_declare(queue="hello")



def callback(ch,method,properties,body):
    print(body)
    print(method)
    print(properties)
    ch.basic_ack(delivery_tag=method.delivery_tag)  #消息不丢失

channel.basic_qos(prefetch_count=1)   #按顺序去取 去消费

channel.basic_consume(callback,queue="hello",no_ack=False)

channel.start_consuming()
