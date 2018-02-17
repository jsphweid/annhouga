import boto3, json
from nn_processors import basic_nn_processor

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='run-nn')

while 1:
    print('[*] Waiting for messages. To exit press CTRL+C')
    messages = queue.receive_messages(WaitTimeSeconds=20, MaxNumberOfMessages=1)

    for message in messages:
        print("Message received: {0}".format(message.body))
        basic_nn_processor(json.loads(message.body))
        message.delete()
