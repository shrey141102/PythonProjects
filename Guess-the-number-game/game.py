### GUI game for Guess-The-Number

import tkinter as tk
import random
from logo import image

def check_guess():
    global chances_left
    guess = int(guess_entry.get())
    if guess < number_to_guess:
        result_label.config(text="Too Low! Guess again.")
    elif guess > number_to_guess:
        result_label.config(text="Too High! Guess again.")
    else:
        result_label.config(text=f"Correct Guess! The number is {number_to_guess}.")
        chances_left = 0

    chances_left -= 1
    attempts_label.config(text=f'Chances left: {chances_left}')
    
    if chances_left == 0:
        result_label.config(text=f"You've run out of chances. The number was {number_to_guess}.")

def start_game():
    global number_to_guess, chances_left
    number_to_guess = random.randint(1, 100)
    chances_left = 10 if difficulty.get() == "Easy" else 5
    attempts_label.config(text=f'Chances left: {chances_left}')
    result_label.config(text="")
    guess_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Variables
number_to_guess = 0
chances_left = 0

# GUI elements
title_label = tk.Label(root, text="Welcome to the Number Guessing Game!", font=('Helvetica', 16))
title_label.pack(pady=10)

logo_label = tk.Label(root, text=image, font=('Arial', 14))
logo_label.pack()

difficulty = tk.StringVar()
difficulty.set("Easy")
difficulty_frame = tk.Frame(root)
difficulty_frame.pack()

easy_radio = tk.Radiobutton(difficulty_frame, text="Easy", variable=difficulty, value="Easy")
easy_radio.pack(side=tk.LEFT)

hard_radio = tk.Radiobutton(difficulty_frame, text="Hard", variable=difficulty, value="Hard")
hard_radio.pack(side=tk.LEFT)

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=5)

guess_label = tk.Label(root, text="Enter your guess (1-100):")
guess_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

check_button = tk.Button(root, text="Check Guess", command=check_guess)
check_button.pack(pady=5)

attempts_label = tk.Label(root, text="")
attempts_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
