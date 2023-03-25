#Prompting for user's input
camelcase = input("camelCase: ")

#Printing snake_case
print("snake_case: ", end="")

#Looping trough every letter
for letter in camelcase:


#Checking for uppercases, inserting the underscores within and turn them into lowercases
    if letter.isupper():
        print("_" + letter.lower(), end="")

    else:
        print(letter, end="")

#Printing the end space
print()