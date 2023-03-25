import sys

def main():
    #Checking the command line arguments number
    arguments_check()
    #Trying to open the file
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    #Checking if file does exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    #Creating a loop to check for white spaces or comments
    count = 0
    for line in lines:
        if lines_check(line) == False:
            count += 1
    print(count)

#Function to check the command line arguments
def arguments_check():
    #Checking for how many arguments in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command line-arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    #Checking if it is a python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def lines_check(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()