import requests
import sys


def main():
    bitcoins = get_bitcoins()
    req_bitcoins(bitcoins)


def get_bitcoins():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            bitcoins = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        else:
            return bitcoins


def req_bitcoins(amount: float) -> None:
    req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = req.json()
    usd = data["bpi"]["USD"]["rate_float"]
    result = float(usd) * float(amount)
    print(f"${result:,.4f}")


if __name__ == "__main__":
    main()