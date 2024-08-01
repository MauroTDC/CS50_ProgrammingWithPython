def main():
    prompt = input("Input: ")
    print(indoor(prompt))


def indoor(txt: str):
    return txt.lower()


if __name__ == "__main__":
    main()