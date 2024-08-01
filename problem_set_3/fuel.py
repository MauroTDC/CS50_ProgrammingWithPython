def main():
    fuel_percentage()

def fuel_percentage() -> None:
    while True:
        try:
            fraction = input("Enter a fraction: ")
            x = int(fraction.split("/")[0])
            y = int(fraction.split("/")[1])
            result = round((x / y) * 100)
        except (ValueError, ZeroDivisionError, IndexError):
            continue
        else:
            if x > y:
                continue
            else:
                if result <= 1:
                    print("E")
                    break
                elif result >= 99:
                    print("F")
                    break
                elif result > 100 or result < 0:
                    continue
                else:
                    print(f"{result}%")
                    break
            
if __name__ == "__main__":
    main()