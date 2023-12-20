from logo import image
print(image)
import random

def get_user_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please choose from the given options.")

def check_guess(secret_number, guessed_number):
    if guessed_number == secret_number:
        return 0
    elif guessed_number < secret_number:
        return -1
    else:
        return 1

def main():
    print("Welcome to the Number Guessing Game 🎲")
    print("I'm thinking of a number between 1 and 100. Can you guess it? 🤔")

    difficulty = get_user_input("Choose difficulty: easy, medium, hard: ", ["easy", "medium", "hard"])

    if difficulty == "easy":
        secret_number = random.randint(1, 20)
        chances = 10
        print("You're playing on easy mode. The number is between 1 and 20.")
    elif difficulty == "medium":
        secret_number = random.randint(1, 50)
        chances = 7
        print("You're playing on medium mode. The number is between 1 and 50.")
    else:
        secret_number = random.randint(1, 100)
        chances = 5
        print("You're playing on hard mode. The number is between 1 and 100.")

    print(f"Let's start guessing! You have {chances} attempts.")

    while chances > 0:
        guess = input("Enter your guess : ")
        
        if not guess.isdigit() or not (1 <= int(guess) <= 100):
            print("Please enter a valid number between 1 and 100.")
            continue
        
        guess = int(guess)
        result = check_guess(secret_number, guess)

        if result == 0:
            print("Congratulations! You guessed it right!")
            print(f"The answer was indeed {secret_number}")
            break
        elif result == -1:
            print("Too low! Try aiming higher.")
        else:
            print("Too high! Try a lower number.")

        chances -= 1
        if chances > 0:
            print(f"You have {chances} attempts left.")

    if chances == 0:
        print("You've run out of chances. Better luck next time! 😔")
        print(f"The correct answer was {secret_number}")

if __name__ == "__main__":
    main()
