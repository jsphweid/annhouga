# ANNHOUGA
Automated Neural Network Hyperparameter Optimization Using Genetic Algorithms (and Python, Keras / Tensorflow, maybe Javascript / Kue, Docker, AWS)


# Running

I assume you are running python 3 and anaconda.

Install virtual environment: `conda create --name annhouga`

Activate: `source activate annhouga`

Deactivate: `source deactivate`


Now that your virtual environment is activated... install python dependencies:
 1. `pip install keras`
 2. `pip3 install --upgrade tensorflow`

Finally, build data:
`python ./sample-NNs/generate-data-for-simple-binary-classifier.py`

Then run...:
`python ./src/run.py`

`conda create -n annhouga`
`source activate yourenvname`

Install redis: https://redis.io/topics/quickstart
and
`pip install redis`

start - `rabbitmq-server`
stop - `rabbitmqctl stop`
 
