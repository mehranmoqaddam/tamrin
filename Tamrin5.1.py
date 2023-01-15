import random

while True:
    tas = random.randint(1, 6)
    a = input("Type r to roll the dice : ")
    if a == "r":
        print(tas)
    if tas == 6:
        print(random.randint(1,6) , " " , random.randint(1,6))
