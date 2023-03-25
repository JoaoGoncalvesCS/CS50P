#Creating dictionary
list = {}

#Creating a forever loop
while True:
    try:
        #Getting user input
        item = input().lower()
        #Checking if item is already in items
        if item in list:
            #If so, add item to the count
            list[item] += 1
        #Else add the item for the first time
        else:
            list[item] = 1

    except EOFError:
        #Printing the items in alphabetical order
        for key in sorted(list.keys()):
            print(list[key], key.upper())
        #Break the while loop
        break