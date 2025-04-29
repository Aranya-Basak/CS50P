import sys
import csv

def main():
    if len(sys.argv) > 3:                                       # checks for errors
        sys.exit("Too many arguements")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguements")
    elif sys.argv[1][-4:] != ".csv" and sys.argv[2][-4:]:
        sys.exit("Not a CSV file")
    else:                                                       # calls func to create dict and calls func to write in output file
        dict = format(sys.argv[1])
        write(dict, sys.argv[2])

def format(file):
    name = []                                                   # empty list of dict formed
    try:
       with open(file, "r") as f:                               # opens input file
        reader = csv.DictReader(f)                              # returns ordered dict to iterate over
        for row in reader:                                      # takes each dict and adds to the list
            name.append(row)
        return name
    except FileNotFoundError:
        sys.exit("File does not exist")


def write(d, file):
    with open(file, "w") as f:                                  # opens output file
        writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        writer.writeheader()                                    # returns ordered dict to iterate over amd writes header
        for row_2 in d:
            first = row_2["name"].split(",")[1].strip()         # splits name
            last = row_2["name"].split(",")[0]
            writer.writerow(                                    # writes according to specific fieldname one at a time
                {
                    "first": first,
                    "last": last,
                    "house": row_2["house"]
                }
            )

if __name__ == "__main__":
    main()
