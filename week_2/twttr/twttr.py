n = input("Input: ")
print("Output: ", end="")

vowl = ["a", "e", "i", "o", "u"]
for p in n:
    if p.lower() in vowl:
        print("", end="")
    else:
        print(p, end="")

print("\n")
