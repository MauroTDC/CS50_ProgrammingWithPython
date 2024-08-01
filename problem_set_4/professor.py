from random import randint


def main():
    problems = generate_problems(get_level())
    correct_answers = solve_problems(problems)

    print(f"Score: {correct_answers}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level not in [1,2,3]:
                continue
            else:
                return level


def generate_problems(level: int):
    problems = []
    if level == 1:
        for i in range(1,11):
            problems.append(f"{randint(1,9)} + {randint(1,9)}")
    elif level == 2:
        for i in range(1,11):
            problems.append(f"{randint(10,99)} + {randint(10,99)}")
    elif level == 3:
        for i in range(1,11):
            problems.append(f"{randint(100,999)} + {randint(100,999)}")
    return problems


def solve_problems(problems: list):
    correct = 0
    for problem in problems:
        error = 0
        print(problem, "=", end=" ")
        first_num = int(problem.split("+")[0])
        second_num = int(problem.split("+")[1])
        answer = first_num + second_num

        try:
            user_answer = int(input())
        except ValueError:
            user_answer = None
        
        while error < 2:
            if user_answer != answer:
                error += 1
                print("EEE")
                print(problem, "=", end=" ")
                try:
                    user_answer = int(input())
                except ValueError:
                    user_answer = 0
            else:
                correct += 1
                break
        if error == 2:
            print(problem, f"= {answer}")
    return correct


if __name__ == "__main__":
    main()