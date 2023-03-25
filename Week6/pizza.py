import sys
import csv
from tabulate import tabulate

def main():
    arguments()
    #Variable for the table data
    data = []
    #Oppening the file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    #Checking if it does exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    #Printing the table
    print(tabulate(data[1:], headers = data[0], tablefmt = "grid"))

def arguments():
    #Checking how many arguments on the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    #Checking if it is a CSV file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()