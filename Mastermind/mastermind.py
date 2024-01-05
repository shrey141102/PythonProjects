from random import *

def choose_mode():
    code_create()
    global mode
    mode = input("Choose mode(Hard or Easy): ").upper()

    while mode != "HARD" and mode != "EASY":
        print("INVALID INPUT.")
        mode = input("Choose your mode: Hard or Easy. ").upper()

    if mode == "HARD":
        print(k(1) + k(3) + """

Object of the Game:

The object of MASTERMIND is to guess a secret code consisting of a series of 5 colored
boxes, Which is decided by the computer. Each guess results in feedback, in the form of a
series of five coloured circles (each either red or white), narrowing down the possibilities 
of the code. To Win you have to guess the secret code within a fixed number of guesses.

Instructions (For Hard Mode):

1.  The Colours are as Follows:""" + k(0) + """
    🟥 = Red
    🟦 = Blue
    🟧 = Orange
    🟨 = Yellow
    🟩 = Green
    🟪 = Purple or Violet
    ⬛ = Black
    ⬜ = White""" + k(1) + k(3) + """

2.  A Five digit code is created by the computer. This may contain any of the 8 colours and the
    colours may be repeated. Some Example Codes are -""" + k(0) + code[0] + code[1] + code[2] + code[3] + code [4] + k(0),end = " , ") 

        code_create()

        print(code[0] + code[1] + code[2] + code[3] + code [4] + k(1) + k(3) + """ etc.

3.  The player will now attempt to guess the secret code by answering certain questions in the following
    format- What shall be put in postion 1?, What shall be put in position 2?, etc. These positons are 
    correspond to the grid in the following format- 
    ╔════╦════╦════╦════╦════╗
    ║ P1 ║ P2 ║ P3 ║ P4 ║ P5 ║
    ╚════╩════╩════╩════╩════╝

4.  The Computer will place coloured circles in the second grid-
    The red circle,""" + k(0) + """🔴""" + k(1) + k(3) + """, refers to one square which is in the correct position and is also the correct colour.
    The white circle,""" + k(0) + """⚪""" + k(1) + k(3) + """,  refers to one square which is the correct colour but is not in the correct position.
    These circles are put in a fixed order in which first all the red circles are put and after that the white ones.

5. The player has 8 guesses and if he/she doesn't guess the code in these 8 guesses, they lose. 
    
""" + k(0))
    elif mode == "EASY":
        print(k(1) + k(3) + """

Object of the Game:

The object of MASTERMIND is to guess a secret code consisting of a series of 5 colored
boxes, Which is decided by the computer. Each guess results in feedback, in the form of a
series of five coloured circles (each either red or white), narrowing down the possibilities 
of the code. To Win you have to guess the secret code within a fixed number of guesses.

Instructions (For Easy Mode):

1.  The Colours are as Follows:""" + k(0) + """
    🟥 = Red
    🟦 = Blue
    🟧 = Orange
    🟨 = Yellow
    🟩 = Green
    🟪 = Purple or Violet
    ⬛ = Black
    ⬜ = White""" + k(1) + k(3) + """

2.  A Five digit code is created by the computer. This may contain any of the 8 colours and the
    colours may be repeated. Some Example Codes are -""" + k(0) +code[0] + code[1] + code[2] + code[3] + code [4] + k(0),end = " , ") 

        code_create()

        print(code[0] + code[1] + code[2] + code[3] + code [4] + k(1) + k(3) + """ etc.


3.  The player will now attempt to guess the secret code by answering certain questions in the following
    format- What shall be put in postion 1?, What shall be put in position 2?, etc. These positons are 
    correspond to the grid in the following format- 
    ╔════╦════╦════╦════╦════╗
    ║ P1 ║ P2 ║ P3 ║ P4 ║ P5 ║
    ╚════╩════╩════╩════╩════╝

4.  The Computer will place coloured circles in the second grid-
    The red circle,""" + k(0) + """🔴""" + k(1) + k(3) + """ , refers to one square which is in the correct position and is also the correct colour.
    The white circle,""" + k(0) + """⚪""" + k(1) + k(3) + """ , refers to one square which is the correct colour but is not in the correct position.
    These circles are put in an order which corresponds to the sqaures you have put.

5. The player has 12 guesses and if he/she doesn't guess the code in these 12 guesses, they lose. 
    
""" + k(0))

def create_grid_hard():
    print("   ╔════╦════╦════╦════╦════╗  ┏━━┳━━┳━━┳━━┳━━┓")
    for i in range(8):
        #if i>2:    
        print(8-i, " ║", end = "")
        #elif i<=8:
        #    print(12-i, "║", end = "")
        for j in range(5):
            print("", guess_list[i][j], "║", end = "")
        print("  ┃", end = "")
        for x in range(5):
            print(check_list[i][x], "┃" , end = "", sep = "")
        print("")
        if i <=6:
            print("   ╠════╬════╬════╬════╬════╣  ┣━━╋━━╋━━╋━━╋━━┫")
        else:
            print("   ╚════╩════╩════╩════╩════╝  ┗━━┻━━┻━━┻━━┻━━┛")
        i += 1

def check_hard(row):
    global checked_red
    checked = []
    checked_red = []
    count_r = 0
    count_w = 0
    for i in range(5):
        if guess_list[row][i] == code[i]:
            count_r += 1
            #check_list[row][i] = pin[0]
            checked.append(guess_list[row][i])
            checked_red.append(guess_list[row][i])

    for i in range(5):
        if check_list[row][i] == "  ":
            if guess_list[row][i] in code:
                if checked.count(guess_list[row][i]) < code.count(guess_list[row][i]):
                    if guess_list[row].count(guess_list[row][i]) > checked_red.count(guess_list[row][i]):
                        count_w += 1
                        #check_list[row][i] = pin[1]
                        checked.append(guess_list[row][i])
    for i in range(count_r):
        check_list[row][i] = pin[0]
    for i in range(count_w):
        check_list[row][count_r + i] = pin[1]

def code_create():
    global code
    code = []
    for i in range(5):
        code.append(choice(colour))

def colour_change(row, col):
    if guess_list[row][col].upper() == "RED":
        guess_list[row][col] = colour[0]
        return True
    elif guess_list[row][col].upper() == "BLUE":
        guess_list[row][col] = colour[1]
        return True
    elif guess_list[row][col].upper() == "ORANGE":
        guess_list[row][col] = colour[2]
        return True
    elif guess_list[row][col].upper() == "YELLOW":
        guess_list[row][col] = colour[3]
        return True
    elif guess_list[row][col].upper() == "GREEN":
        guess_list[row][col] = colour[4]
        return True
    elif guess_list[row][col].upper() == "VIOLET" or guess_list[row][col] == "PURPLE":
        guess_list[row][col] = colour[5]
        return True
    elif guess_list[row][col].upper() == "BLACK":
        guess_list[row][col] = colour[6]
        return True
    elif guess_list[row][col].upper() == "WHITE":
        guess_list[row][col] = colour[7]
        return True
    else:
        print("INVALID INPUT.")
        return False

def create_grid():
    print("   ╔════╦════╦════╦════╦════╗  ┏━━┳━━┳━━┳━━┳━━┓")
    for i in range(12):
        if i>2:    
            print(12-i, " ║", end = "")
        elif i<=8:
            print(12-i, "║", end = "")
        for j in range(5):
            print("", guess_list[i][j], "║", end = "")
        print("  ┃", end = "")
        for x in range(5):
            print(check_list[i][x], "┃" , end = "", sep = "")
        print("")
        if i <=10:
            print("   ╠════╬════╬════╬════╬════╣  ┣━━╋━━╋━━╋━━╋━━┫")
        else:
            print("   ╚════╩════╩════╩════╩════╝  ┗━━┻━━┻━━┻━━┻━━┛")
        i += 1

def check(row):
    global checked_red
    checked = []
    checked_red = []
    for i in range(5):
        if guess_list[row][i] == code[i]:
            check_list[row][i] = pin[0]
            checked.append(guess_list[row][i])
            checked_red.append(guess_list[row][i])

    for i in range(5):
        if check_list[row][i] == "  ":
            if guess_list[row][i] in code:
                if checked.count(guess_list[row][i]) < code.count(guess_list[row][i]):
                    if guess_list[row].count(guess_list[row][i]) > checked_red.count(guess_list[row][i]):
                        check_list[row][i] = pin[1]
                        checked.append(guess_list[row][i])

def main():
    global guess_list, check_list
    guess_list = []
    check_list = []

    for i in range(12):
        guess_list.append(["  ", "  ", "  ", "  ", "  "])
        check_list.append(["  ", "  ", "  ", "  ", "  "])

    choose_mode()
    code_create()
    if mode == "HARD":
        for x in range(7,-1,-1):
            create_grid_hard()
            for y in range(5):
                guess_list[x][y] = input(k(1) + k(3) + "Which colour shall be put in postion " + str(y+1) + "? " + k(0)).upper()
                t = colour_change(x, y)
                while t == False:
                        guess_list[x][y] = input(k(1) + k(3) + "Which colour shall be put in postion " + str(y+1) + "? " + k(0)).upper()
                        t = colour_change(x, y)
            check_hard(x)
            if checked_red == guess_list[x]:
                create_grid_hard()
                play = input(k(1) + k(3) + k(4) + k(32) + "Congratulations! You Won!!" + k(0) + k(1) + k(3) + "\nDo you wanna play again?? [Y/N]" + k(0)).upper()
                while play != "Y" and play != "N":
                    print("INVALID INPUT.")
                    play = input(k(1) + k(3) + "Do you wanna play again?? [Y/N]" + k(0)).upper()
                if play == "Y":
                    guess_list = []
                    check_list = []

                    for i in range(12):
                        guess_list.append(["  ", "  ", "  ", "  ", "  "])
                        check_list.append(["  ", "  ", "  ", "  ", "  "])

                    main()
                elif play == "N":
                    print(k(1) + k(3) + k(4) + "Thank You For Playing Our Game! Have a good day!" + k(0))
                    break
                
        else:
            create_grid_hard()
            play = input(k(1) + k(3) + k(4) + k(31) + "You Lost... The code was " + k(0) +code[0] + code[1] + code[2] + code[3] + code [4] + k(0) + k(1) + k(3) + "\nDo you wanna play again?? [Y/N]" + k(0)).upper()
            while play != "Y" and play != "N":
                print("INVALID INPUT.")
                play = input(k(1) + k(3) + "Do you wanna play again?? [Y/N]" + k(0)).upper()
            if play == "Y":
                guess_list = []
                check_list = []

                for i in range(12):
                    guess_list.append(["  ", "  ", "  ", "  ", "  "])
                    check_list.append(["  ", "  ", "  ", "  ", "  "])

                main()
            elif play == "N":
                print(k(1) + k(3) + k(4) + "Thank You For Playing Our Game! Have a good day!" + k(0))
            
    elif mode == "EASY":
        for x in range(11,-1,-1):
            create_grid()
            for y in range(5):
                guess_list[x][y] = input(k(1) + k(3) + "Which colour shall be put in postion " + str(y+1) + "? " + k(0)).upper()
                t = colour_change(x, y)
                while t == False:
                        guess_list[x][y] = input(k(1) + k(3) + "Which colour shall be put in postion " + str(y+1) + "? " + k(0)).upper()
                        t = colour_change(x, y)
            check(x)
            if checked_red ==guess_list[x]:
                create_grid()
                play = input(k(1) + k(3) + k(4) + k(32) + "Congratulations! You Won!!" + k(0) + k(1) + k(3) + "\nDo you wanna play again?? [Y/N]" + k(0)).upper()
                while play != "Y" and play != "N":
                    print("INVALID INPUT.")
                    play = input(k(1) + k(3) + "Do you wanna play again?? [Y/N]" + k(0)).upper()
                if play == "Y":
                    guess_list = []
                    check_list = []

                    for i in range(12):
                        guess_list.append(["  ", "  ", "  ", "  ", "  "])
                        check_list.append(["  ", "  ", "  ", "  ", "  "])

                    main()
                elif play == "N":
                    print(k(1) + k(3) + k(4) + k(34) + "Thank You For Playing Our Game! Have a good day!" + k(0))
                    break
            
        else:
            create_grid()
            play = input(k(1) + k(3) + k(4) + k(31) + "You Lost... The code was " + k(0) +code[0] + code[1] + code[2] + code[3] + code [4] + k(1) + k(3) + "\nDo you wanna play again?? [Y/N]" + k(0)).upper()
            while play != "Y" and play != "N":
                print("INVALID INPUT.")
                play = input(k(1) + k(3) + "Do you wanna play again?? [Y/N]" + k(0)).upper()
            if play == "Y":
                guess_list = []
                check_list = []

                for i in range(12):
                    guess_list.append(["  ", "  ", "  ", "  ", "  "])
                    check_list.append(["  ", "  ", "  ", "  ", "  "])
                    
                main()
            elif play == "N":
                print(k(1) + k(3) + k(4) + k(34) + "Thank You For Playing Our Game! Have a good day!" + k(0))

def k(n):
    return ("\033[" + str(n) + "m")

print(k(1) + k(3) + k(34) + """
           ┏━━━━━━━━━━━━┓
           ┃ MASTERMIND ┃
           ┗━━━━━━━━━━━━┛
""" + k(0))


colour = ["🟥","🟦","🟧","🟨","🟩","🟪","⬛","⬜" ]
pin = ["🔴","⚪"]

main()
