from working import convert
import pytest

def main():
    test_format()
    test_time()
    test_hour()
    test_minute()

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")
    with pytest.raises(ValueError):
        convert("8:70 AM to 12:70 PM")
    with pytest.raises(ValueError):
        convert("9AM to 8PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9AM - 8PM")
    with pytest.raises(ValueError):
        convert("09:00 - 17:00")


def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_hour():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")

def test_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")


if __name__ == "__main__":
    main()