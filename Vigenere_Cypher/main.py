print("Welcome to Vignere Cipher Game\n")

def encrypt(message, key):
    message = message.lower()
    key = key.lower()

    cleaned_message = ""
    for character in message:
        if character.isalpha():
            cleaned_message += character
    message = cleaned_message

    cleaned_key = ""
    for character in key:
        if character.isalpha():
            cleaned_key += character
    key = cleaned_key

    key = key[:26]
    
    substitution_dict = {}
    for i in range(26):
        substitution_dict[chr(i+97)] = key[i]

    encrypted_message = ""
    for character in message:
        encrypted_message += substitution_dict[character]
    
    return encrypted_message

def decrypt(message, key):
    message = message.lower()
    key = key.lower()

    cleaned_message = ""
    for character in message:
        if character.isalpha():
            cleaned_message += character
    message = cleaned_message

    cleaned_key = ""
    for character in key:
        if character.isalpha():
            cleaned_key += character
    key = cleaned_key

    key = key[:26]

    substitution_dict = {}
    for i in range(26):
        substitution_dict[key[i]] = chr(i+97)

    decrypted_message = ""
    for character in message:
        decrypted_message += substitution_dict[character]

    return decrypted_message

def hack(message):
    english_letters = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']

    frequency_dict = {}
    for character in message:
        if character in frequency_dict:
            frequency_dict[character] += 1
        else:
            frequency_dict[character] = 1

    encrypted_letters = []
    for character in frequency_dict:
        encrypted_letters.append(character)
    encrypted_letters.sort(key = lambda x: frequency_dict[x], reverse = True)

    substitution_dict = {}
    for i in range(26):
        substitution_dict[encrypted_letters[i]] = english_letters[i]

    key = ""
    for i in range(26):
        key += substitution_dict[chr(i+97)]

    return key

def play():
    print("Enter 1 to encrypt a message")
    print("Enter 2 to decrypt a message")
    print("Enter 3 to end the game \n")

    choice = int(input("Please give your input "))
    
    if choice == 1:
        message = input("Enter the message to be encrypted : ")
        key = input("Enter the key : ")
        
        if len(key) < 26:
            print("Key is short, please use 26 letters in key \n")
            play()  
        encrypted_message = encrypt(message, key)
        print("The encrypted message is : ", encrypted_message)
        print("Do you want to play again ?")
        print("Enter 1 for yes and 2 for no")
        choice = int(input())
        if choice == 1:
            play()
        else:
            print("Thanks for playing")
            return
    
    elif choice == 2:
        message = input("Enter the message to be decrypted : ")
        key = input("Enter the key : ")
        if len(key) < 26:
            print("Key is short, please use 26 letters in key \n")
            play()        
        decrypted_message = decrypt(message, key)
        print("The decrypted message is : ", decrypted_message)
        print("Do you want to play again ?")
        print("Enter 1 for yes and 2 for no")
        choice = int(input())
        if choice == 1:
            play()
        else:
            print("Thanks for playing")
            return

    elif choice == 3:
        print("Thanks for playing")
        return

    else:
        print("Wrong choice")
        print("Do you want to play again ?")
        print("Enter 1 for yes and 2 for no")
        choice = int(input())
        if choice == 1:
            play()
        else:
            print("Thanks for playing")
            return

def rules():
    print("Rules : ")
    print("1. The message should contain only letters")
    print("2. The key should contain only letters")
    print("3. The key should be of 26 letters")
    print("4. The key should not contain any letter more than once")
    print("5. The key should not contain any symbol or space")
    print("6. The message should not contain any symbol or space \n \n \n")

rules()
play()