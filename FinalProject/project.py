import re
import sys

def main():
    email()
    password()
    username()

def email():
    try:
        print("Email must contain '@harvard.edu.com'.")
        global email
        email = input("Email:  ").strip()
        if re.match(r"^(\w|\.)+@harvard.(edu).(com)$", email, re.IGNORECASE):
            print("Valid")
    except:
        sys.exit("Invalid Email")


def password():
    try:
        print("Password must contain 8 characters, including uppercase, lowercase and numbers.")
        global password
        password = input("Password: ")
        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
        if re.match(password_pattern, password):
            print("Valid")
    except:
        sys.exit("Invalid Password")

def username():
    print("Username must to be between 4 to 8 characters")
    global username
    username = input("Username: ")
    if re.match(username, password):
        sys.exit("Invalid Username")
    elif len(username) > 8:
        sys.exit("Too many characters")
    elif len(username) < 4:
        sys.exit("Need more characters")
    else:
        print("Valid")


if __name__ == "__main__":
    main()