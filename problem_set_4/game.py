from random import randint


def main():
    play(set_level())


def set_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level < 1:
                continue
            else:
                return randint(1, level)


def play(number: int) -> None:
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        else:
            if guess < 1:
                continue
            elif guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
            else:
                print("Just right!")
                break
        

if __name__ == "__main__":
    main()