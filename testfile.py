import testpython

_Roman = testpython.Roman

def test_add_numbers():
    assert _Roman.add_numbers(4,2) == 6
    print("Test done")
    

def test_name():
    assert _Roman.name == "Roman"
        
