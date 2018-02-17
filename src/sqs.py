import boto3, json

with open('../sample-NNs/instance-config.json', 'r') as f:
    config = json.load(f)

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='run-nn')

# Create a new message
response = queue.send_message(MessageBody=json.dumps(config))

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))