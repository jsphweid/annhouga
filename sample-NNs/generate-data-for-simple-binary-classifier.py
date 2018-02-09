import numpy as np
import keras
import json
import os

base_dir = '/var/tmp/annhouga/data'

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

x_train = np.random.random((1000, 1))
with open('/var/tmp/annhouga/data/xTrain.json', 'w') as outfile:
    json.dump(x_train.tolist(), outfile)

x_train_reformed = [(1 if item[0] > 0.5 else 0) for item in x_train]
y_train = keras.utils.to_categorical(x_train_reformed, num_classes=2) # hot encodes
with open('/var/tmp/annhouga/data/yTrain.json', 'w') as outfile:
    json.dump(y_train.tolist(), outfile)

x_test = np.random.random((100, 1))
with open('/var/tmp/annhouga/data/xTest.json', 'w') as outfile:
    json.dump(x_test.tolist(), outfile)

x_test_reformed = [(1 if item[0] > 0.5 else 0) for item in x_test]
y_test = keras.utils.to_categorical(x_test_reformed, num_classes=2)
with open('/var/tmp/annhouga/data/yTest.json', 'w') as outfile:
    json.dump(y_test.tolist(), outfile)