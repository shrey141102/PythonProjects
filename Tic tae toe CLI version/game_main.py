import random
import tkinter as tk
from tkinter import messagebox

def print_board(board):
    game_board = "\nGame Board:\n"
    for row in board:
        game_board += " | ".join(row) + "\n" + "-" * 9 + "\n"
    return game_board

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def get_computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def get_row_col_from_position(position):
    row = (position - 1) // 3
    col = (position - 1) % 3
    return row, col

def handle_click(row, col):
    global board, player
    if board[row][col] == " ":
        board[row][col] = player
        game_label.config(text=print_board(board))
        
        if check_winner(board, player):
            result = messagebox.askyesno("Winner", f"Player {player} wins! Do you want to continue?")
            if result:
                reset_game()
        elif is_board_full(board):
            result = messagebox.askyesno("Tie", "It's a tie! Do you want to continue?")
            if result:
                reset_game()
        else:
            player = 'X' if player == 'O' else 'O'
            if player == 'O':
                computer_move()

def computer_move():
    global board, player
    row, col = get_computer_move(board)
    board[row][col] = player
    game_label.config(text=print_board(board))

    if check_winner(board, player):
        result = messagebox.askyesno("Winner", f"Player {player} wins! Do you want to continue?")
        if result:
            reset_game()
    elif is_board_full(board):
        result = messagebox.askyesno("Tie", "It's a tie! Do you want to continue?")
        if result:
            reset_game()
    else:
        player = 'X' if player == 'O' else 'O'

def reset_game():
    global board, player
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = 'X'
    game_label.config(text=print_board(board))

root = tk.Tk()
root.title("Tic Tac Toe")

board = [[" " for _ in range(3)] for _ in range(3)]
player = 'X'

game_label = tk.Label(root, text=print_board(board))
game_label.pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = []
button_number = 1
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(buttons_frame, text=str(button_number), width=4, height=2, command=lambda row=i, col=j: handle_click(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
        button_number += 1
    buttons.append(row_buttons)

player_label = tk.Label(root, text="You are player X")
player_label.pack()

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack()

root.mainloop()
