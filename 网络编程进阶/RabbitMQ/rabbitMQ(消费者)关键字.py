import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))
channel=connection.channel()
channel.exchange_declare(exchange="direct_logs",type="direct")

result=channel.queue_declare(exclusive=True)
queue_name=result.method.queue

severties=["infor","error"]


for i in severties:
    channel.queue_bind(exchange="direct_logs",queue=queue_name,routing_key=i)


def callback(ch,method,properties,body):
    print(body)

channel.basic_consume(callback,queue=queue_name,no_ack=True)

channel.start_consuming()