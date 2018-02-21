def couldBeBool(potential_bool):
    type(potential_bool) == bool

def is_int(potential_int):
    try:
        print('potential_int', potential_int)
        num = int(potential_int)
        print('num', num)
        return isinstance(num, int) and not couldBeBool(num)
    except Exception:
        return False

def is_float(potential_float):
    try:
        num = float(potential_float)
        return isinstance(num, float) and not couldBeBool(num)
    except Exception:
        return False

def is_real_number(potential_num):
    return is_int(potential_num) or is_float(potential_num)

def is_list_with_two_numbers(value):
    return type(value) is list and len(value) == 2 and is_real_number(value[0]) and is_real_number(value[1])

def is_list_of_dictionaries(value):
    return type(value) is list and all(type(item) is dict for item in value)