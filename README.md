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
 3. `pip install mysqlclient` (requires mysql to be installed... `brew install mysql`)
 4. `pip install -U pytest`
 5. `pip install pytest-testmon`
 6. `pip install pytest-watch`

Finally, build data:
`python ./sample-NNs/generate-data-for-simple-binary-classifier.py`

Then run...:
`python ./src/run.py`

Run tests...:
`ptw -c`
