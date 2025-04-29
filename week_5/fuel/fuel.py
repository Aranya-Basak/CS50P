def main():
    p = (input("Fraction: "))
    p = convert(p)
    p = gauge(p)
    print(p)


def convert(fraction):
    fraction = fraction.split("/")
    a = int(fraction[0])
    b = int(fraction[1])
    if a > b and b != 0:
        raise ValueError
    elif b == 0:
        raise ZeroDivisionError
    else:
        return round((a / b) * 100)



def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
