from time import sleep
import pika
from random import random


import pika
from time import sleep

if __name__ == "__main__":
    params = pika.ConnectionParameters(host="localhost", port=8081)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue="ZP", durable=True)


    def callback (ch, method, properties, body):
        print(f"Otrzymano: {body.decode()}")
        sleep(30)
        chack = ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Przetworzono: {body.decode()}")
        pass

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume('ZP', callback, auto_ack=False )
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()
