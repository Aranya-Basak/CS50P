ans = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().title()

match ans:
    case "42" | "Forty-Two" | "Forty Two":
        print("Yes")
    case _:
        print("No")

