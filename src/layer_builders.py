from keras.layers import Dense, Dropout, Activation

def make_layer(layer_config, additional_args):
    print('-----------', layer_config)
    switcher = {
        'Dense': (lambda args : Dense(**args)),
        'Dropout': (lambda args : Dropout(**args))
    }
    layer_type = layer_config['type']
    layer_config.pop('type', None)
    args = { **additional_args, **layer_config }
    return switcher.get(layer_type, 'Layer Not Recognized.')(args)
