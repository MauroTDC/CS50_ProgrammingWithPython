from validator_collection import validators


def main():
    if validate_email(input("What's your email address? ")):
        print("Valid")
    else:
        print("Invalid")


def validate_email(email: str):
    try:
        validators.email(email)
        return True
    except:
        return False


if __name__ == "__main__":
    main()