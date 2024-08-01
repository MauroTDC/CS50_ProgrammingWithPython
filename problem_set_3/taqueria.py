def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    get_total(menu)


def get_total(items: dict) -> None:
    total = 0
    while True:
        try:
            item = input("Item: ")
            if item.title() in items:
                total += items[item.title()]
        except (ValueError):
            continue
        except (KeyboardInterrupt, EOFError):
            print(f"Total: ${total}")
            break
    

if __name__ == "__main__":
    main()