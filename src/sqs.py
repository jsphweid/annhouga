import boto3, json

with open('../sample-NNs/instance-config.json', 'r') as f:
    config = json.load(f)

# Get the service resource
sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='run-nn')

arr = []
for i in range(0, 10):
    message = { "Id": str(i), "MessageBody": json.dumps(config) }
    arr.append(message)

response = queue.send_messages(Entries=arr)


# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))