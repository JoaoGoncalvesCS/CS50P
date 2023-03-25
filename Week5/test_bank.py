from bank import value

def main():
    #Calling the test functions
    test_0()
    test_20()
    test_100()

#Testing the return 0
def test_0():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0

#Testing the return 20
def test_20():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("hey") == 20
    assert value("Hey") == 20

#Testing the return 100
def test_100():
    assert value("Good morning") == 100
    assert value("Good afternoon") == 100


if __name__ == "__main__":
    main()