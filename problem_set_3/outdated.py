months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    convert_date_format()


def convert_date_format() -> None:
    while True:
        try:
            date = input("Date: ").lower().strip()
            if "/" in date:
                month, day, year = map(int, date.split("/"))
                if month > 12 or month < 1 or day > 31 or day < 1 or year < 1:
                    continue
                else:
                    print(f"{year}-{month:02}-{day:02}")
                break
            elif "," in date:
                month = date.split(" ")[0]
                day = int((date.split(" ")[1])[:-1])
                year = int(date.split(" ")[2])

                if day > 31 or day < 1 or year < 1:
                    continue
                else:
                    month_index = 0
                    for i in range(len(months)):
                        if month.lower() == months[i].lower():
                            month_index = i + 1

                    print(f"{year}-{month_index:02}-{day:02}")
                    break            
            else:
                continue
        except ValueError:
            continue


if __name__ == "__main__":
    main()