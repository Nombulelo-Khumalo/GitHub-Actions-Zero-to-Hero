# This is a test commit, unit testing
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    
    
def subtract(a, b):
    return a - b

def test_subtract():
    assert subtract(10, 5) == 5
    
