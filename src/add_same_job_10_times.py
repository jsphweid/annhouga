import boto3, json

with open('../sample-NNs/instance-config.json', 'r') as f:
    config = json.load(f)

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='annhouga-nn-jobs')

arr = [{ "Id": str(i), "MessageBody": json.dumps(config) } for i in range(10)]

response = queue.send_messages(Entries=arr)