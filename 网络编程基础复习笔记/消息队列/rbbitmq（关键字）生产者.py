import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host="192.168.1.10"))
channel=connection.channel()

channel.exchange_declare(exchange="direct_logs",type="direct")

serverity="error"
message="daskjdkja"
channel.basic_publish(exchange="direct_logs",routing_key=serverity,body=message)

connection.close()

