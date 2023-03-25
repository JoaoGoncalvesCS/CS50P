#Prompting the user for input
string = input("Input: ")

#Printing the output
print("Output: ", end="")

#Loop for trough each letter
for char in string:
    #Checking if there's any vowels on the string
    if not char.lower() in ["a", "e", "i", "o", "u"]:
        print(char, end = "")

#Printing new line
print()