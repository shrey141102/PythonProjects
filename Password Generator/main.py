import random
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
def generate_password(nl, ns, nn, shuffle=True):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    
    password += [random.choice(letters) for _ in range(nl)]
    password += [random.choice(symbols) for _ in range(ns)]
    password += [random.choice(numbers) for _ in range(nn)]

    if shuffle:
        random.shuffle(password)

    return ''.join(password)

print("Welcome to the PyPassword Generator!")
nl = int(input("How many letters would you like in your password?\n"))
ns = int(input("How many symbols would you like?\n"))
nn = int(input("How many numbers would you like?\n"))

shuffle_option = input("Do you want to shuffle the characters in the password? (yes/no): ").lower()
shuffle_password = shuffle_option == 'yes'

generated_password = generate_password(nl, ns, nn, shuffle_password)
print("Your generated password is:", generated_password)

## By including the shuffle parameter, 
# you give users the flexibility to choose whether they prioritize a completely random arrangement of characters for
#  increased security or if they prefer a specific structure for ease of memorization or other reasons
