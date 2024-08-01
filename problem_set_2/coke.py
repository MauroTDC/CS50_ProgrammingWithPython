def main():
    coke_machine()


def coke_machine() -> None:
    total = 0
    while total < 50:
        print(f"Amount due: {50 - total}")
        amount = int(input("Insert Coin: "))
        if amount in [25, 10, 5]:
            total += amount

    change_owed = total - 50
    print(f"Change owed: {change_owed}")


if __name__ == "__main__":
    main()