def main():
    c = input("What time is it? ")
    c = convert(c)

    if 7.0 <= c <= 8.0:
        print("breakfast time")
    elif 12.0 <= c <= 13.0:
        print("lunch time")
    elif 18.0 <= c <= 19.0:
        print("dinner time")


def convert(time):
    time_1 = float(time.split(":")[0])
    time_2 = float(time.split(":")[1])
    time = time_1 + (time_2/60)
    return time
if __name__ == "__main__":
    main()

