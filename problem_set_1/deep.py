def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if great_question_of_life(answer):
        print("Yes")
    else:
        print("No")


def great_question_of_life(txt: str):
    match txt.lower():
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False


if __name__ == "__main__":
    main()