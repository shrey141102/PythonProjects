# ASCII control characters (0-31 and 127)
# ASCII printable characters (32-126) (most commonly referred to)
# Extended ASCII characters (128-255)

with open('ascii.txt', 'w') as f:
    for i in range(33,127):
        f.write(f"ASCII CODE FOR {chr(i)} IS {i}\n")
print("File created")

# Use .join() to create a word using ascii characters
# print("".join(chr[i] for i in [ascii code corresponding the letter]))

for i in range(33,127):
        print(f"ASCII CODE FOR {chr(i)} IS {i}\n")

# Some examples 
# Congratulations
print(''.join([chr(i) for i in [67, 111, 110, 103, 114, 97, 116, 117, 108, 97, 116, 105, 111, 110, 115]]))

# Happy Birthday
print(''.join([chr(i) for i in [72, 97, 112, 112, 121, 0, 66, 105, 114, 116, 104,100, 97, 121]]))

# Thank You
print(''.join([chr(i) for i in [84, 104, 97, 110, 107, 0, 89, 111, 117]]))

# Welcome
print(''.join([chr(i) for i in [87, 101, 108, 99, 111, 109, 101]]))

# Hi!
print(''.join([chr(i) for i in [72, 105, 33]]))