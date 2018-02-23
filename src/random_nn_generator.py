import json, random, type_checkers as types

with open('../sample-NNs/sample-user-config.json', 'r') as f:
    user_config = json.load(f)

def handle_number_range(range):
    first_num = range[0]
    second_num = range[1]
    if types.is_int(first_num) and types.is_int(second_num):
        return random.randint(int(first_num), int(second_num))
    elif types.is_real_number(first_num) and types.is_real_number(second_num):
        return random.uniform(float(first_num), float(second_num))
    else:
        raise ValueError('Looked like you entered a range but values in the range are not valid.')

def handle_dict(a_dict):
    output_dict = {}
    for key, value in a_dict.items():
        output_dict[key] = generic_handler(value)
    return output_dict

def handle_list_of_dicts(list_of_dicts):
    return handle_dict(random.choice(list_of_dicts))

def generic_handler(value):
    if type(value) is str or types.is_real_number(value):
        return value
    elif types.is_list_with_two_numbers(value):
        return handle_number_range(value)
    elif types.is_list_of_dictionaries(value):
        return handle_list_of_dicts(value)
    elif type(value) is dict:
        return handle_dict(value)
    elif type(value) is list:
        return random.choice(value)
    else: # consider just taking out the top...
        return value

def handle_layers():
    numHiddenLayers = handle_number_range(user_config['numHiddenLayers'])
    layers = [handle_list_of_dicts(user_config['hiddenLayers']) for i in range(numHiddenLayers)]
    # layers = [5 for i in range(numHiddenLayers)]
    layers.insert(0, generic_handler(user_config['firstLayer']))
    layers.append(generic_handler(user_config['outputLayer']))
    return layers

def get_random_canned_config():
    new_config = {}
    new_config['data'] = user_config['data']
    new_config['epochs'] = generic_handler(user_config['epochs'])
    new_config['batchSize'] = generic_handler(user_config['batchSize'])
    new_config['layers'] = handle_layers()
    new_config['optimizer'] = generic_handler(user_config['optimizers'])
    new_config['loss'] = generic_handler(user_config['loss'])
    new_config['metrics'] = generic_handler(user_config['metrics'])
    return new_config


# TODO, should I use the generic handler for everything or use specific 'private functions' when appropriate? (i.e. everything should fall into the correct private function handler through the generic function....)