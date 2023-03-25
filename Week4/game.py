import random

#Forever Loop
while True:
    try:
        #Prompting the user for the level
        level = int(input("Level: "))
        #Checking if level has a positive int
        if level > 0:
            break
    except:
        pass

#Getting the random number
number = random.randint(1, level)

while True:
    try:
        #Prompting the user for the guess
        guess = int(input("Guess: "))
        #Checking if guess has a positive int
        if guess > 0:
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass