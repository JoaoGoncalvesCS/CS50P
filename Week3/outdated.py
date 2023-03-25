#List with all the names for the months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#Creating a forever loop
while True:
    #Getting user's input
    date = input("Date: ")

    #Replacing the comma in date with a space
    if "," in date:
        month, day, year = date.replace(",", " ").split()
        try:
            #Converting day and year into int
            day = int(day)
            year = int(year)
        except ValueError:
            continue
        #Confirming that the day goes up to 31 and there's only 12 months
        if day > 31 or month not in months:
            continue
        else:
            month = months.index(month) + 1
            break
    #Replacing the "/" with a space
    elif "/" in date:
        month, day, year = date.replace("/", " ").split()
        try:
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            continue
        if day > 31 or month > 12:
            continue
        break
    else:
        continue

print(f"{year}-{int(month):02}-{int(day):02}")