import time, timeit, copy, keras, json, numpy as np

from keras.models import Sequential
from optimizer_builders import make_optimizer
from layer_builders import make_layer

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def load_data(file_path):
    return np.asarray(load_json(file_path))

x_train = None
y_train = None
x_test = None
y_test = None

def basic_nn_processor(config):
   
    global x_train
    global y_train
    global x_test
    global y_test
    
    if x_train is None:
        print('loading data...')
        x_train = load_data(config['data']['xTrainPath'])
        y_train = load_data(config['data']['yTrainPath'])
        x_test = load_data(config['data']['xTestPath'])
        y_test = load_data(config['data']['yTestPath'])

    model = Sequential()

    for index, layer_config in enumerate(config['layers']):

        additional_args = {}
        if index == 0: # handle input layer
            additional_args['input_dim'] = len(x_train[0])
        if index == len(config['layers']) - 1: # handle output layer
            additional_args['units'] = len(y_train[0])

        model.add(make_layer(copy.deepcopy(layer_config), additional_args))

    optimizer = make_optimizer(copy.deepcopy(config['optimizer']))
    model.compile(loss=config['loss'], optimizer=optimizer, metrics=config['metrics'])
    run_time_start = time.time()
    model.fit(x_train, y_train, epochs=config['epochs'], batch_size=config['batch_size'])
    run_time_end = time.time()
    loss, accuracy = model.evaluate(x_test, y_test, batch_size=config['batch_size'])
    return {
        "loss": loss,
        "accuracy": accuracy,
        "run_time": run_time_end - run_time_start,
        "config": config
    }