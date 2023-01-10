import math
x = float((input("enter your number : ")))
op = input("choose operation : ")
if op == "radical":
    print(math.sqrt(x))
if op == "sin":
    print(math.sin(x))
if op == "cos":
    print(math.cos(x))
if op == "tan":
    print(math.tan(x))
if op == "factorial":
    y = int(x)
    print(math.factorial(y))
if op == "cot":
    cot = math.cos(x)/math.sin(x)
    print(cot)





