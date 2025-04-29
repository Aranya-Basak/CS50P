raw_list = []                                       # list for storing raw value
sort_dict = {}                                      # dict for sorted grocery

def main():
    global raw_list
    global sort_dict
    raw_list = create_list()                        # initiate func to get user input
    for a in raw_list:                              # itterating over the list item to check and count the items and adding them to dict
        if a in sort_dict:
            sort_dict[a] += 1
        else:
            sort_dict[a] = 1
    sort_dict = dict(sorted(sort_dict.items()))     # sorting dict
    for item in sort_dict.keys():
        print(f"{sort_dict[item]} {item}")          # printing in desired manner


def create_list():
    p = []                                          # declare a list to be used in func
    while True:                                     # loop
        try:                                        # getting user input and adding them in list by full uppercase
            p.append(input("").upper())
        except EOFError:                            # detecting ctrl + d and returning the list
            print("\n")
            return p

main()
