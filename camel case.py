s=input("enter string:")
count=0

    
for i in range(len(s)):
    if ord(s[i]) >= 65 and ord(s[i]) <= 91:
           count += 1
print(count)
