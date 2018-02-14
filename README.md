# ANNHOUGA
Automated Neural Network Hyperparameter Optimization Using Genetic Algorithms (and Python, Keras / Tensorflow, maybe Javascript / Kue, Docker, AWS)


# Running

I assume you are running python 3.

You may or may not need to do all of these steps:
 1. instead pip `sudo easy_install pip`
 2. install virtualenv with pip `pip install --upgrade virtualenv`
 3. set up virtualenv `virtualenv --system-site-packages -p python3 ~/whatever-you-want`
 4. activate your virtualenv `source ~/whatever-you-want/bin/activate`

Now that your virtualenv is activated... install python dependencies:
 1. `pip install keras`
 2. `pip3 install --upgrade tensorflow`

Finally, build data:
`python ./sample-NNs/generate-data-for-simple-binary-classifier.py`

Then run...:
`python ./src/run.py`

 
