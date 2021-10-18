def Hello():
    print("Hello world")

def add_numbers(n1,n2):
    return n1 + n2

def test_add_numbers():
    assert add_numbers(4,2) == 6
