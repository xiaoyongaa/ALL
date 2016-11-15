import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host="192.168.1.10"))
channel=connection.channel()   #创建频道
channel.exchange_declare(exchange="logs",type="fanout")
message="hiiiiii"
channel.basic_publish(exchange="logs",routing_key="",body=message)
connection.close()

