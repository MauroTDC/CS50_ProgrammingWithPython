import sys

def main():
    try:
        file = sys.argv[1]
        print(count_lines(file))
    except IndexError:
        sys.exit("Missing command-line argument")

def count_lines(filename: str):
    num_lines = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                if len(line.strip()) > 1:
                    if "#" not in line.strip():
                        num_lines += 1
            return num_lines
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()