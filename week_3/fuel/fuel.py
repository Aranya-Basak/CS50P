def main():
    x, y = get_frac()
    z = (x / y) * 100
    if 0 <= z <= 1:
        print("E")
    elif 99 <= z <= 100:
        print("F")
    else:
        print(f"{round(z)}%")

def get_frac():
    while True:
        try:
            p = (input("Fraction: "))
            p = p.split("/")
            a = int(p[0])
            b = int(p[1])
            if a > b:
                raise Exception()
            elif b == 0:
                raise ZeroDivisionError
            else:
                return a, b
        except (ValueError, Exception, ZeroDivisionError):
            pass

main()

