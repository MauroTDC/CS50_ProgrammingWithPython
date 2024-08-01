def main():
    text = input("Input: ")
    shorten(text)


def shorten(text: str):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    new_text = ""
    for i in range(len(text)):
        if text[i] not in vowels:
            new_text += text[i]
    print(new_text)
    return new_text


if __name__ == "__main__":
    main()