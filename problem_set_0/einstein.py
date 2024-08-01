def main():
    try:
        mass = int(input("m: "))
        print(convert(mass))
    except ValueError:
        print("Mass must be a integer")


def convert(mass: int):
    return f"E: {mass*(300000000**2)}"


if __name__ == "__main__":
    main()