def main():
    print(convert(input("Input: ")))


def convert(txt: str):
    return txt.replace(":)", "🙂").replace(":(","😟")


if __name__ == "__main__":
    main()