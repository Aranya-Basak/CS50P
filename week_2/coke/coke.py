# setting up changable global var
due = 50
insert = 0

def main():
    global insert, due
    while insert < 50:  #while insert is valid
        insert, due = p_input(insert, due)  #passing onto user input func
        if insert >= 50:
            print(f"Change Owed: {insert - 50}")    #owed calculation and print
            break
        else:
            continue


def p_input(n, p):
    while True:
        print(f"Amount Due: {p}")  #printing due
        k = int(input("Insert Coin: "))     #taking input
        if k == 25 or k == 10 or k == 5:    #validation of input
            n = n + k
            p = p - k
            return n, p
        else:   #if non-valid input given the loop continues
            continue

main()
