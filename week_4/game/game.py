import random
import sys

def main():
    while True:
        lvl = get_level()
        num_1 = get_num(lvl)
        try:
            while True:
                inp = int(input("Guess: "))
                if num_1 < inp:
                    print("Too large!")
                    continue
                elif num_1 > inp:
                    print("Too small!")
                    continue
                elif num_1 == inp:
                    print("Just right!")
                    sys.exit()
        except ValueError:
            pass

def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l > 0:
                return l
            else:
                raise ValueError
        except ValueError:
            pass

def get_num(level):
    a = random.randint(1, level)
    return a

main()
