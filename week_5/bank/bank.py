def main():
    gret = input("Greetings: ")
    gret = value(gret)
    print(f"${gret}")


def value(greeting):
    greeting = greeting.strip().lower().split()[0]
    if "hello" in greeting:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
