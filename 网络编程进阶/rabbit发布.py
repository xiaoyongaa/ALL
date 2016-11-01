import pika
import sys
connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))
channel=connection.channel()

####
channel.exchange_declare(exchange="logs",type="fanout")
###



message="xiaoyong"
channel.basic_publish(exchange="logs",routing_key="",body=message)
connection.close()

