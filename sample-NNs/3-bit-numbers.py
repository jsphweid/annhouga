import numpy as np
import tensorflow as tf 
from random import randint


def convertDecimalToBinaryArray(num):
	binary_number_as_string = bin(num)[2:].zfill(NUM_BITS)
	return list(map(int, binary_number_as_string))

def getRandomDataPair():
	randomInt = randint(0, HOT_LENGTH - 1)
	hotEncoded = [0] * HOT_LENGTH
	hotEncoded[randomInt] = 1
	binaryArray = convertDecimalToBinaryArray(randomInt)
	return [binaryArray, hotEncoded]

def getBatch(size):
	inputs = []
	labels = []
	for i in range(size):
		x_input, y_label = getRandomDataPair()
		inputs.append(x_input)
		labels.append(y_label)
	return [inputs, labels]


NUM_BITS = 12
HOT_LENGTH = 2 ** NUM_BITS


learning_rate = 0.1
num_steps = 50000
batch_size = 50
display_step = 20

# Network Parameters
n_hidden_1 = 16 # 1st layer number of neurons
n_hidden_2 = 16 # 2nd layer number of neurons
num_input = NUM_BITS # MNIST data input (img shape: 28*28)
num_classes = HOT_LENGTH # MNIST total classes (0-9 digits)

# tf Graph input
X = tf.placeholder("float", [None, num_input])
Y = tf.placeholder("float", [None, num_classes])

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([num_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, num_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([num_classes]))
}


# Create model
def neural_net(x):
    # Hidden fully connected layer with 256 neurons
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    # Hidden fully connected layer with 256 neurons
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    # Output fully connected layer with a neuron for each class
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Construct model
logits = neural_net(X)
prediction = tf.nn.softmax(logits)

# Define loss and optimizer
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)

# Evaluate model
correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    for step in range(1, num_steps + 1):
        batch_x, batch_y = getBatch(batch_size)
        # Run optimization op (backprop)
        sess.run(train_op, feed_dict={X: batch_x, Y: batch_y})
        if step % display_step == 0 or step == 1:
            # Calculate batch loss and accuracy
            loss, acc = sess.run([loss_op, accuracy], feed_dict={X: batch_x,
                                                                 Y: batch_y})
            print("Step " + str(step) + ", Minibatch Loss= " + \
                  "{:.4f}".format(loss) + ", Training Accuracy= " + \
                  "{:.3f}".format(acc))

    print("Optimization Finished!")

    # Calculate accuracy for MNIST test images
    # print("Testing Accuracy:", \
    #     sess.run(accuracy, feed_dict={X: mnist.test.images,
    #                                   Y: mnist.test.labels}))    
