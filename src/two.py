import pika, time 

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel2 = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
channel2.queue_declare(queue='task_queue2', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received1 %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

def callback2(ch, method, properties, body):
    print(" [x] Received2 %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel2.basic_qos(prefetch_count=1)

channel.basic_consume(callback, queue='task_queue', no_ack=False)
channel2.basic_consume(callback2, queue='task_queue2', no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
channel2.start_consuming()
