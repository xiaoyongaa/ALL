import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))
channel=connection.channel()

channel.queue_declare(queue="hello")
def callback(ch,method,properties,body):
    print(body)


channel.basic_consume(callback,queue="hello",no_ack=True)
channel.start_consuming()
