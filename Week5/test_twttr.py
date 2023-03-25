from twttr import shorten

def main():
    #Calling the test functions
    test_lower_upper()
    test_numbers()
    test_punctuation()

#Testing letters upper and lower cases
def test_lower_upper():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwItTeR") == "TwtTR"

#Testing numbers
def test_numbers():
    assert shorten("1234") == "1234"

#Testing the punctuation
def test_punctuation():
    assert shorten("!?,.") == "!?,."

if __name__ == "__main__":
    main()