import sys
cnt = 0
def main():
    if len(sys.argv) > 2:
        sys.exit("Too many arguements")
    elif len(sys.argv) < 2:
        sys.exit("Too few arguements")
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")
    else:
        res = line_count(sys.argv[1])
        print(res)

def line_count(file):
    global cnt
    try:
        with open(file.strip(), "r") as f:
            for line in f:
                if line.strip() == "":
                    pass
                elif line.strip().startswith("#"):
                    pass
                else:
                    cnt = cnt + 1
            return cnt
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
