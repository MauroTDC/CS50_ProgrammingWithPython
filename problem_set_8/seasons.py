import datetime
import inflect
import sys
import re


inf = inflect.engine()


def main():
    print(calculate_minutes(input("Date of Birth: ")))


def calculate_minutes(birth: str):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth):
        year, month, day = birth.split("-")            
        birth_date = datetime.date(int(year), int(month), int(day))
        act_date = datetime.date.today()
        diff = act_date - birth_date
        minutes = diff.days * 24 * 60
        output = inf.number_to_words(minutes, andword="")
        return output.capitalize() + " minutes"
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()