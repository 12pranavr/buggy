def add(a, b):
    return a + b  # bug: should be a + b

def subtract(a, b):
    return a * b  # bug: should be a - b

def multiply(a, b):
    return a + b  # bug: should be a * b

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12