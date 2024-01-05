import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Rock-Paper-Scissors")

CHOICES = ["rock", "paper", "scissors"]

def play_game(player_choice):
    computer_choice = random.choice(CHOICES)

    player_label.config(text=f"Player: {player_choice.capitalize()}")
    computer_label.config(text=f"Computer: {computer_choice.capitalize()}")

    if player_choice == computer_choice:
        result_label.config(text="It's a tie! You win!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result_label.config(text="You win!")
    else:
        result_label.config(text="You lose!")

    continue_button.pack()
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)

def on_button_click(choice):
    play_game(choice)

def play_again():
    result_label.config(text="")
    continue_button.pack_forget()
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)

# GUI elements
frame = tk.Frame(root)
frame.pack(pady=20)

rock_button = tk.Button(frame, text="Rock", width=10, command=lambda: on_button_click("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(frame, text="Paper", width=10, command=lambda: on_button_click("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(frame, text="Scissors", width=10, command=lambda: on_button_click("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

player_label = tk.Label(root, text="Player: ")
player_label.pack()

computer_label = tk.Label(root, text="Computer: ")
computer_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

continue_button = tk.Button(root, text="Continue", width=10, command=play_again)

root.mainloop()
