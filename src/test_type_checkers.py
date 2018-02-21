import type_checkers as types

# is_int

def test_basic_is_int():
    assert types.is_int(5) == True

def test_string_cannot_be_int():
    assert types.is_int('5') == False

def test_float_is_not_int1():
    assert types.is_int(1.53) == False

def test_float_is_not_int2():
    assert types.is_int(5.) == False

def test_boolean_is_not_int1():
    assert types.is_int(False) == False

def test_boolean_is_not_int2():
    assert types.is_int(True) == False

# is_float

def test_basic_is_float():
    assert types.is_float(4.3) == True

def test_string_cannot_be_float():
    assert types.is_float('5') == False

def test_int_is_not_float():
    assert types.is_float(5) == False

def test_plain_zero_is_not_float():
    assert types.is_float(0) == False

def test_boolean_is_not_float1():
    assert types.is_float(False) == False

def test_boolean_is_not_float2():
    assert types.is_float(True) == False

# is_real_number

def test_int_is_real_number():
    assert types.is_real_number(5) == True

def test_float_is_real_number():
    assert types.is_real_number(5.1) == True

def test_complex_num_is_not_real_number():
    assert types.is_real_number(1j) == False

def test_string_is_not_real_number():
    assert types.is_real_number('test') == False

def test_dict_is_not_real_number():
    assert types.is_real_number({}) == False

def test_list_is_not_real_number():
    assert types.is_real_number([1]) == False

# is_list_with_two_numbers

def test_is_list_with_two_numbers1():
    assert types.is_list_with_two_numbers([1, 2]) == True

def test_is_list_with_two_numbers2():
    assert types.is_list_with_two_numbers([1., 2]) == True

def test_is_list_with_two_numbers3():
    assert types.is_list_with_two_numbers([-4, 2.3248]) == True

def test_list_with_3_numbers_is_false():
    assert types.is_list_with_two_numbers([-4, 2.3248, 11]) == False

def test_list_with_a_string_is_false():
    assert types.is_list_with_two_numbers(['lol', 2.3248]) == False

def test_dict_with_two_items_is_false():
    assert types.is_list_with_two_numbers({ "one": 1, "two": 2 }) == False

# is_list_of_dictionaries

def test_is_list_of_dictionaries():
    assert types.is_list_of_dictionaries([{}, {}]) == True

def test_is_list_of_dictionaries_with_lists_is_false():
    assert types.is_list_of_dictionaries([[], []]) == False

def test_is_list_of_dictionaries_with_strs_is_false():
    assert types.is_list_of_dictionaries(['test', 'hi']) == False

def test_is_list_of_dictionaries_with_ints_and_dicts_is_false():
    assert types.is_list_of_dictionaries([5, {}]) == False


