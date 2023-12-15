from logo import image
import random

print(image)
print("Welcome to the number guessing game 🫡")
print("I'm thinking of a number between 1 and 100 🧞‍♂️")

n = random.randint(1, 100)
# print(n)
# Options for diificulty
option = input("Type 'easy' or 'hard' for difficulty:  ")

if option == "easy":
    chance = 10
    flag = False
    while chance > 0:
        chance -= 1
        guess = int(input("Enter your guess?  "))
        if guess > n:
            print("Too High\nGuess again")
        elif guess < n:
            print("Too Low\nGuess again")
        else:
            # flag = True
            print("Correct Guess!!!")
            print(f"The answer is {n}")
            break
        print(f"You have {chance} attempts remaining to guess the number")
        if chance == 0:
            print("You've run out of chances, you lose. 😭")
            print(f"The correct answer was {n}")


elif option == "hard":
    chance = 5
    flag = False
    while chance > 0:
        chance -= 1
        guess = int(input("Enter your guess?  "))
        if guess > n:
            print("Too High\nGuess again")
        elif guess < n:
            print("Too Low\nGuess again")
        else:
            # flag = True
            print("Correct Guess!!!")
            print(f"The answer is {n}")
            break
        print(f"You have {chance} attempts remaining to guess the number")
        if chance == 0:
            print("You've run out of chances, you lose. 🥲")
            print(f"The correct answer was {n}")
else:
    print("Wrong input")
