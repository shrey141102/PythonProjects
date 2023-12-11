from tkinter import *
from tkinter import messagebox
from tkinter.font import *
from tkinter import ttk
import random

x = 0
y = 0
z = 1

def reset():
    global border1, border2
    
    x = 0
    y = 0
    z = 1

    border1.config(text = "TIC TAC TOE")
    b1.config(text = " ", bg = 'lightsalmon')
    b2.config(text = " ", bg = 'lightsalmon')
    b3.config(text = " ", bg = 'lightsalmon')
    b4.config(text = " ", bg = 'lightsalmon')
    b5.config(text = " ", bg = 'lightsalmon')
    b6.config(text = " ", bg = 'lightsalmon')
    b7.config(text = " ", bg = 'lightsalmon')
    b8.config(text = " ", bg = 'lightsalmon')
    b9.config(text = " ", bg = 'lightsalmon')

    border2.config(text = 'TIC TAC TOE')
    a1.config(text = " ", bg = 'lightsalmon')
    a2.config(text = " ", bg = 'lightsalmon')
    a3.config(text = " ", bg = 'lightsalmon')
    a4.config(text = " ", bg = 'lightsalmon')
    a5.config(text = " ", bg = 'lightsalmon')
    a6.config(text = " ", bg = 'lightsalmon')
    a7.config(text = " ", bg = 'lightsalmon')
    a8.config(text = " ", bg = 'lightsalmon')
    a9.config(text = " ", bg = 'lightsalmon')


def newgame():
    main()
    main1.withdraw()
    main2.withdraw()


def one_player_intro():
    global chance1, intro1
    intro1 = Toplevel(root)
    intro1.title('Single Player')
    root.withdraw()

    border = LabelFrame(intro1, bg = 'tomato', text = "CHOOSE", font = ('agency FB', 40, 'bold'),labelanchor= N, borderwidth = 8, relief = RIDGE)
    border.pack(fill=BOTH, expand = True)

    x_btn = Button(border, bg = 'lightsalmon', text = "X", font = ('comic sans MS', 19, 'bold'), height = 2, width = 5, command = chosen_x).grid(row = 0, column = 0)
    Label(border, bg = 'tomato', text = 'or', font = ('agency FB', 17)).grid(row = 0, column = 1)
    o_btn = Button(border, bg = 'lightsalmon', text = "O", font = ('comic sans MS', 19, 'bold'), height = 2, width = 5, command = chosen_y).grid(row = 0, column = 2)

def chosen_x():
    global chosen
    chosen = chosen
    one_player()

def chosen_y():
    global chosen
    chosen = chosen + 1
    one_player()

def one_player():
    global intro1, b1, b2, b3, b4, b5, b6, b7, b8, b9, y, z, border1, main1
    main1 = Toplevel(intro1)
    main1.title('Single Player')
    intro1.withdraw()


    border1 = LabelFrame(main1, bg = 'tomato', text = "TIC TAC TOE", font = ('agency FB', 40, 'bold'),labelanchor= N, borderwidth = 8, relief = RIDGE, padx = 4, pady = 4)
    border1.pack(fill=BOTH, expand = True)

    b1 = Button(border1, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click1(b1))
    b2 = Button(border1, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click1(b2))
    b3 = Button(border1, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click1(b3))
    b4 = Button(border1, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click1(b4))
    b5 = Button(border1, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click1(b5))
    b6 = Button(border1, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click1(b6))
    b7 = Button(border1, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click1(b7))
    b8 = Button(border1, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click1(b8))
    b9 = Button(border1, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click1(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1, columnspan = 2)
    b3.grid(row=0, column=3)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1, columnspan = 2)
    b6.grid(row=1, column=3)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1, columnspan = 2)
    b9.grid(row=2, column=3)

    Button(border1, bg = 'firebrick', text = 'Reset', font = ('comic sans MS', 19, 'bold'), height = 1, width = 9, command = reset).grid(row = 3, column = 0, columnspan = 2, pady = 2)
    Button(border1, bg = 'firebrick', text = 'New Game', font = ('comic sans MS', 19, 'bold'), height = 1, width = 9, command = newgame).grid(row = 3, column = 2, columnspan = 2, pady = 2)

    if chosen%2 != 0:
        if z%2 != 0:
           computer_chance()
        else:
            return
    elif chosen%2 == 0:
        if y%2 != 0:
           computer_chance()
        else:
           return




def btn_click1(btn1):
    global chosen, y, z, p, q, r
    if chosen%2 == 0:
        if (btn1['text'] == " "):
            if y%2 == 0:
               btn1.config(text = "X")
               y = y+1
        if y%2 != 0:
            computer_chance()
    else:
        if (btn1['text'] == " "):
            if z%2 == 0:
               btn1.config(text = "O")
               z = z+1
        if z%2 != 0:
           computer_chance()

    if check_win(b1, b2, b3) == True or check_win(b4, b5, b6) == True or check_win(b7, b8, b9) == True or check_win(b1, b4, b7) == True or check_win(b2, b5, b8) == True or check_win(b3, b6, b9) == True or check_win(b1, b5, b9) == True or check_win(b3, b5, b7) == True:
        if chosen%2 == 0:
            if p1['text'] == q1['text'] == r1['text'] == 'X':
                border1.config(text = "YOU WIN")
            else:
                border1.config(text = "YOU LOSE")
        if chosen%2 != 0:
            if p1['text'] == q1['text'] == r1['text'] == 'O':
                border1.config(text = "YOU WIN")
            else:
                border1.config(text = "YOU LOSE")
    else:
        if b1['text'] != " " and b2['text'] != " " and b3['text'] != " " and b4['text'] != " " and b5['text'] != " " and b6['text'] != " " and b7['text'] != " " and b8['text'] != " " and b9['text'] != " " :
            border1.config(text = "IT'S A TIE")

def computer_chance():
    global chosen, y, z, b1, b2, b3, b4, b5, b6, b7, b8, b9
    y = y + 1
    z = z + 1

    first_choice = random.choice([b1, b3, b7, b9])
    next_choice = random.choice([b2, b4, b6, b8])

    if check_win != True:
        if check_almostwin(b1, b2, b3) == True :
            return
        elif check_almostwin(b4, b5, b6) == True:
            return
        elif check_almostwin(b7, b8, b9) == True:
            return
        elif check_almostwin(b1, b4, b7) == True:
            return
        elif check_almostwin(b2, b5, b8) == True:
            return
        elif check_almostwin(b3, b6, b9) == True:
            return
        elif check_almostwin(b1, b5, b9) == True:
            return
        elif check_almostwin(b3, b5, b7) == True:
            return

        if chosen%2 == 0:
            if b5['text'] == " ":
                b5.config(text = 'O')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'O')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'O')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'O')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'O')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'O')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'O')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'O')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'O')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'O')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'O')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'O')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'O')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'O')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'O')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'O')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'O')

        elif chosen%2 != 0:
            if first_choice['text'] == " ":
                first_choice.config(text = 'X')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'X')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'X')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'X')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'X')
            elif b5['text'] == " ":
                b5.config(text = 'X')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'X')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'X')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'X')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'X')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'X')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'X')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'X')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'X')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'X')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'X')
            elif next_choice['text'] == " ":
                next_choice.config(text = 'X')
            elif first_choice['text'] == " ":
                first_choice.config(text = 'X')
    else:
        return False

def check_almostwin(a, b, c):
    if chosen%2 == 0:
        if a['text'] == "O" and b['text'] == "O" and c['text'] == " ":
            c.config(text = "O")
            return True
        elif a['text'] == " " and b['text'] == "O" and c['text'] == "O":
            a.config(text = "O")
            return True
        elif a['text'] == "O" and b['text'] == " " and c['text'] == "O":
            b.config(text = "O")
            return True
        elif a['text'] == "X" and b['text'] == "X" and c['text'] == " ":
            c.config(text = "O")
            return True
        elif a['text'] == " " and b['text'] == "X" and c['text'] == "X":
            a.config(text = "O")
            return True
        elif a['text'] == "X" and b['text'] == " " and c['text'] == "X":
            b.config(text = "O")
            return True

    elif chosen%2 != 0:
        if a['text'] == "X" and b['text'] == "X" and c['text'] == " ":
            c.config(text = "X")
            return True
        elif a['text'] == " " and b['text'] == "X" and c['text'] == "X":
            a.config(text = "X")
            return True
        elif a['text'] == "X" and b['text'] == " " and c['text'] == "X":
            b.config(text = "X")
            return True
        elif a['text'] == "O" and b['text'] == "O" and c['text'] == " ":
            c.config(text = "X")
            return True
        elif a['text'] == " " and b['text'] == "O" and c['text'] == "O":
            a.config(text = "X")
            return True
        elif a['text'] == "O" and b['text'] == " " and c['text'] == "O":
            b.config(text = "X")
            return True                                                                                                                                                                                                                                                                                                                                                                                                         
    else:
        return False

def two_player():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, border2, main2
    main2 = Toplevel(root)
    main2.title('Multi Player')
    root.withdraw()
    
    border2 = LabelFrame(main2, bg = 'tomato', text = "TIC TAC TOE", font = ('agency FB', 40, 'bold'),labelanchor= N, borderwidth = 8, relief = RIDGE, padx = 2, pady = 2)
    border2.pack(fill=BOTH, expand = True)

    a1 = Button(border2, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click2(a1))
    a2 = Button(border2, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click2(a2))
    a3 = Button(border2, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click2(a3))
    a4 = Button(border2, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click2(a4))
    a5 = Button(border2, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click2(a5))
    a6 = Button(border2, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click2(a6))
    a7 = Button(border2, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click2(a7))
    a8 = Button(border2, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click2(a8))
    a9 = Button(border2, bg = 'lightsalmon', text = " ", font = ('comic sans MS', 19, 'bold'), height = 2, width = 6, command = lambda: btn_click2(a9))

    a1.grid(row=0, column=0)
    a2.grid(row=0, column=1, columnspan = 2)
    a3.grid(row=0, column=3)
    a4.grid(row=1, column=0)
    a5.grid(row=1, column=1, columnspan = 2)
    a6.grid(row=1, column=3)
    a7.grid(row=2, column=0)
    a8.grid(row=2, column=1, columnspan = 2)
    a9.grid(row=2, column=3)

    Button(border2, bg = 'firebrick', text = 'Reset', font = ('comic sans MS', 19, 'bold'), height = 1, width = 9, command = reset).grid(row = 3, column = 0, columnspan = 2, pady = 2)
    Button(border2, bg = 'firebrick', text = 'New Game', font = ('comic sans MS', 19, 'bold'), height = 1, width = 9, command = newgame).grid(row = 3, column = 2, columnspan = 2, pady = 2)


def btn_click2(btn2):
    global a1, x, chosen, a2, a3, a4, a5, a6, a7, a8, a9, border2, b1, b2
    if (btn2['text'] == " "):
        if x%2 == 0:
            btn2.config(text = "X")
            x = x+1
        else:
            btn2.config(text = "O")
            x = x+1
    else:
        return

    if check_win(a1, a2, a3) == True or check_win(a4, a5, a6) == True or check_win(a7, a8, a9) == True or check_win(a1, a4, a7) == True or check_win(a2, a5, a8) == True or check_win(a3, a6, a9) == True or check_win(a1, a5, a9) == True or check_win(a3, a5, a7) == True:
        if chosen%2 == 0:
            if p1['text'] == q1['text'] == r1['text'] == 'X':
                border2.config(text = "PLAYER X WINS")
            else:
                border2.config(text = "PLAYER O WINS")
        if chosen%2 != 0:
            if p1['text'] == q1['text'] == r1['text'] == 'O':
                border2.config(text = "PLAYER O WINS")
            else:
                border2.config(text = "PLAYER X WINS")
    else:
        if b1['text'] != " " and b2['text'] != " " and b3['text'] != " " and b4['text'] != " " and b5['text'] != " " and b6['text'] != " " and b7['text'] != " " and b8['text'] != " " and b9['text'] != " " :
            border2.config(text = "IT'S A TIE")


def check_win(p, q, r):
    global p1, q1, r1
    p1 = p
    q1 = q
    r1 = r
    if p['text'] == q['text'] == r['text'] != " ":
        p.config(bg = 'brown')
        q.config(bg = 'brown')
        r.config(bg = 'brown')
        return True
    else:
        return False



def main():
    global root
    root = Tk()
    root.geometry('300x250')
    root.title('Tic Tac Toe')

    frame1 = LabelFrame(root, bg = 'tomato', text = "TIC TAC TOE", font = ('agency FB', 40, 'bold'),labelanchor= N, borderwidth = 8, relief = RIDGE)
    frame1.pack(fill=BOTH, expand = True)

    single_player = Button(frame1, text = "Single Player", background = 'lightsalmon', font = ('comic sans MS', 20), command = one_player_intro)
    single_player.pack(padx = 3, pady = 8)

    multi_player = Button(frame1, text = "Multi Player", background = 'lightsalmon', font = ('comic sans MS', 20), padx = 7, command = two_player)
    multi_player.pack(padx = 3, pady = 3)

if y%2 != 0:
    if check_win == False:
        computer_chance()


main()
chance1 = StringVar()
chosen = 0

root.mainloop()
