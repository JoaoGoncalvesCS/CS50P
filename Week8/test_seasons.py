from seasons import check_birthdate

def main():
    test_check_birthdate()

def test_check_birthdate():
    assert check_birthdate("1996-02-22") == ("1996", "02", "22")
    assert check_birthdate("1996-2-2") == None
    assert check_birthdate("February, 22, 1996") == None


if __name__ == "__main__":
    main()