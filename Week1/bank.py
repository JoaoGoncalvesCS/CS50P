#Getting Greating from user
greating = input("Greating: ").lower().strip()

#Checking if hello is in greating
if "hello" in greating:
    print("$0")

#Checking if is any greating starting with an h
elif "h" == greating[0]:
    print("$20")

#If not any of those conditions, printing $100
else:
    print("$100")