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

l = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
n = int(input())
r = random.randint(0,2)
if n>2: print("invalid")


print(f' you chose \n {l[n]}')
print(f'computer chose \n {l[r]}')
if n == r:
  print("Draw")
elif n==0:
  if r == 1:
    print("You lose")
  if r == 2:
    print("You win")

elif n==1:
  if r == 2:
    print("You lose")
  if r == 0:
    print("You win")

else:
  if r == 0:
    print("You lose :(")
  if r == 1:
    print("You win :)")