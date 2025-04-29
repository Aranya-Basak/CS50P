p = input("camelCase: ")
print("snake_case: ", end="")
for s in p:
    if s.islower() == True:
        print(s, end="")
    else:
        q = s.lower()
        print(f"_{q}", end="")
print("\n")
