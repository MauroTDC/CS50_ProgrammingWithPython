import re


def main():
    print(count(input("Text: ")))


def count(s: str):
    ums = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(ums)


if __name__ == "__main__":
    main()