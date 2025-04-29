gret = input("Greetings: ").strip().lower().split()[0]
if "hello" in gret:
    print("$0")
elif gret[0] == "h":
    print("$20")
else:
    print("$100")



