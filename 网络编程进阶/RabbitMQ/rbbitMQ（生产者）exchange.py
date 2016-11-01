import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))
channel=connection.channel()

channel.exchange_declare(exchange="logs",type="fanout")   #创建exchange字段


message="hello world"
channel.basic_publish(exchange="logs",routing_key="",body=message)  #往exchange字段里面发消息


connection.close()




