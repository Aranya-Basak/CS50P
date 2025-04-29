import re


def main():
    print(count(input("Text: ")))


def count(s):
    pat = r"\bum\b"
    lst = re.findall(pat, s, re.IGNORECASE)
    return len(lst)


if __name__ == "__main__":
    main()
