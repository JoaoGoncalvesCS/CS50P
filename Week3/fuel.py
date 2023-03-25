#Forever while loop
while True:
    #Get user input
    user = input("Fraction: ")

    #Try to split the the input
    try:
        numerator, denominator = user.split("/")

        #Convert the str into int
        int_numerator = int(numerator)
        int_denominator = int(denominator)

        #Calculating the division
        division = int_numerator / int_denominator

        #Checking if numerator is less than 1
        if division <= 1:
            break

    except (ValueError, ZeroDivisionError):
        pass

#Getting the percentage out of the division
percentage = int(round(division * 100))

#Associating E if percentage is less than 1
if percentage <= 1:
    print("E")
#Associating F if percentage is greater than 99
elif percentage >= 99:
    print("F")
#Last case cenario just printing the percentage
else:
    print(f"{percentage}%")