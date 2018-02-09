from keras.optimizers import SGD

def make_optimizer(optimizer_config):
    switcher = {
        'SGD': lambda: SGD(**optimizer_config)
    }
    optimizer_type = optimizer_config['type']
    optimizer_config.pop('type', None)
    return switcher.get(optimizer_type, 'Optimizer Not Recognized.')()