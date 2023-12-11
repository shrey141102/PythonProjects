from random import *
from tkinter import *
from tkinter.font import *
from tkinter import messagebox
import sys

def home(root):
    global main
    
    if root == 'a':
         main = Tk()
    else:
        main = Toplevel(root)
        root.withdraw()

    game = False

    main.title('MINESWEEPER')

    main_labelframe = LabelFrame(main, text = "MINESWEEPER", font = ('agency FB', 40, 'bold'),labelanchor= N, borderwidth = 8, relief = RIDGE, bg = 'turquoise3', pady = 20)
    main_labelframe.pack()

    label = Label(main_labelframe, text = "Choose a mode:", font = ('comic sans ms',22, 'bold'), bg = 'Turquoise4', borderwidth = 3, relief = RIDGE).pack(pady = 8)

    button1 = Button(main_labelframe, text = "CLASSIC", bg = 'PaleTurquoise1', font = ('agency FB',25, 'bold'), padx = 44, relief = RAISED, command = lambda: how_to_play(main, 1, 'b')).pack()
    button2 = Button(main_labelframe, text = "DETONATION", bg = 'PaleTurquoise1', font = ('agency FB',25, 'bold'), padx = 23, relief = RAISED, command = lambda: how_to_play(main, 2, 'b')).pack()
    button3 = Button(main_labelframe, text = "TREASURE HUNT", bg = 'PaleTurquoise1', font = ('agency FB',25, 'bold'), relief = RAISED, command = lambda: how_to_play(main, 3, 'b')).pack()

    create_menubar(main)

def create_menubar(root):
    global helpmenu 

    menubar = Menu(root, tearoff = 0)

    newgame = Menu(menubar, tearoff = 0, bg = 'Turquoise4', fg = 'white', font = Font(size = 10, weight = 'bold'))

    classicmenu = Menu(newgame, tearoff = 0, bg = 'Turquoise4', fg = 'white', font = Font(size = 10, weight = 'bold'))
    classicmenu.add_command(label = "Beginner", command = lambda: menubar_function("CLASSIC MODE", "B", root))
    classicmenu.add_command(label = "Intermediate", command = lambda: menubar_function("CLASSIC MODE", "I", root))
    classicmenu.add_command(label = "Advanced", command = lambda: menubar_function("CLASSIC MODE", "A", root))

    detonationmenu = Menu(newgame, tearoff = 0, bg = 'Turquoise4', fg = 'white', font = Font(size = 10, weight = 'bold'))
    detonationmenu.add_command(label = "Beginner", command = lambda: menubar_function("DETONATION", "B", root))
    detonationmenu.add_command(label = "Intermediate", command = lambda: menubar_function("DETONATION", "I", root))
    detonationmenu.add_command(label = "Advanced", command = lambda: menubar_function("DETONATION", "A", root))

    treasuremenu = Menu(newgame, tearoff = 0, bg = 'Turquoise4', fg = 'white', font = Font(size = 10, weight = 'bold'))
    treasuremenu.add_command(label = "Beginner", command = lambda: menubar_function("TREASURE HUNT", "B", root))
    treasuremenu.add_command(label = "Intermediate", command = lambda: menubar_function("TREASURE HUNT", "I", root))
    treasuremenu.add_command(label = "Advanced", command = lambda: menubar_function("TREASURE HUNT", "A", root))

    newgame.add_cascade(label = "Classic Mode", menu = classicmenu)
    newgame.add_cascade(label = "Detonation", menu = detonationmenu)
    newgame.add_cascade(label = "Treasure Hunt", menu = treasuremenu)
    newgame.add_separator()
    newgame.add_command(label = "Exit", command = sys.exit)

    helpmenu = Menu(menubar, tearoff = 0, bg = "Turquoise4", fg = 'white', font = Font(size = 10, weight = 'bold'))

    howtoplay_menu = Menu(helpmenu, tearoff = 0, bg = 'Turquoise4', fg = 'white', font = Font(size = 10, weight = 'bold'))
    howtoplay_menu.add_command(label = 'Classic Mode', command = lambda: how_to_play(root, 1, 'a'))
    howtoplay_menu.add_command(label = 'Detonation', command = lambda: how_to_play(root, 2, 'a'))
    howtoplay_menu.add_command(label = 'Treasure Hunt', command = lambda: how_to_play(root, 3, 'a'))

    helpmenu.add_cascade(label = "How to play", menu = howtoplay_menu)

    menubar.add_cascade(label = "New Game", menu = newgame)
    menubar.add_cascade(label = "Help", menu = helpmenu)

    root.config(menu = menubar)

def menubar_function(mode_, level_, root_):
    global mode, level_window

    mode = mode_
    level_window = Toplevel(root_)
    root_.withdraw()
    start_game(level_)

def create_board(list1):
    for i in range(row):
        list1.append([])
        for j in range(col):
            list1[i].append(' ')

def display_board(list1, frame):
    buttons = []
    for a in change_list:
        i,j = a[0],a[1]
    
        if list1[i][j] == '✹':
            buttons.append(Button(frame, text = list1[i][j], bg = 'firebrick2', font = Font(size = 13), width = 1, height = 0, padx = 7, pady = 0, relief = SUNKEN).grid(row = i, column = j))
        
        elif list1[i][j] == ' ':
            btn = Button(frame, text = list1[i][j], bg = 'Turquoise4', font = Font(size = 10), width = 3, height = 1, padx = 0, pady = 3, relief = RAISED)
            btn.grid(row = i, column = j)

            if mode == "CLASSIC MODE":
                btn.bind('<Button-1>', lambda event, x = i, y = j: classic(event,x,y))
                btn.bind('<Button-3>', lambda event, x = i, y = j: board_click_right(event,x,y))
            elif mode == "TREASURE HUNT":
                btn.bind('<Button-1>', lambda event, x = i, y = j: treasure(event,x,y))
                btn.bind('<Button-3>', lambda event, x = i, y = j: board_click_right(event,x,y))
            else:
                btn.bind('<Button-1>', lambda event, x = i, y = j: detonation(event,x,y))

        elif list1[i][j] == '0':
            buttons.append(Button(frame, text = ' ', bg = 'PaleTurquoise1', font = Font(size = 13), width = 1, height = 0, padx = 7, pady = 0, relief = SUNKEN).grid(row = i, column = j))
        
        elif list1[i][j] == 'F':
            btn = Button(frame, text = '🚩', bg = 'DarkGoldenRod1', fg = 'firebrick2', font = Font(size = 13), width = 1, height = 0, padx = 7, pady = 0, relief = SUNKEN)
            btn.grid(row = i, column = j)
            btn.bind('<Button-3>', lambda event, x = i, y = j: board_click_right(event,x,y))
        
        elif list1[i][j] == 'T':
            buttons.append(Button(frame, text = '💎', bg = 'green', font = Font(size = 13, weight = 'bold'), width = 1, height = 0, padx = 7, pady = 0, relief = SUNKEN).grid(row = i, column = j))
        
        else:
            buttons.append(Button(frame, text = list1[i][j], bg = 'PaleTurquoise1', fg = num_colours[int(list1[i][j])], font = Font(size = 13), width = 1, height = 0, padx = 7, pady = 0, relief = SUNKEN).grid(row = i, column = j))

def reset_change_list():
    global change_list

    change_list = []
    for i in range(row):
        for j in range(col):
            change_list.append([i,j])

def choose_level(n):
    global mode, level_window, help_window

    level_window = Toplevel(help_window)
    level_window.title("MINESWEEPER")
    help_window.withdraw()
    
    create_menubar(level_window)
    mode = n

    level_frame = LabelFrame(level_window, text = mode, font = ('agency FB', 40, 'bold'),labelanchor= N, borderwidth = 8, relief = RIDGE, bg = 'turquoise3', pady = 20)
    level_frame.pack()

    level_lbl = Label(level_frame, text = "Choose a level:", font = ('comic sans ms',22, 'bold'), bg = 'Turquoise4', borderwidth = 3, relief = RIDGE)
    level_lbl.pack(pady = 8, padx = 5)

    cl_button1 = Button(level_frame, text = "BEGINNER", bg = 'PaleTurquoise1', font = ('agency FB',25, 'bold'), padx = 23, relief = RAISED, command = lambda: start_game('B')).pack()
    cl_button2 = Button(level_frame, text = "INTERMEDIATE", bg = 'PaleTurquoise1', font = ('agency FB',25, 'bold'), relief = RAISED, command = lambda: start_game('I')).pack()
    cl_button3 = Button(level_frame, text = "ADVANCED", bg = 'PaleTurquoise1', font = ('agency FB',25, 'bold'), padx = 21, relief = RAISED, command = lambda: start_game('A')).pack()

def start_game(a):
    global row, col, num_bombs, num_hints, bombs_left, num_moves, c, num_lives, game_frame, result_label, moves_label, lives_label, dug, board, hidden_board, change_list, game_window

    dug = set()

    if a == 'B':   
        row, col, num_bombs, bombs_left, num_moves, c = 10, 10, 14, 14, 18, 14
    elif a == 'I':
        row, col, num_bombs, bombs_left, num_moves, c = 14, 18, 40, 40, 45, 18
    elif a == 'A':
        row, col, num_bombs, bombs_left, num_moves, c = 14, 32, 99, 99, 102, 25

    num_lives = 3
    num_hints = 3

    if 'game_window' in globals():
        game_window.withdraw()

    game_window = Toplevel(level_window)
    game_window.title("MINESWEEPER")
    game_window.configure(bg = "Turquoise3")
    

    level_window.withdraw()

    create_menubar(game_window)
    helpmenu.add_command(label = 'Hint        H', command = give_hint)

    game_frame = LabelFrame(game_window, text = mode, font = ('agency FB', 40, 'bold'),labelanchor= N, borderwidth = 8, relief = RIDGE, bg = 'turquoise3')
    game_frame.pack()

    result_label = Label(game_frame, text = f"Mines: {bombs_left}", font = ('comic sans MS', 20, 'bold'), bg = 'Turquoise4', relief = RIDGE)
    moves_label = Label(game_frame, text = f"Moves: {num_moves}", font = ('comic sans MS', 20, 'bold'), bg = 'Turquoise4', relief = RIDGE)
    lives_label = Label(game_frame, text = f"Lives: {num_lives}", font = ('comic sans MS', 20, 'bold'), bg = 'Turquoise4', relief = RIDGE)
    
    home_btn = Button(game_frame, text = "Home", font = ('agency FB', 20, 'bold'), bg = 'Turquoise4', relief = RAISED, command = home)
    retry_btn = Button(game_frame, text = "Retry", font = ('agency FB', 20, 'bold'), bg = 'Turquoise4', relief = RAISED, command = lambda: start_game(a))
    quit_btn = Button(game_frame, text = "Quit", font = ('agency FB', 20, 'bold'), bg = 'Turquoise4', relief = RAISED, command = sys.exit)

    game_window.bind('<h>', lambda x: give_hint())

    board = []
    create_board(board)

    hidden_board = []
    create_board(hidden_board)
    insert_bombs_treasure() if mode == "TREASURE HUNT" else insert_bombs_classic()
    insert_numbers()

    reset_change_list()
    display_board(board, game_frame)

    if mode == "CLASSIC MODE":
        result_label.grid(row = row+1, column = 0, columnspan = col, sticky = 'ew')
    elif mode == "DETONATION":
        result_label.grid(row = row+1, column = 0, columnspan = col//2, sticky = 'ew')
        moves_label.grid(row = row+1, column = col//2, columnspan = col//2, sticky = 'ew')
    else:
        result_label.grid(row = row+1, column = 0, columnspan = col//2, sticky = 'ew')
        lives_label.grid(row = row+1, column = col//2, columnspan = col//2, sticky = 'ew')

    home_btn.grid(row = row+2, column = 0, columnspan = col//3, sticky = 'ew', pady = 5)
    retry_btn.grid(row = row+2, column = col//3, columnspan = (col//3) + 1, sticky = 'ew', pady = 5)
    quit_btn.grid(row = row+2, column = 2*col//3 + 1, columnspan = col//3, sticky = 'ew', pady = 5)
    if a == "I":
        retry_btn.grid(row = row+2, column = (col//3), columnspan = col//3, sticky = 'ew', pady = 5)
        quit_btn.grid(row = row+2, column = 2*col//3, columnspan = col//3, sticky = 'ew', pady = 5)
    elif a == "A":
        quit_btn.grid(row = row+2, column = 2*col//3, columnspan = (col//3) + 1, sticky = 'ew', pady = 5)

    game_window.mainloop()
   
def classic(event, a,b):
    global change_list 

    change_list = []
    if dig(a,b) == False:
        result_label.config(text = "You lose:(")
        reset_change_list()
        display_board(hidden_board, game_frame)
    else:
        display_board(board,game_frame)
  
    if len(dug) == row*col - num_bombs and bombs_left == 0:
        result_label.config(text = "Congrats! You win!!")
        reset_change_list()
        display_board(board, game_frame)

def detonation(event, a,b):
    global num_moves, change_list

    change_list = []
    dig_detonation(a,b)
    result_label.config(text = f"Mines: {bombs_left}")

    if bombs_left == 0:
        moves_label.destroy()
        result_label.config(text = "Congrats! You win!!")
        result_label.grid(row = row+1, column = 0, columnspan = col, sticky = 'ew')
        display_board(hidden_board, game_frame)

    elif num_moves < bombs_left:
        moves_label.destroy()
        result_label.config(text = 'Sorry! You ran out of moves :(')
        result_label.grid(row = row+1, column = 0, columnspan = col, sticky = 'ew')
        display_board(hidden_board, game_frame)

    else:
        num_moves -= 1
        moves_label.config(text = f"Moves: {num_moves}")
        display_board(board, game_frame)
        if num_moves < bombs_left:
            moves_label.destroy()
            result_label.config(text = 'Sorry! You ran out of moves :(')
            result_label.grid(row = row+1, column = 0, columnspan = col, sticky = 'ew')
            
def treasure(event, a,b):
    global num_lives, bombs_left, lives_label, change_list

    if hidden_board[a][b] == 'T':
        lives_label.destroy()
        result_label.config(text = "Congrats! You win!!")
        result_label.grid(row = row+1, column = 0, columnspan = col, sticky = 'ew')
        reset_change_list()
        display_board(hidden_board, game_frame)

    change_list = []
    if dig(a,b) == False:
        num_lives -= 1
        bombs_left -= 1
        if num_lives < 0:
            lives_label.destroy()
            result_label.config(text = "You lose:(")
            result_label.grid(row = row+1, column = 0, columnspan = col, sticky = 'ew')
            reset_change_list()
            display_board(hidden_board, game_frame)
        else:
            lives_label.config(text = f"Lives: {num_lives}")
            board[a][b] == hidden_board[a][b]
            display_board(board,game_frame)
    else:
        display_board(board,game_frame)

def insert_bombs_classic():
    i = 0
    while i<num_bombs:
        x1,y1 = randint(0,row-1), randint(0,col-1)
        if hidden_board[x1][y1] == '✹':
            continue
        hidden_board[x1][y1] = '✹'
        i += 1

def insert_numbers():
    for i in range(row):
        for j in range(col):
            if hidden_board[i][j] == '✹' or hidden_board[i][j] == 'T':
                continue
            c = 0
            for a in range(max(0,i-1), min(i+1, row-1) + 1):
                for b in range(max(0,j-1), min(j+1, col-1) + 1):
                    if a == i and b == j:
                        continue
                    if hidden_board[a][b] == '✹':
                        c+=1
            hidden_board[i][j] = str(c)

def insert_bombs_treasure():
    global xt, yt

    xt = randint(1,row-2)
    yt = randint(1,col-2)
    hidden_board[xt][yt] = 'T'
    for i in range(xt-1,xt+2):
        for j in range(yt-1,yt+2):
            if i == xt and j == yt:
                continue
            hidden_board[i][j] = '✹'
    i = 8
    while i<num_bombs:
        x1,y1 = randint(0,row-1), randint(0,col-1)
        if hidden_board[x1][y1] == '✹' or (x1 == xt and y1 == yt):
            continue
        hidden_board[x1][y1] = '✹'
        i += 1

def dig(a,b):
    global bombs_left, result_label, change_list

    change_list.append([a,b])

    dug.add((a,b))
    if board[a][b] == 'F':
        bombs_left += 1
        result_label.config(text = f"Mines left: {bombs_left}")
        
    board[a][b] = hidden_board[a][b]
    
    if hidden_board[a][b] == '✹':
        return False

    elif hidden_board[a][b] != '0':
        return 
    else:
        for i in range(max(0,a-1), min(a+1, row-1) + 1):
            for j in range(max(0,b-1), min(b+1, col-1) + 1):
                if i == a and j == b:
                    continue
                if (i,j) in dug:
                    continue
                dig(i,j)

def dig_detonation(a,b):
    global bombs_left

    change_list.append([a,b])

    if hidden_board[a][b] == '✹':
        board[a][b] = hidden_board[a][b]
        bombs_left -= 1
        l1 = []
        for i1 in range(max(0,a-1), min(a+1, row-1) + 1):
            for j1 in range(max(0,b-1), min(b+1, col-1) + 1):
                if (i1 == a and j1 == b) or (i1,j1) in dug or hidden_board[i1][j1] == '✹':
                    continue
                dig(i1,j1)
                l1.append([i1,j1])
        for i in l1:
            for i2 in range(max(0,i[0]-1), min(i[0]+1, row-1) + 1):
                for j2 in range(max(0,i[1]-1), min(i[1]+1, col-1) + 1):
                    if hidden_board[i2][j2] == '0' and board[i2][j2] == ' ':
                        dig(i2,j2)
    else:
        dig(a,b)

def board_click_right(event,a,b):
    global bombs_left, change_list

    change_list = [[a,b]]
    if board[a][b] == 'F':
        board[a][b] = ' '
        bombs_left += 1
    else:
        if bombs_left == 0:
            return
        else:
            board[a][b] = 'F'
            bombs_left -= 1

    display_board(board,game_frame)
    result_label.config(text = f"Mines: {bombs_left}")

def give_hint():
    global change_list, num_hints

    if num_hints == 0:
        messagebox.showwarning("MINESWEEPER", "Sorry, no more hints left. You are on your own now.")
    else:
        num_hints -= 1
        change_list = []

        while True:
            x = randint(0,row-1)
            y = randint(0,col-1)
            if hidden_board[x][y] == '✹' or hidden_board[x][y] == 'T':
                continue
            elif board[x][y] != ' ':
                continue
            break
        dig(x,y)
        display_board(board, game_frame)

def how_to_play(root, n, x):
    global help_window

    help_window = Toplevel(root)
    help_window.title("HOW TO PLAY")

    if n == 1:
        mode1 = "CLASSIC MODE"
        title = 'Welcome to Classic Mode!!'
        rules = ('''
1. Pick a level [Beginner/Intermediate/Advanced].
2. On your turn the board will be displayed, empty at first with mines hidden in it.
3. Click on the location you want to dig.
4. Digging will help you check if a mine is present at a particular location.
5. Boxes will recursively be dug starting from selected position until we reach a dug box adjacent to a mine.
6. Numbers on the boxes refer to the number of mines in neighbouring positions.
7. Empty dug box means there are no mines in neighbouring boxes.
8. Press 'H' for a hint [Maximum 3 hints], or select hint through 'Help' menu.
9. Right click on a box to place a flag at potential mine location.
10. At every turn, number of mines left will be displayed, decreasing as you place more flags
11. If you dig at a mine position, you lose.
12. To win the game, clear the whole board without detonating any mines.
''')
        
    elif n == 2:
        mode1 = 'DETONATION'
        title = 'Welcome to Detonation Mode!!'
        rules = ('''
1. Pick a level [Beginner/Intermediate/Advanced].
2. On your turn the board will be displayed, with a few numbers given beforehand.
3. Click on the location you want to dig.
4. Numbers on the boxes refer to the number of mines in neighbouring positions.
5. At every turn, number of mines left and also moves left will be displayed
6. With every click, more of the board will be revealed helping you find the mines.
7. Your goal is to detonate all mines before you run out of moves.
''')
        
    else:
        mode1 = 'TREASURE HUNT'
        title = 'Welcome to Treasure Hunt Mode!!'
        rules = ('''
1. Pick a level [Beginner/Intermediate/Advanced].
2. On your turn the board will be displayed, empty at first with mines and a treasure hidden in it.
3. Click on the location you want to dig.
4. Boxes will recursively be dug starting from the selected position until we reach a dug box adjacent to a mine.
5. Numbers on the boxes refer to the number of mines in neighbouring positions.
6. Press 'H' for a hint [Maximum 3 hints], or select hint through 'Help' menu.
7. Right click on a box to place a flag at potential mine location.
8. At every turn, number of mines left will be displayed, decreasing as you place more flags
9. If you dig at a mine position, you lose a life. Be careful! You have only 3 lives.
10. The treasure is a box on the board surrounded by mines on all sides.

             |# # #|
GOAL: |# T #| Find and click on this treasure ['T'] before you run out of lives to win the game!!
             |# # #|
''')
        
    
    rules_frame = LabelFrame(help_window, text = title, font = ('agency FB', 40, 'bold'),labelanchor= N, borderwidth = 8, relief = RIDGE, bg = 'turquoise3')
    rules_frame.pack()
    
    rules_label = Label(rules_frame, text = rules, justify = 'left',font = ('times new roman', 15), fg = 'white', borderwidth = 5, bg = 'Turquoise4', relief = GROOVE)

    if x == 'a':
        rules_label.grid(row = 0, column = 0, padx = 5, pady = 5)
        btn = Button(rules_frame, text = 'Ok, got it.', font = ('agency FB', 20, 'bold'), bg = 'Turquoise3', command = help_window.withdraw)
        btn.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'ew')
    else:
        root.withdraw()
        rules_label.grid(row = 0, column = 0,columnspan = 2, padx = 5, pady = 5)
  
        btn1 = Button(rules_frame, text = 'Back', font = ('agency FB', 20, 'bold'), bg = 'Turquoise3', command = lambda: home(help_window))
        btn1.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'ew')

        btn2 = Button(rules_frame, text = 'Ok, got it.', font = ('agency FB', 20, 'bold'), bg = 'Turquoise3', command = lambda: choose_level(mode1))
        btn2.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'ew')

num_colours = ['', 'DeepSkyBlue2', 'SpringGreen2', 'red3', 'RoyalBlue4', 'RoyalBlue4', 'RoyalBlue4', 'RoyalBlue4', 'RoyalBlue4']

home('a')
main.mainloop()
