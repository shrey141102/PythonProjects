
print("Welcome to Tic Tac Toe")

def print_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

def check_win(board):
    if board[0] == board[1] == board[2] != " ":
        return True
    elif board[3] == board[4] == board[5] != " ":
        return True
    elif board[6] == board[7] == board[8] != " ":
        return True
    elif board[0] == board[3] == board[6] != " ":
        return True
    elif board[1] == board[4] == board[7] != " ":
        return True
    elif board[2] == board[5] == board[8] != " ":
        return True
    elif board[0] == board[4] == board[8] != " ":
        return True
    elif board[2] == board[4] == board[6] != " ":
        return True
    else:
        return False

def check_draw(board):
    if " " not in board:
        return True
    else:
        return False

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print_board(board)
    player = "X"
    while True:
        print("Player", player, "turn")
        position = int(input("Enter the position: "))-1
        if board[position] == " ":
            board[position] = player
            print_board(board)
            if check_win(board):
                print("Player", player, "wins")
                break
            elif check_draw(board):
                print("It's a draw")
                break
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("The position is already filled")
            continue
    print("Do you want to play again?")
    print("Enter 1 for yes and 2 for no")
    user_choice = int(input())
    if user_choice == 1:
        play_game()
    else:
        print("Thanks for playing")
        return

play_game()
