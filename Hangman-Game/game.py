import tkinter as tk
import random
from hangman_words import word_list
from hangman_art import stages,logo

def update_hangman():
    global lives
    if lives >= 0:
        hangman_image_label.config(text=stages[lives])
        lives -= 1
    else:
        message_label.config(text=f"You lose. The word was {chosen_word.capitalize()}")

# Select a random word from the list
chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)
guessed_letters = set()
lives = len(stages) - 1

def check_guess():
    global lives
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if guess in guessed_letters:
        pass
    else:
        guessed_letters.add(guess)
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = letter
            guessed_word_label.config(text=" ".join(display))
            if "_" not in display:
                message_label.config(text="Congratulations! You win.")
        else:
            lives -= 1
            if lives >= 0:
                update_hangman()
            else:
                message_label.config(text=f"You lose. The word was {chosen_word.capitalize()}")
                
    if lives < 0 or "_" not in display:
        guess_button.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Hangman")

hangman_image_label = tk.Label(root, text=stages[lives], font=('Courier', 12))
hangman_image_label.pack()

logo_label = tk.Label(root, text=logo, font=('Arial', 14))
logo_label.pack()

guessed_word_label = tk.Label(root, text=" ".join(display), font=('Arial', 24))
guessed_word_label.pack()

guess_label = tk.Label(root, text="Enter a letter:", font=('Arial', 14))
guess_label.pack()

guess_entry = tk.Entry(root, font=('Arial', 14))
guess_entry.pack()

guess_button = tk.Button(root, text="Guess", command=check_guess, font=('Arial', 14))
guess_button.pack()

message_label = tk.Label(root, text="", font=('Arial', 16))
message_label.pack()

root.mainloop()
