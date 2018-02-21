import pika, time, timeit, copy




import keras
from keras.models import Sequential
from optimizer_builders import make_optimizer
from layer_builders import make_layer
import json
import numpy as np

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def load_data(file_path):
    return np.asarray(load_json(file_path))

config = load_json('./../sample-NNs/instance-config.json')

# load data
x_train = load_data(config['data']['xTrainPath'])
y_train = load_data(config['data']['yTrainPath'])
x_test = load_data(config['data']['xTestPath'])
y_test = load_data(config['data']['yTestPath'])







connection = pika.BlockingConnection(pika.ConnectionParameters('https://sqs.us-east-1.amazonaws.com/801215208692/run-nn'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    build_time_start = time.time()
    print(" [x] Received %r" % body)
    # init model
    model = Sequential()

    ## add layers
    for index, layer_config in enumerate(config['layers']):

        additional_args = {}
        if index == 0: # handle input layer
            additional_args['input_dim'] = len(x_train[0])
        if index == len(config['layers']) - 1: # handle output layer
            additional_args['units'] = len(y_train[0])

        model.add(make_layer(copy.deepcopy(layer_config), additional_args))


    optimizer = make_optimizer(copy.deepcopy(config['optimizer']))
    model.compile(loss=config['loss'], optimizer=optimizer, metrics=config['metrics'])
    model.fit(x_train, y_train, epochs=config['epochs'], batch_size=config['batchSize'])
    end_build_time = time.time() - build_time_start  
    score = model.evaluate(x_test, y_test, batch_size=config['batchSize'])
    end_run_time = time.time() - end_build_time

    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback, queue='task_queue', no_ack=False)

channel.start_consuming()
