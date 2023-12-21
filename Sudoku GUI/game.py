import copy
import random

import numpy as np
import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set the dimensions of the screen
WIDTH, HEIGHT = 540, 600
CELL_SIZE = 60
GRID_SIZE = 9
BOARD_SIZE = CELL_SIZE * GRID_SIZE
boat = [[0 for _ in range(9)] for _ in range(9)]

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Font settings
font = pygame.font.Font(None, 36)
bold_font = pygame.font.Font(None, 42)


def draw_grid():
    for i in range(GRID_SIZE + 1):
        thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(
            screen, BLACK, (0, i * CELL_SIZE), (BOARD_SIZE, i * CELL_SIZE), thickness
        )
        pygame.draw.line(
            screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, BOARD_SIZE), thickness
        )


def draw_numbers(board, user_input):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            cell_value = str(user_input[i][j]) if user_input[i][j] != 0 else ""
            if board[i][j] != 0:
                num = font.render(str(board[i][j]), True, BLACK)
                screen.blit(num, (j * CELL_SIZE + 20, i * CELL_SIZE + 10))
            else:
                user_num = font.render(cell_value, True, BLUE)
                screen.blit(user_num, (j * CELL_SIZE + 20, i * CELL_SIZE + 10))


def create_sudoku():
    base = 3
    side = base * base

    # Pattern for a baseline valid solution
    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side

    # Randomly shuffle numbers
    def shuffle(s):
        return random.sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # Produce board using randomized baseline pattern
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    # Full board solution for reference
    solution = [[board[r][c] for c in range(side)] for r in range(side)]

    # Remove numbers to create the puzzle
    squares = side * side
    empties = squares * 1 // 2
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board


sudoku = create_sudoku()


def possible(row, column, number):
    global sudoku
    for i in range(0, 9):
        if sudoku[row][i] == number:
            return False
    for i in range(0, 9):
        if sudoku[i][column] == number:
            return False

    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[y0 + i][x0 + j] == number:
                return False
    return True


def solve():
    global sudoku
    solutions = []  # Store all solutions here

    def solve_sudoku():
        nonlocal solutions
        for row in range(0, 9):
            for column in range(0, 9):
                if sudoku[row][column] == 0:
                    for number in range(1, 10):
                        if possible(row, column, number):
                            sudoku[row][column] = number
                            solve_sudoku()
                            sudoku[row][column] = 0
                    return
        # When a solution is found, append a copy of the solution to the solutions list
        solutions.append(np.copy(sudoku))

    solve_sudoku()
    return solutions


solutions = solve()


def check_solution(user_input, solved):
    for solution in solved:
        if all(row in solution for row in user_input):
            return True
    return False


def main():
    user_input = [row[:] for row in sudoku]
    selected = None

    running = True
    while running:
        screen.fill(WHITE)

        draw_grid()
        draw_numbers(sudoku, user_input)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("\nAll possible solutions given below :\n")

                for idx, sol in enumerate(solutions, start=1):
                    print(f"Solution {idx}:")
                    print(np.matrix(sol))
                    print()

                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE
                selected = (row, col)
            elif event.type == pygame.KEYDOWN:
                if selected:
                    row, col = selected
                    if event.key == pygame.K_BACKSPACE:
                        user_input[row][col] = 0
                    elif event.key in range(pygame.K_1, pygame.K_9 + 1):
                        user_input[row][col] = event.key - pygame.K_0

        if selected:
            pygame.draw.rect(
                screen,
                BLUE,
                (
                    selected[1] * CELL_SIZE,
                    selected[0] * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE,
                ),
                3,
            )

        if all(cell != 0 for row in user_input for cell in row):
            if check_solution(user_input, solutions):
                text = bold_font.render("Success!", True, BLACK)
            else:
                text = bold_font.render("Attempted Failed!", True, RED)
            screen.blit(text, (150, BOARD_SIZE + 20))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
