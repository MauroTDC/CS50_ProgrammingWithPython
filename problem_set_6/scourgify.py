import sys
import csv

def main():
    old_file, new_file = get_files()
    data = get_data(old_file)
    create_file(data, new_file)

def get_files():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            old_file = sys.argv[1].lower()
            new_file = sys.argv[2].lower()
            if ".csv" not in old_file or ".csv" not in new_file:
                sys.exit("Not a CSV file")
            return old_file, new_file
        except IndexError:
            sys.exit("Not a CSV file")

def get_data(old_f: str):
    data = []
    try:
        with open(old_f, "r") as old_file:
            reader = csv.reader(old_file)
            i = 0
            for row in reader:
                if i > 0:
                    last, first = row[0].split(", ")
                    data.append({"first": first, "last": last, "house": row[1]})
                i+=1
        return data
    except FileNotFoundError:
        sys.exit("File not found")

def create_file(data: list, filename: str):
    with open(filename, "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=["first","last","house"])
        writer.writerow({"first":"first","last":"last","house":"house"})
        for item in data:
            writer.writerow({"first": item["first"], "last": item["last"], "house": item["house"]})

if __name__ == "__main__":
    main()