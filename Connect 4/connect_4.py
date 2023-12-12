# intro
print('\033[1m' + '\033[4m' + '\033[96m' + "WELCOME TO CONNECT 4" + '\033[0m' + '\033[96m' + '\033[1m' + ' !!!' +  '\033[0m') 
print('\033[1m' + '\033[4m' + '\033[31m' + '''
RULES:-''' + '\033[0m' + '''
1.On your turn enter a column number.
2.A checker(coloured piece) will be dropped in the column.
3.It will be placed above the first occupied spot in the column.
4.Your objective is to get 4 checkers in a row / column / diagonal before the other player can.
 
Not as easy as it looks! Have fun!!
''')
ans = 'Y'
# variable to govern whose turn it is
x = 0
# get player names
player_1 = input('Player 1, please enter your name: ' )
player_2 = input('Player 2, please enter your name: ')
print()
players = {'🔴': player_1, '🔵':player_2}
 
# get grid size
row = int(input("enter number of rows(min 4): "))
column = int(input("enter number of columns(4 to 9): "))
print()
 
grid = []
for i in range(column):
    grid.append([])
    for j in range(row):
        grid[i].append('⚪')
 
num = '➀➁➂➃➄➅➆➇➈'
for i in num:
    if num.index(i) < column:
        print('|' + '\033[1m' + str(i) +'\033[0m', end = '')
print('|')
    
for i in range(row):
    for j in range(column):
        print(grid[j][i], end =  '')
    print()
 
# main game loop
while ans == 'Y':
       
    # get column number
    if x%2 == 0:
        n = int(input(players['🔴']+ ' please enter column number: \n'))
    else:
        n = int(input(players['🔵']+ ' please enter column number: \n' ))
  
    # check for invalid inputs
    while n > column:
        print('Invalid input, column number out of range.')
        n = int(input('Please enter another column number: \n' ))
 
    while '⚪' not in grid[n-1]:
        print('Invalid input, column full.')
        n = int(input('Please enter another column number: \n'))
 
    
    for i in range(row):
        if grid[n-1][i] != '⚪':
            grid[n-1][i-1] = list(players.keys())[x%2]
            filled_column, filled_row = n-1, i-1
            break
    else:
       grid[n-1][row-1] = list(players.keys())[x%2]     
       filled_column, filled_row = n-1, row-1

    
    num = '➀➁➂➃➄➅➆➇➈'
    for i in num:
        if num.index(i) < column:
            print('|' + '\033[1m' + str(i) +'\033[0m', end = '')
    print('|')
    
    for i in range(row):
        for j in range(column):
           print(grid[j][i], end =  '')
        print()

        current_colour = (list(players.keys()))[x%2]
 
    # check column
    c = 0
    k= False
    for i in grid[filled_column]:
        if i == current_colour:
            c+=1
        else:
            c=0
    if c >= 4:
        k=True
 
    # check row
    c = 0
    for i in range(column):
       if grid[i][filled_row] == current_colour:
           c+=1
       else:
           c=0
    if c>=4:
        k=True
       
 
    # check diagonal1
    c = 0
    A,B = filled_column+filled_row,0
    while A>column-1:
        A,B = A-1, B+1
    while B<=row-1 and A>=0:
        if grid[A][B] == current_colour:
            c += 1
        else:
            c = 0
        A,B = A-1, B+1
    if c>=4:
       k=True
 
    # check diagonal2   
    c = 0
    A,B = filled_column-filled_column,0
    while A<0:
        A,B = A+1,B+1
    while B<=row-1 and A<=column-1:
        if grid[A][B] == current_colour:
            c+=1
        else:
            c = 0
        A,B = A+1,B+1
    if c>=4:
        k=True
    if  k== True:
        print('Congrats!!', list(players.values())[x%2],'wins.\n')
        ans = input('Do you want to play again [Y,N]?? ')
        print()
        if ans == 'Y':
                row = int(input("enter number of rows(min 4): "))
                column = int(input("enter number of columns(4 to 9): "))
                grid = []
                for i in range(column):
                    grid.append([])
                    for j in range(row):
                        grid[i].append('⚪')

              
                num = '➀➁➂➃➄➅➆➇➈'
                for i in num:
                    if num.index(i) < column:
                        print('|' + '\033[1m' + str(i) +'\033[0m', end = '')
                print('|')
                for i in range(row):
                    for j in range(column):
                        print(grid[j][i], end =  '')
                    print()

 
    
    tie = True
    for i in grid:
        for j in i:
            if j == '⚪':
                tie = False
                break
        if tie == False:
            break
    if tie == True:
        print("It's a tie!\n")
        ans = input('Do you want to play again [Y,N]?? ')
        print()
        if ans == 'Y':
              row = int(input("enter number of rows(min 4): "))
              column = int(input("enter number of columns(4 to 9): "))
              grid = []
              for i in range(column):
                grid.append([])
                for j in range(row):
                  grid[i].append('⚪')
             
              num = '➀➁➂➃➄➅➆➇➈'
              for i in num:
                if num.index(i) < column:
                  print('|' + '\033[1m' + str(i) +'\033[0m', end = '')
                print('|')
              for i in range(row):
                for j in range(column):
                  print(grid[j][i], end =  '')
                print()            
       
    x += 1
