from time import sleep
import pika


import pika
from time import sleep

if __name__ == "__main__":
    params = pika.ConnectionParameters(host="localhost", port=8081)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue="work", durable=True)


    def callback (ch, method, properties, body):
        print(body)
        pass
    channel.basic_consume('work' )
    channel.start_consuming()

    connection.close()