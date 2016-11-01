import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host="10.0.0.25"))
channel=connection.channel()

channel.exchange_declare(exchange="logs",type="fanout")#创建exchange字段logs

################################################
result=channel.queue_declare(exclusive=True)    #创建随机队列
queue_name=result.method.queue
########################################

channel.queue_bind(exchange="logs",queue=queue_name)  #把队列和exchange绑定起来，队列queue绑定exchange字段logs



######################################
def callback(ch,method,properties,body):
    print(body)

channel.basic_consume(callback,queue=queue_name,no_ack=True)


channel.start_consuming()








