month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():  # 9/8/1636    September 8, 1636
    while True:
        try:
            p = input("Date: ").strip()
            if "/" in p:
                p = p.split("/")
                if 0 < int(p[0]) <= 12 and 0 < int(p[1]) <= 31:
                    print(f"{p[2]}-{p[0].zfill(2)}-{p[1].zfill(2)}")
                    break
                else:
                    raise Exception()
            elif "," in p:
                p = p.split(" ")
                if p[0] in month and 1 <= int(p[1][-2]) <= 31:
                    a = f"{month.index(p[0]) + 1}"
                    print(f"{p[2].zfill(4)}-{a.zfill(2)}-{p[1][-2].zfill(2)}")
                    break
                else:
                    raise Exception()
            else:
                raise Exception()
        except Exception:
            pass


main()
