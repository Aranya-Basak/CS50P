from validator_collection import validators, errors


def main():
    print(check(input("What' your email address: ")))


def check(s):
    try:
        email_address = validators.email(s)
        return f"Valid"

    except errors.EmptyValueError:
        return f"Invalid"
    except errors.InvalidEmailError:
        return f"Invalid"

if __name__ == "__main__":
    main()
