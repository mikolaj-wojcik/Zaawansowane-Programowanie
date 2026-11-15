import pika
from time import sleep

if __name__ == "__main__":
    params = pika.ConnectionParameters(host="localhost", port=8081)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue="work", durable=True)
    for i in range(200):
        channel.basic_publish(exchange="", routing_key="work", body=b"pending")
        sleep(10)

    connection.close()