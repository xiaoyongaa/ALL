import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))
channel=connection.channel()

channel.exchange_declare(exchange="direct_logs",type="direct")

severity="error"
message="hiiiii"


channel.basic_publish(exchange="direct_logs",routing_key=severity,body=message)

connection.close()