exp = input("Expression: ").strip().split(" ")
a = exp[0]
b = exp[1]
c = exp[2]

match b:
    case "+":
        print(round(float(a)+float(c), 1))
    case "-":
        print(round(float(a)-float(c), 1))
    case "*":
        print(round(float(a)*float(c), 1))
    case "/":
        print(round(float(a)/float(c), 1))
