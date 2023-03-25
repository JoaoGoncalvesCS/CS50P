from um import count

def main():
    test_uplow_cases()
    test_um()
    test_spaces()

def test_uplow_cases():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks um...") == 2

def test_um():
    assert count("yummi") == 0

def test_spaces():
    assert count("Hello um world") == 1
    assert count("um?") == 1


if __name__ == "__main__":
    main()