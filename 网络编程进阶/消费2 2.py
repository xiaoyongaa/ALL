import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))  #链接rabbitMQ服务端
channel=connection.channel()    #创建频道

channel.exchange_declare(exchange="direct_logs",type="direct")  #定义队列 channel.queue_declare(queue="hello")


##创建随机队列
###########
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
#####################


severities=["error",]   #

for severity in severities:
    channel.queue_bind(exchange="direct_logs",queue=queue_name,routing_key=severity)

###############################


########################################################
print(' [*] Waiting for logs. To exit press CTRL+C')
def callback(ch,method,properties,body):
    print(body)

channel.basic_consume(callback,queue=queue_name,no_ack=True)  #消费队列  channel.basic_consume(callback,queue="hello",no_ack=True)  #消费消息

channel.start_consuming()