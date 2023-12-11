import pyfiglet

# check font list from fonts.txt

font = input("Enter type of font\n") or "slant"
text = str(input("Enter your text\n")) or "Text"

with open('fonts.txt') as f:
    arr = f.read().split()

if font in arr:
    result = pyfiglet.figlet_format(text, font=font)
    print(result)

else:
    print(f"Sorry {font} font not found. Error 404")