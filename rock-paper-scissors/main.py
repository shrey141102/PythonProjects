import random

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


def get_choices():
    player_choice=input("Enter a choice(rock,paper,scissors):")
    options=["rock","paper","scissors"]
    player_selection = {'rock': rock, 'paper': paper, 'scissors': scissors}
    computer_choice = random.choice(options)
    Choices = {"player": player_choice, "computer": computer_choice}
    return Choices, player_selection

def check_win(player,computer,player_selection):
    print(f"You chose {player}\n {player_selection[player]}\n computer chose {computer}\n {player_selection[computer]}")
    if player == computer:
        return "Its a tie!"
    elif player=="rock":
     if computer=="scissors":
      return "Rock smashes scissors!You win!"
     else:
      return "paper cover rock!You lose!"
    elif player=="paper":
     if computer=="rock":
      return "paper cover rock!You win!"
     else:
      return "scissor cuts paper!you lose!"
    elif player=="scissors":
     if computer=="paper":
      return "scissor cuts paper!you win!"
     else:
      return "rock smashes scissor!you lose!"

Choices, player_selection = get_choices()
result = check_win(Choices["player"], Choices["computer"], player_selection)
print(result)