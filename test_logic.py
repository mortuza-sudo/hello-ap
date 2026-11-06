from logic import add


from logic import add

def test_add_positive_numbers():
    assert add(5, 3) == 8

def test_add_negative_numbers():
    assert add(-5, -3) == -8

def test_add_positive_and_negative():
    assert add(10, -5) == 5

def test_add_zero():
    assert add(5, 0) == 5

def test_add_float_numbers():
    assert add(2.5, 3.5) == 6.0

def test_add_two_zeros():
    assert add(0, 0) == 0