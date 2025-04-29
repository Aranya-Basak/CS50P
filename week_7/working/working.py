import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(
        r"^(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$",
        s,
    )
    if matches:
        st_tm = std(matches.group(1), matches.group(2), matches.group(3))
        ed_tm = std(matches.group(4), matches.group(5), matches.group(6))
        return f"{st_tm} to {ed_tm}"
    else:
        raise ValueError


def std(hr, min, mer):
    if hr == "12":
        if mer == "AM":
            hr = "00"
        else:
            hr = "12"
    else:
        if mer == "AM":
            hr = f"{int(hr):02}"
        else:
            hr = f"{(int(hr)+12):02}"
    if min == None:
        min = "00"
    else:
        min = f"{int(min):02}"

    return f"{hr}:{min}"


if __name__ == "__main__":
    main()
