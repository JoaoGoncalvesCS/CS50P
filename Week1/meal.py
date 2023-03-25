def main():
    #Getting input from user
    answer = input("What time is it? ")

    #Calling the convert function
    time = convert(answer)

    #Breakfast Time
    if time >= 7 and time <= 8:
        print("Breakfast Time")

    #LunchTime
    if time >= 12 and time <= 13:
        print("Lunch Time")

    #Dinner Time
    if time >= 18 and time <= 19:
        print("Dinner Time")

def convert(time):
    #Hours and minutes
    hours, minutes = time.split(":")

    #Convert time into float
    new_minute = float(minutes) / 60

    #Return the result to the main function
    return float(hours) + new_minute

if __name__ == "__main__":
    main()