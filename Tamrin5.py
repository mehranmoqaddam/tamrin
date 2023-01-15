import random

while True:
    tas = random.randint(1, 6)
    print(tas)
    if tas == 6:
        print(random.randint(1,6)," ",random.randint(1,6))
        break