def main():
    #Getting input from the user
    message = input()

    #Calling the convert function
    emoji = convert(message)

    #Print the emoji
    print(emoji)

#Converting the string into emoji
def convert(message):
    message1 = message.replace(":)", '🙂')
    message2 = message1.replace(":(", '🙁')

    #Return String
    return message2

main()