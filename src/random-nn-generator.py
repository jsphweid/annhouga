import json, random

with open('../sample-NNs/sample-user-config.json', 'r') as f:
    user_config = json.load(f)

def is_int(potential_int):
    return type(is_int) is int

def is_float(potential_float):
    return type(potential_float) is float

def is_real_number(potential_num):
    return is_int(potential_num) or is_float(potential_num)

def is_list_with_two_numbers(value):
    return type(value) is list and len(value) == 2 and is_real_number(value[0]) and is_real_number(value[1])

def is_list_of_dictionaries(value):
    return type(value) is list and all(type(item) is dict for item in value)

def handle_number_range(range):
    first_num = range[0]
    second_num = range[1]
    if is_int(first_num) and is_int(second_num):
        return random.randint(first_num, second_num)
    elif is_real_number(first_num) and is_real_number(second_num):
        return random.uniform(first_num, second_num)
    else:
        raise ValueError('Looked like you entered a range but values in the range are not valid.')

def handle_list_of_dicts(list_of_dicts):
    output_dict = {}
    random_dict = random.choice(list_of_dicts)
    for key, value in random_dict.items():
        output_dict[key] = generic_handler(value)
    return output_dict

def generic_handler(value):
    if type(value) is str or is_real_number(value) or type(value) is dict:
        return value
    elif is_list_with_two_numbers(value):
        return handle_number_range(value)
    elif is_list_of_dictionaries(value):
        return handle_list_of_dicts(value)
    elif type(value) is list:
        return random.choice(value)
    else: # consider just taking out the top...
        return value

new_config = {}
new_config['data'] = user_config['data']
new_config['epochs'] = generic_handler(user_config['epochs'])
new_config['batch_size'] = generic_handler(user_config['batch_size'])
# numHiddenLayers
new_config['optimizers'] = generic_handler(user_config['optimizers'])
new_config['loss'] = generic_handler(user_config['loss'])
new_config['metrics'] = generic_handler(user_config['metrics'])

print(new_config)
