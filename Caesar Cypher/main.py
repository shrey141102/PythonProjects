from art import logo

print(logo)

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(txt, shft, dirc):
    new_word = ""
    n = 0
    for i in txt:
        if i not in alphabet:
            new_word += i + ""
            continue
        if i == " ":
            new_word += " " + ""
            continue
        n = alphabet.index(i)
        if dirc == "encode":
            n += shft
            while n >= 26:
                n = n - 26
        if dirc == "decode":
            n -= shft
            while n < 0:
                n = n + 26
        new_word += alphabet[n] + ""
    print(f"The {dirc}d text is :\n", new_word.capitalize())


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    choice = input("Do you want to continue the cipher program?\n").lower()
    if choice == "no":
        print("Goodbye😃")
        break
