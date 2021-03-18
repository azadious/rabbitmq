import pika
from datetime import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

queue_name = 'simple'
channel.queue_declare(queue='simple')

timestamp = datetime.now()

for i in range(10):
    body = 'loop count %s %s' % (i, timestamp)
    channel.basic_publish(exchange='', routing_key=queue_name, body=body)
    print(" [/] Sent " + body)
connection.close()
