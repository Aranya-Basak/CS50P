menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
t = 0
def main():
    while True:
        try:
            global t
            a = order()
            t = t + a
            print(f"Total: ${t:.2f}")
        except EOFError:
            print("\n")
            break

def order():
    while True:
        try:
            p = input("Item: ").title()
            if p in menu:
                return float(menu[p])
            else:
                raise KeyError
        except KeyError:
            pass

main()
