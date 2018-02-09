import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

# Generate dummy data
import numpy as np

x_train = np.random.random((1000, 1))
x_train_reformed = [(1 if item[0] > 0.5 else 0) for item in x_train]
y_train = keras.utils.to_categorical(x_train_reformed, num_classes=2) # hot encodes

x_test = np.random.random((100, 1))
x_test_reformed = [(1 if item[0] > 0.5 else 0) for item in x_test]
y_test = keras.utils.to_categorical(x_test_reformed, num_classes=2)



model = Sequential()

model.add(Dense(units=128, activation='relu', input_dim=1))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

optimizer = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(loss='categorical_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)