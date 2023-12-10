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
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
n = int(input())
r = random.randint(0,2)
if n>2: print("Invalid input")
c = "y"


while c == "y" or c=="Y":
    print(f'\nYou chose : \n {l[n]}\n')
    print(f'Computer chose : \n {l[r]}\n')
    if n == r:
      print(" It's a Draw!! ")
    elif n==0:
      if r == 1:
        print("You lose! :( ")
      if r == 2:
        print("You win! :) ")

    elif n==1:
      if r == 2:
        print("You lose! :( ")
      if r == 0:
        print("You win! :) ")

    else:
      if r == 0:
        print("You lose! :(")
      if r == 1:
        print("You win! :)")

    print("\nDo you want to continue? Press y for continue else press n to discontinue: ")
    c = (input())
    if(c!="y" and c!="Y"): break
    print("Enter your choice again! Type 0 for Rock, 1 for Paper or 2 for Scissors")
    n = int(input())
    r = random.randint(0,2)

print("\nHope you enjoyed playing ;)\n")

