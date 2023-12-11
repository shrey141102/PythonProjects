import random
import tkinter as tk

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

def play_game():
    def get_choices():
        player_choice = player_var.get().lower()
        options = ["rock", "paper", "scissors"]
        player_selection = {'rock': rock, 'paper': paper, 'scissors': scissors}
        computer_choice = random.choice(options)
        Choices = {"player": player_choice, "computer": computer_choice}
        return Choices, player_selection

    def check_win(player, computer, player_selection):
        result_label.config(text="")
        result_text = f"You chose {player}\n {player_selection[player]}, computer chose {computer}\n {player_selection[computer]}\n\n"
        if player == computer:
            result_text += "It's a tie!"
        elif player == "rock":
            if computer == "scissors":
                result_text += "Rock smashes scissors! You win!"
            else:
                result_text += "Paper covers rock! You lose!"
        elif player == "paper":
            if computer == "rock":
                result_text += "Paper covers rock! You win!"
            else:
                result_text += "Scissors cut paper! You lose!"
        elif player == "scissors":
            if computer == "paper":
                result_text += "Scissors cut paper! You win!"
            else:
                result_text += "Rock smashes scissors! You lose!"
        result_label.config(text=result_text)

    def on_button_click():
        choices, player_selection = get_choices()
        check_win(choices["player"], choices["computer"], player_selection)

    player_var = tk.StringVar()

    label = tk.Label(root, text="Enter a choice (rock, paper, scissors):")
    label.pack()

    entry = tk.Entry(root, textvariable=player_var)
    entry.pack()

    play_button = tk.Button(root, text="Play", command=on_button_click)
    play_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play_game()
root.mainloop()
