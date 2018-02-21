import boto3, json
from nn_processors import basic_nn_processor

sqs = boto3.resource('sqs')
nn_job_queue = sqs.get_queue_by_name(QueueName='annhouga-nn-jobs')
rds_job_queue = sqs.get_queue_by_name(QueueName='annhouga-rds-jobs')

while 1:
    print('[*] Waiting for messages. To exit press CTRL+C')
    messages = nn_job_queue.receive_messages(WaitTimeSeconds=20, MaxNumberOfMessages=1)

    for message in messages:
        print("Message received: {0}".format(message.body))
        result = basic_nn_processor(json.loads(message.body))
        response = rds_job_queue.send_message(MessageBody=json.dumps(result))
        if response:
            message.delete()
