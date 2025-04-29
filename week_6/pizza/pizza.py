import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many arguements")
    elif len(sys.argv) < 2:
        sys.exit("Too few arguements")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    else:
        res = format(sys.argv[1])
        print(tabulate(res, headers = "firstrow", tablefmt="grid"))

def format(file):
    menu = []
    try:
        with open(file, "r") as f:
            read = csv.reader(f)
            for row in read:
                menu.append(row)
            return menu
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
