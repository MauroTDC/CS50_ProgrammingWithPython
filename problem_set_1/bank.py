def main():
    greeting = input("Greeting: ")
    bank_greeting(greeting)


def bank_greeting(txt: str) -> None:
    greeting = txt.lower().strip()
    if greeting[0:5] == "hello":
        print("$0")
    elif greeting [0:1] == "h":
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()