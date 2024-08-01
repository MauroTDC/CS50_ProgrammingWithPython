def main():
    load_grocery_list()


def load_grocery_list() -> None:
    list = {}
    print("Grocery list: ")
    while True:
        try:
            item = input()
            if item.upper() in list:
                list[item.upper()] += 1
            else:
                list[item.upper()] = 1
        except (KeyboardInterrupt, EOFError):
            for item, amount in sorted(list.items()):
                print(amount, item)
            return


if __name__ == "__main__":
    main()