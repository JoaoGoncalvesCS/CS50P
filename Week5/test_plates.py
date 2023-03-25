from plates import is_valid

def main():
    #Calling the test functions
    test_range()
    test_twoletters()
    test_number_end()
    test_zero()
    test_punctuation()
    
#Plates must have a max of 6 characters and a min of 2
def test_range():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

#Plates must to start with at least two letters
def test_twoletters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

#Number can only come at the end of the plate
def test_number_end():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

#The first number cannot be 0
def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

#No puctuation allowed
def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI3 14") == False
    assert is_valid("PI3?14") == False

if __name__ == "__main__":
    main()