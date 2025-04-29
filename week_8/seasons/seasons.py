from datetime import date
import sys
import inflect
import re

p = inflect.engine()

def main():
    b_day_1 = input("Date of Birth: ")
    try:
        yr, mnt, day = tst_date(b_day_1)
    except:
        sys.exit("Invalid Date")
    b_day_1 = date(int(yr), int(mnt), int(day))
    today = date.today()
    minutes = (today - b_day_1).days * 24 * 60
    print((p.number_to_words(minutes, andword="")).capitalize() + " minutes")

def tst_date(b_day):
    if re.search(r"^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$", b_day):
        return b_day.split("-")


if __name__ == "__main__":
    main()
