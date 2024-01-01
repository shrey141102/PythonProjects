#A basic arithmetic calculator
print("WELCOME TO OUR CAlCULATOR!!!!!!!!!!!!")# welcome message to the user
num1 = int(input("Enter the 1st number: "))# values for num1
num2 = int(input("Enter the 2nd number")) # values for num2

op = input("Enter +/*///- : Add,Sub,Mul,Div") #commands for operations

# addition function
def add(n1,n2):
    return n1+n2

# substraction function 
def sub(n1,n2):
    return n1-n2

# multiplication function 
def mul(n1,n2):
    return n1*n2

#division function
def div(n1,n2):
    return n1/n2



# While for N number of times to execute  

while True:
    if op == "+":
        print("Here is the Sum of two number :",add(num1,num2)) # it will give output for addtion operation
    
    elif op == "-":
        print("Here is the subtraction of two number :",add(num1,num2)) # it will give output for subtraction

    elif op == "*":
        print("Here is the multiplication of two number :",add(num1,num2)) # it will give output for multiplication

    elif op == "/":
        print("Here is the division of two number :",add(num1,num2)) # it will give output for division
    
# take input from user whether they want to continue or not
    choice = input("Do you want to continue?(y/n)")

    if choice == "n":
        break

