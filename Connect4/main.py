import pygame
import sys

# initializing pygame
pygame.init()


# CONSTANTS
sqSize = 100
cols, rows = 8, 6
sqs = [[] for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        sqs[i].append( pygame.Rect((sqSize + 5) * j, (sqSize + 5) * i, sqSize, sqSize) )


# Initializing the screen
width, height = (sqSize + 4) * cols, (sqSize + 4) * rows
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Connect 4")


# GAME VARIABLES
vals = [[0 for i in range(cols)] for j in range(rows)]
clickedCol = None
rowToBePlaced = None
selected = False
turn = 1  # 1 for yellow, -1 for red
started, ended, yellowWon, redWon, tie = [False] * 5


# FONT VARIABLES
font1 = pygame.font.Font("freesansbold.ttf", 32)
font2 = pygame.font.Font("freesansbold.ttf", 16)


# GAME UTILITIES
def resetGame():
    global clickedCol, rowToBePlaced, selected, turn, started, ended, yellowWon, redWon, tie, vals

    vals = [[0 for i in range(cols)] for j in range(rows)]

    clickedCol = None
    rowToBePlaced = None
    selected = False
    turn = 1
    started, ended, yellowWon, redWon, tie = [False] * 5


def checkGameEndAndWinner():
    global yellowWon, redWon, tie, ended
    # horizontal check
    for i in range(rows):
        for j in range(cols - 3):
            if vals[i][j] == vals[i][j + 1] == vals[i][j + 2] == vals[i][j + 3] == 1:
                yellowWon = True
            elif vals[i][j] == vals[i][j + 1] == vals[i][j + 2] == vals[i][j + 3] == -1:
                redWon = True

    # vertical check
    for i in range(rows - 3):
        for j in range(cols):
            if vals[i][j] == vals[i + 1][j] == vals[i + 2][j] == vals[i + 3][j] == 1:
                yellowWon = True
            elif vals[i][j] == vals[i + 1][j] == vals[i + 2][j] == vals[i + 3][j] == -1:
                redWon = True

    # diagonal check
    for i in range(rows - 3):
        for j in range(cols - 3):
            if vals[i][j] == vals[i + 1][j + 1] == vals[i + 2][j + 2] == vals[i + 3][j + 3] == 1:
                yellowWon = True
            elif vals[i][j] == vals[i + 1][j + 1] == vals[i + 2][j + 2] == vals[i + 3][j + 3] == -1:
                redWon = True

    for i in range(rows - 3):
        for j in range(3, cols):
            if vals[i][j] == vals[i + 1][j - 1] == vals[i + 2][j - 2] == vals[i + 3][j - 3] == 1:
                yellowWon = True
            elif vals[i][j] == vals[i + 1][j - 1] == vals[i + 2][j - 2] == vals[i + 3][j - 3] == -1:
                redWon = True

    # tie check
    if 0 not in vals[0]:
        tie = True

    if yellowWon or redWon or tie:
        ended = True


def handlePlacingPiece(mouseX):
    global clickedCol, rowToBePlaced, selected, turn, vals

    clickedCol = mouseX // (sqSize + 5)
    for x in range(rows - 1, -1, -1):
        if vals[x][clickedCol] != 0:
            continue
        rowToBePlaced = x
        selected = True
        vals[rowToBePlaced][clickedCol] = turn
        turn *= -1
        break

    if not selected:
        clickedCol = None


### GAME SCREEN RENDERERS ###
def renderGameScreen():
    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(surface, (150, 150, 150), sqs[i][j])
            pygame.draw.ellipse(surface, (100, 100, 100), sqs[i][j])
            if vals[i][j] == 1:
                pygame.draw.ellipse(surface, (255, 255, 0), sqs[i][j])
            elif vals[i][j] == -1:
                pygame.draw.ellipse(surface, (255, 0, 0), sqs[i][j])


def renderStartScreen():
    surface.fill((41, 44, 36))
    startText = font1.render("START", True, (200, 200, 200))
    pressEnterText = font2.render("Press Enter or Click To Begin", True, (200, 200, 200))
    surface.blit(startText, (width / 2 - startText.get_rect().width / 2, height / 2 - startText.get_rect().height/2))
    surface.blit(pressEnterText, (width/2 - pressEnterText.get_rect().width/2, height/2 + pressEnterText.get_rect().height/2 + startText.get_rect().height))


def renderEndScreen():
    surface.fill((41, 44, 36))
    if yellowWon:
        winText = font1.render("YELLOW WON", True, (200, 200, 200))
    elif redWon:
        winText = font1.render("RED WON", True, (200, 200, 200))
    else:
        winText = font1.render("TIE", True, (200, 200, 200))

    pressEnterText = font2.render(
        "Press Enter or Click To Play Again", True, (200, 200, 200))
    surface.blit(winText, (width / 2 - winText.get_rect().width / 2, height / 2 - winText.get_rect().height/2))
    surface.blit(pressEnterText, (width/2 - pressEnterText.get_rect().width/2, height/2 + pressEnterText.get_rect().height/2 + winText.get_rect().height))


# GAME LOOP
while True:
    # event Handling
    for e in pygame.event.get():
        # for closing the window and exiting the game
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        mouseX, mouseY = pygame.mouse.get_pos()

        # for placing the piece
        if started and e.type == pygame.MOUSEBUTTONDOWN:
            handlePlacingPiece(mouseX)

            # for starting and restarting the game
        clickedOrEntered = lambda: (e.type == pygame.MOUSEBUTTONDOWN and mouseX > 0 and mouseY > 0 and mouseY < width and mouseY < height) or (e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN)
        if not started and clickedOrEntered():
            started = True
        if ended and clickedOrEntered():
            resetGame()

    surface.fill((100, 100, 100))

    # checking if the game has ended
    checkGameEndAndWinner()

    # rendering the screen
    if started and not ended:
        renderGameScreen()
    elif ended:
        renderEndScreen()
    else:
        renderStartScreen()

        # updating the display
    pygame.display.flip()