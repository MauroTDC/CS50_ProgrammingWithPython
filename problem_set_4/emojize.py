import emoji


def main():
    emojize(input("Input: "))


def emojize(text: str) -> None:
    print(emoji.emojize(f"Output: {text}", language="alias"))


if __name__ == "__main__":
    main()