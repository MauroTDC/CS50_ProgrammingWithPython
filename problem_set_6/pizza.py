from tabulate import tabulate
import sys
import csv


def main():
    filename = get_file()
    show_prices(filename)


def get_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        try:
            filename = sys.argv[1].lower()
            if filename.split(".")[1] != "csv":
                sys.exit("Not a CSV file")
            else:
                return filename
        except IndexError:
            sys.exit("Not a CSV file")


def show_prices(file: str) -> None:
    data = []
    try:
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                data.append(row)
        print(tabulate(data, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()