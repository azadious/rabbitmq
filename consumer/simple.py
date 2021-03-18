#!/usr/bin/env python
import os
import pika
import sys


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    # optional
    queue_name = 'simple'
    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(" [/] Received queue %s %r" % (queue_name, body))

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            pass
