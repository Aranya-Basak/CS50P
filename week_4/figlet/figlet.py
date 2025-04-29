import random
import sys
from pyfiglet import Figlet

argue = ["-f", "--font"]
figlet = Figlet()
def main():
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        a = input("Input: ")
        render(a, font)
    elif len(sys.argv) == 3 and sys.argv[1] in argue and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
        a = input("Input: ")
        render(a, font)
    else:
        sys.exit("Invalid Usage & Font")


def render(text, f):
    figlet.setFont(font=f)
    print("Output: ")
    print(figlet.renderText(text))

main()
