import pika
from time import sleep

if __name__ == "__main__":
    params = pika.ConnectionParameters(host="localhost", port=8081)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue="ZP", durable=True)
    for i in range(500):
        channel.basic_publish(exchange="", routing_key="ZP", body='pending ' + i.__str__())
        sleep(1)

    connection.close()