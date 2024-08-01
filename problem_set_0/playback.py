def main():
    print(playback(input("Input: ")))


def playback(txt: str):
    return txt.replace(" ","...")


if __name__ == "__main__":
    main()