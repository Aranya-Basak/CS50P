vowl = ["a", "e", "i", "o", "u"]
wrd = []
def main():
    n = input("Input: ")
    n = shorten(n)
    print(n)


def shorten(word):
    global wrd
    for p in word:
        if p.lower() in vowl:
            continue
        else:
            wrd.append(p)
    a = "".join(wrd)
    wrd = []
    return a



if __name__ == "__main__":
    main()
