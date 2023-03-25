import sys
import csv

def main():
    #Checking the command-line arguments
    arguments()
    output = []
    #Trying to open the file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                output.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})
    #If can not open the file, does not exist.
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    #Writting new CSV file
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house":row["house"]})


def arguments():
    #Checking how many arguments on the command-line
    if len(sys.argv) < 3:
        sys.exit("Two few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Two many command-line arguments")
    #Checking if it is a CSV file
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()