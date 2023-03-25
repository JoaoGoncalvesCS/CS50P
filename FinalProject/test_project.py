from project import email, password, username


def test_email():
    assert email is not None
    assert email is not "@gmail.com"
    assert email is not "@yahoo.com"
    assert email is not "@outlook.com"

def test_password():
    assert password is not None
    assert password is not "Maria"
    assert password is not "12345"
    assert password is not "maria1234"

def test_username():
    assert username is not None
    assert username is not password
    assert username is not "A"
    assert username is not "Hihowareyouguys"