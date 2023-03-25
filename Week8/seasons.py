from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    birth = input("Date of Birth: ")
    try:
        year, month, day = check_birthdate(birth)
    except:
        sys.exit("Invalid Date")

    dob = date(int(year), int(month), int(day))
    today = date.today()
    age = today - dob
    minutes = age.days * 24 * 60
    output = p.number_to_words(minutes, andword = "")
    print(output.capitalize() + " minutes")


def check_birthdate(birth):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth):
        year, month, day = birth.split("-")
        return year, month, day


if __name__ == "__main__":
    main()