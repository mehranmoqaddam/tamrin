import random

secret_number = random.randint(0 , 30)
i = 0

while True :
    guess_number = int(input("Enter your guess : "))
    i += 1
    if guess_number == secret_number:
        print("You won")
        print("Number of guesses: " ,i)
        break
    if guess_number > secret_number :
        print("Boro payintar" )
    else :
        print("Boro balatar" )

