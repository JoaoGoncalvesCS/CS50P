#Declaring the amount due variable
amount_due = 50

#Loop while the amount due is not 0
while amount_due > 0:
    print("Amount Due:", amount_due)

#Prompt user to insert coins
    coin = int(input("Insert Coins: "))

#Checking if coins are 5, 10, 25, 50
    if coin in [25, 10, 5]:
       amount_due -= coin

#Getting the change due
change_due = abs(amount_due)
print(change_due)
