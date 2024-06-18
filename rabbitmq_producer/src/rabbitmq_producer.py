#!/usr/bin/python3

import pika
import sys
import time
import argparse
from datetime import datetime

currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

############################################
################# HELPERS ##################
############################################
def argParse():
    parser = argparse.ArgumentParser(prog='rabbitmq_producer.py', description="Script for produce test messages to RabbitMQ", epilog='Editor: jakubnoga95@gmail.com')
    parser.add_argument("--host", "-H", type=str, help="Host of the RabbitMQ")
    parser.add_argument("--port", "-P", type=int, help="Port of the RabbitMQ")
    parser.add_argument("--username", "-U", type=str, help="RabbitMQ username")
    parser.add_argument("--password", "-p", type=str, help="RabbitMQ user password")
    parser.add_argument("--queue", "-Q", type=str, help="RabbitMQ queue")
    parser.add_argument("--message", "-M", type=int, help="Number of messages")

    args = parser.parse_args()

    if args.host:
        host = args.host
        print(f"{currentTime}: Using host {host}")
    else:
        host = "127.0.0.1"
        print(f"{currentTime}: Using default host {host}")

    if args.port:
        port = args.port
        print(f"{currentTime}: Using port {port}")
    else:
        port = 5672
        print(f"{currentTime}: Using default host {port}")

    if args.username:
        username = args.username
        print(f"{currentTime}: Using user {username}")
    else:
        raise Exception(f"{currentTime}: Please provide RabbitMQ user")

    if args.password:
        password = args.password
        print(f"{currentTime}: Using password {password}")
    else:
        raise Exception(f"{currentTime}: Please provide RabbitMQ user password")

    if args.queue:
        queue = args.queue
        print(f"{currentTime}: Using queue {queue}")
    else:
        raise Exception(f"{currentTime}: Please provide RabbitMQ queue")

    if args.message:
        message = args.message
        print(f"{currentTime}: Using message {message}")
    else:
        raise Exception(f"{currentTime}: Please provide RabbitMQ queue")

    return host, port, username, password, queue, message

############################################
################## MAIN ####################
############################################
def main():

    host, port, username, password, queue, message = argParse()

    credentials = pika.PlainCredentials(username, password)

    try:
        print(f"{currentTime}: Connecting to RabbitMQ server at {host}...")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=credentials))
        print(f"{currentTime}: Connected successfully.")
    except Exception as e:
        print(f"{currentTime}: Failed to connect to RabbitMQ server: {e}")
        sys.exit(1)

    channel = connection.channel()

    try:
        print(f"{currentTime}: Declaring queue '{queue}'...")
        channel.queue_declare(queue=queue, durable=True)
        print(f"{currentTime}: Queue declared successfully.")
    except Exception as e:
        print(f"{currentTime}: Failed to declare queue: {e}")
        connection.close()
        sys.exit(1)

    for num in range(message):
        try:
            print(f"{currentTime}: Publishing message...")
            channel.basic_publish(exchange='',
                                routing_key=queue,
                                body=f"Hello World! - {num}",
                                properties=pika.BasicProperties(
                                    delivery_mode=2,  # make message persistent
                                ))
            print(f"{currentTime}: [x] Sent 'Hello World!'")
        except Exception as e:
            print(f"{currentTime}: [x] Failed to publish message: {e}")

    time.sleep(1)

    connection.close()
    print(f"{currentTime}: Connection closed.")

# Main
if __name__ == '__main__':
    main()
    