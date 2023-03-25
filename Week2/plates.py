def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Checking if the lenght of plate is more than 2 and less than 6
    if len(s) < 2 or len(s) > 6:
        return False

    #Checking if plates start with at leat 2 letters
    if s[0].isalpha() == False or s[1].isalpha == False:
        return False

    #Checking if numbers come at the end of the plate and the first number can not be 0
    i = 0

    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    #Removing periods, spaces and punctuation marks
    for word in s:
        if word in [".", " ", "!", "?"]:
            return False

    return True

main()