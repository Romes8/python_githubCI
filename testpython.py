
class Person():
    def __init__(self,name):
        self.name = name

    def add_numbers(n1,n2):
        return n1 + n2



Roman = Person("Roman")
Roman.add_numbers(4,2)


def test_add_numbers():
    assert Roman.add_numbers(4,2) == 6

def test_name():
    assert Roman.name == "Roman"
        

    

