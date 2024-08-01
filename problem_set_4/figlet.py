from pyfiglet import Figlet
import sys
from random import randint


def main():
    show_message()


def show_message() -> None:
    figlet = Figlet()
    while True:
        fonts = figlet.getFonts()
        if len(sys.argv) == 1:
            text = input("Input: ")
            figlet.setFont(font=fonts[randint(0, len(fonts))])
            print("Output:")
            print(figlet.renderText(text))
            break
        elif len(sys.argv) == 3:
            if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                try:
                    figlet.setFont(font=sys.argv[2])
                except:
                    print("Font not found")
                    break
                else:
                    text = input("Input: ")
                    print("Output:")
                    print(figlet.renderText(text))
                    break
            else:
                print("Invalid usage")
                break
        else:
            print("Invalid usage")
            break


if __name__ == "__main__":
    main()