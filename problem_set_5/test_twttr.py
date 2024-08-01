def main():
    test_twttr()


def shorten(text: str):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    new_text = ""
    for i in range(len(text)):
        if text[i] not in vowels:
            new_text += text[i]
    return new_text


def test_twttr():
    assert shorten("Twitter") == "Twttr"


if __name__ == "__main__":
    main()