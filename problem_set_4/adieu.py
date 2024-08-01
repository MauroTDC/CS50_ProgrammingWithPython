
def main():
    names = get_names()
    print_lyrics(names)

def get_names():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name.title())
        except (KeyboardInterrupt, EOFError):
            print()
            return names

def print_lyrics(names: list) -> None:    
    list_names = ""
    if len(names) == 1:
        list_names = names[0]
    elif len(names) >= 2:
        for i in range(len(names[:-1])):
            list_names += f"{names[i]}, "
        list_names += f"and {names[-1]}"

    print(f"Adieu, adieu, to {list_names}")


if __name__ == "__main__":
    main()