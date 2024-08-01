def main():
    convert(input("What time is it? "))


def convert(time: str) -> None:
    time = time.lower()
    hour = time.split(":")[0]

    if len(time) > 5:
        am_pm = time[5:].strip().replace(".","")
        if am_pm == "am":
            if hour in ("7", "8", "07", "08"):
                print("breakfast time")
            elif hour == "12":
                print("lunch time")
        elif am_pm == "pm":
            if hour in ("1", "01"):
                print("lunch time")
            elif hour in ("6", "7", "06", "07"):
                print("dinner time")
    else:
        if hour in ("7", "8", "07", "08"):
            print("breakfast time")
        elif hour in ("12", "13"):
            print("lunch time")
        elif hour in ("18", "19"):
            print("dinner time")
        
        
if __name__ == "__main__":
    main()