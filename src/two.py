import pika, time, timeit


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(timeit.timeit('"-".join(str(n) for n in range(100))', number=100000))

    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback, queue='task_queue', no_ack=False)

channel.start_consuming()
