def main():
    say = input("Say somthing with emoticons ")
    print(convert(say))

def convert(p):
    return p.replace(":)", "🙂").replace(":(", "🙁")

main()
