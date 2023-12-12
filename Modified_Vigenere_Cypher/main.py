def vigenere_encrypt(text, key):
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_length = len(key)
    for i in range(len(text)):
        result += alphabet[(alphabet.find(text[i]) + (alphabet.find(key[i % key_length]) + 1)) % 26]
    return result

def vigenere_decrypt(text, key):
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_length = len(key)
    for i in range(len(text)):
        result += alphabet[(alphabet.find(text[i]) - (alphabet.find(key[i % key_length]) + 1)) % 26]
    return result

def run_game():
    print("Enter 1 to encrypt a message")
    print("Enter 2 to decrypt a message")
    print("Enter 3 to end the game \n")
    user_choice = int(input("Please give your input: "))

    if user_choice == 1:
        message = input("Enter the message to be encrypted: ")
        key = input("Enter the key: ")
        message_without_spaces = message.replace(" ", "")
        key_without_spaces = key.replace(" ", "")

        encrypted_message = vigenere_encrypt(message_without_spaces, key_without_spaces)
        print("The encrypted message is: ", encrypted_message)
        print("Do you want to play again?")
        print("Enter 1 for yes and 2 for no")
        user_choice = int(input())
        if user_choice == 1:
            run_game()
        else:
            print("Thanks for playing")
            return

    elif user_choice == 2:
        message = input("Enter the message to be decrypted: ")
        key = input("Enter the key: ")
        message_without_spaces = message.replace(" ", "")
        key_without_spaces = key.replace(" ", "")
        decrypted_message = vigenere_decrypt(message_without_spaces, key_without_spaces)
        print("The decrypted message is: ", decrypted_message)
        print("\n Do you want to play again?")
        print("Enter 1 for yes and 2 for no")
        user_choice = int(input())
        if user_choice == 1:
            run_game()
        else:
            print("Thanks for playing")
            return

    elif user_choice == 3:
        print("Thanks for playing")
        return



print("Welcome to the Modified Vigenere Cypher \n")
print("The rules are as follows: ")
print("1. The message should only contain lowercase letters")
print("2. The key should only contain lowercase letters")
print("3. They must not have any spaces in between")


run_game()