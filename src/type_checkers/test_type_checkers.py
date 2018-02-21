import type_checkers as types

def test_basic_is_int():
    assert types.is_int(5) == True
