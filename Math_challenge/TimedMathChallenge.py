import random
import time

# Define operators for the arithmetic expressions
OPERATORS = ["+", "-", "*"]
# Define the minimum and maximum operands for the arithmetic expressions
MIN_OPERAND = 3
MAX_OPERAND = 12
# Define the total number of problems to be generated
TOTAL_PROBLEMS = 10

# Function to generate a random arithmetic problem
def generate_problem():
    # Generate random operands and operator
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    # Create the arithmetic expression as a string
    expr = str(left) + " " + operator + " " + str(right)
    # Calculate the correct answer using eval() function
    answer = eval(expr)
    return expr, answer

# Initialize a counter for incorrect answers
wrong = 0

# Prompt the user to start the quiz
input("Press enter to start!")
print("----------------------")

# Record the start time to calculate the total time taken
start_time = time.time()

# Loop through the total number of problems
for i in range(TOTAL_PROBLEMS):
    # Generate a new problem
    expr, answer = generate_problem()
    
    # Continue asking the user for input until they provide the correct answer
    while True:
        # Prompt the user with the current problem and get their guess
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        
        # Check if the guess is correct
        if guess == str(answer):
            break
        # If the guess is incorrect, increment the wrong counter
        wrong += 1

# Record the end time and calculate the total time taken
end_time = time.time()
total_time = round(end_time - start_time, 2)

# Display the final results
print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")