def main():
    solve_math_calc(input("Expression: "))


def solve_math_calc(calc: str) -> None:
    try:
        first_num = float(calc.split(" ")[0])
        operator = calc.split(" ")[1]
        second_num = float(calc.split(" ")[2])
    except ValueError:
        print("Invalid format. Separate arguments with one space between")
    else:
        if operator == "+":
            result = first_num + second_num
        elif operator == "-":
            result = first_num - second_num
        elif operator == "*":
            result = first_num * second_num
        elif operator == "/":
            result = first_num / second_num
        print(f"{result:.1f}")
        

if __name__ == "__main__":
    main()