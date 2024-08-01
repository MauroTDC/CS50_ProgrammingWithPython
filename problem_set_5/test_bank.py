def main():
    test_bank()


def bank_greeting(txt: str):
    greeting = txt.lower().strip()
    if greeting[0:5] == "hello":
        return "$0"
    elif greeting [0:1] == "h":
        return "$20"
    else:
        return "$100"


def test_bank():
    assert bank_greeting("Hello, Newman") == "$0"
    assert bank_greeting("H") == "$20"
    assert bank_greeting("CS50") == "$100"


if __name__ == "__main__":
    main()