import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url_pattern = re.search(r"(http(s)?:\/\/(www\.)?youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if url_pattern:
            url_splitted = url_pattern.groups()
            return f"https://youtu.be/{url_splitted[3]}"


if __name__ == "__main__":
    main()