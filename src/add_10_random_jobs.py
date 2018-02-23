import boto3, json
from random_nn_generator import get_random_canned_config

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='annhouga-nn-jobs')

arr = [{ "Id": str(i), "MessageBody": json.dumps(get_random_canned_config()) } for i in range(10)]

response = queue.send_messages(Entries=arr)