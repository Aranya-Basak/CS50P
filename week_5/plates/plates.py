def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():    # Checks for length and punctuation
        if s.isalpha():                     # Checks if all are letters
            return True
        else:
            if s[0:2].isalpha() and s[-1].isdigit():   # Checks for first two places are letter and last is digit
                for i in range(len(s)):         # goes through every index
                    if s[i].isdigit():
                        if s[i] == "0":
                            return False
                        elif not s[i:].isdigit():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False

if __name__ == "__main__":
    main()
