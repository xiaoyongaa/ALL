import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))
channel=connection.channel()    #创建频道

channel.exchange_declare(exchange="direct_logs",type="direct")  #定义channel.queue_declare(queue="hello")

severity="error"
message="123"



channel.basic_publish(exchange="direct_logs",routing_key=severity,body=message)


connection.close()


