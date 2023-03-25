import random


def main():
    #Call the function get_level
    level = get_level()

    #Getting the score
    score = total(level)

    #Print the score
    print("Score: ", score)


def get_level():
    #Forever loop
    while True:
        #Prompting the user for a level and confirming that is between 1 and 3
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level

def generate_integer(level):
    #From the level get different random ints
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

#Creating a function to simulate each math problem
def simulate_round(x, y):
    count_tries =  1

    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer ==  (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False

#Creating a function to simulate a total
def total(level):
    count_round = 1
    score = 0

    while count_round <= 10:
        x , y = generate_integer(level)
        response = simulate_round(x,y)

        if response == True:
            score += 1
        count_round += 1
    return score

if __name__ == "__main__":
    main()