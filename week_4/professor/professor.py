import random

score = 0
prblm_cnt = 0
wrng = 0
def main():
    global prblm_cnt
    global score
    global wrng
    lvl = get_level()
    while prblm_cnt < 10:
        prblm_cnt = prblm_cnt + 1
        int_1 = generate_integer(lvl)
        int_2 = generate_integer(lvl)
        sol = int_1 + int_2
        prblm = (f"{int_1} + {int_2} = ")
        wrng = 0
        while wrng < 3:
            ans = (input(f"{prblm}"))
            if wrng < 3 and ans == f"{sol}":
                score = score + 1
                break
            elif wrng < 3 and ans != f"{sol}":
                print("EEE")
                wrng = wrng + 1
                continue
        if wrng == 3:
            print(f"{int_1} + {int_2} = {sol}")
        if prblm_cnt == 10:
            print(f"Score: {score}")
            break
        else:
            continue


def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if 1 <= l <= 3:
                return l
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        a = random. randint(0, 9)
        return a
    elif level == 2:
        a = random. randint(10, 99)
        return a
    elif level == 3:
        a = random. randint(100, 999)
        return a

if __name__ == "__main__":
    main()
