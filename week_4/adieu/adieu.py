import inflect

p = inflect.engine()
def main():
    raw_list = create_list()
    out = p.join(raw_list)
    print(f"Adieu, adieu, to {out}")

def create_list():
    k = []                                          # declare a list to be used in func
    while True:                                     # loop
        try:                                        # getting user input and adding them in list by full uppercase
            k.append(input("Name: "))
        except EOFError:                            # detecting ctrl + d and returning the list
            print("\n")
            return k

main()
