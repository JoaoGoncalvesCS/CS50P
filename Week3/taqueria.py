#Putting the menu into a dict
menu = {
        "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#Creating the variable for total price
total = 0

#Creating a forever loop
while True:
    try:
        #Getting the user input
        item = input("Item: ").title()

        #Confirming if item is in dict
        if item in menu:
            #if so, add the item to the total price
            total += menu[item]
            #print the new value for total price
            print("Total: $", end="")
            print("{:.2f}".format(total))
    except EOFError:
        print()
        break