
from tkinter import *

root = Tk()
root.title("Binary converter")
root.geometry("500x300+0+0")
root.configure(bg = 'teal')

a1 = StringVar()
a2 = StringVar()
a1.set('bnry')
a2.set('bnry')
ans = 0

def bnry_deci(n):
    global ans
    x = 0
    ans = 0
    while n > 0:
        d = n%10
        n//=10
        ans += 2**x * d
        x += 1
    
def deci_bnry(n):
    global ans
    ans = ''
    print(n)
    while n > 0:
        d = n%2
        n//=2
        ans += str(d)
    ans = ans[::-1]

def deci_octa(n):
    global ans
    ans = ''
    while n > 0:
        d = n%8   
        n//=8
        ans += str(d)
    ans = ans[::-1]
        
def bnry_hexa(n): 
    global ans
    key = {'0': '0', '1': '1', '10': '2', '11': '3', '100': '4', '101': '5', '110': '6', '111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    ans = ''
    while n > 0:
        d = n%10000
        n //= 10000
        ans += key[str(d)]
    ans = ans[::-1]    

def octa_deci(n):
    global ans
    x = 0
    ans = 0
    while n > 0:
        d = n%10
        n//=10
        ans += 8**x * d
        x += 1

def hexa_deci(n):
    global ans
    key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    x = len(n) - 1
    ans = 0
    for i in n:
        ans += int(key.index(i))*16**x
        x -= 1

def convert(type1,type2):
    global ans
    n2.delete(0, END)

    if type1 == 'bnry':
        if type2 == 'deci':
            bnry_deci(int(n1.get()))
        elif type2 == 'octa':
            bnry_deci(int(n1.get()))
            deci_octa(int(ans))
        elif type2 == 'hexa':
            bnry_hexa(int(n1.get()))

    elif type1 == 'deci':
        if type2 == 'bnry':
            deci_bnry(int(n1.get()))
        elif type2 == 'octa':
            deci_octa(int(n1.get()))
        elif type2 == 'hexa':
            deci_bnry(int(n1.get()))
            bnry_hexa(int(ans))

    elif type1 == 'octa':
        if type2 == 'bnry':
            octa_deci(int(n1.get()))
            deci_bnry(int(ans))
        elif type2 == 'deci':
            octa_deci(int(n1.get()))
        elif type2 == 'hexa':
            octa_deci(int(n1.get()))
            deci_bnry(int(ans))
            bnry_hexa(int(ans))

    elif type1 == 'hexa':
        if type2 == 'bnry':
            hexa_deci(n1.get())
            deci_bnry(int(ans))
        elif type2 == 'deci':
            hexa_deci(n1.get())
        elif type2 == 'octa':
            hexa_deci((n1.get()))
            deci_octa(int(ans))

    n2.insert(10, ans)


lb = Label(root, text = 'Binary converter', font = ('arial', 40), background = 'teal', borderwidth = 5)
lb.grid(row = 0, column = 0, columnspan = 4, padx = 47)

n1 = Entry(root, text = 'Enter number', font = ('arial', 14))
n2 = Entry(root, font = ('arial', 14))

n1.grid(row = 1, column = 0, pady = 10, columnspan = 2)
n2.grid(row = 1, column = 2, pady = 10, columnspan = 2)

lb2 = Label(root, text = 'TO', font = ('arial', 20), background = 'teal', borderwidth = 5)
lb2.grid(row = 2, column = 1, columnspan = 2)
convertbtn = Button(root, text = 'CONVERT', font = ('arial', 20), bg = 'lightseagreen', command = lambda: convert(a1.get(), a2.get()))
convertbtn.grid(row = 3, column = 1, columnspan = 2)

n1frame = Frame(root, borderwidth = 3, bg = 'lightseagreen', bd = 5, height = 100, width = 90)
n2frame = Frame(root, borderwidth = 3, bg = 'lightseagreen', bd = 5, height = 100, width = 90)

n1frame.grid(row = 2, column = 0)
n2frame.grid(row = 2, column = 3)

n1bnry = Radiobutton(n1frame, text = 'Binary', bg = 'lightseagreen', font = (20), value = 'bnry', variable = a1)
n1deci = Radiobutton(n1frame, text = 'Decimal', bg = 'lightseagreen', font = (20), value = 'deci', variable = a1)
n1octa = Radiobutton(n1frame, text = 'Octal', bg = 'lightseagreen', font = (30), value = 'octa', variable = a1)
n1hexa = Radiobutton(n1frame, text = 'Hexadeci', bg = 'lightseagreen', font = (10), value = 'hexa', variable = a1)

n1bnry.grid(row = 0, column = 0)
n1deci.grid(row = 1, column = 0)
n1octa.grid(row = 2, column = 0)
n1hexa.grid(row = 3, column = 0)

n1bnry = Radiobutton(n2frame, text = 'Binary', bg = 'lightseagreen', font = (20), value = 'bnry', variable = a2)
n1deci = Radiobutton(n2frame, text = 'Decimal', bg = 'lightseagreen', font = (20), value = 'deci', variable = a2)
n1octa = Radiobutton(n2frame, text = 'Octal', bg = 'lightseagreen', font = (30), value = 'octa', variable = a2)
n1hexa = Radiobutton(n2frame, text = 'Hexadeci', bg = 'lightseagreen', font = (10), value = 'hexa', variable = a2)

n1bnry.grid(row = 0, column = 0)
n1deci.grid(row = 1, column = 0)
n1octa.grid(row = 2, column = 0)
n1hexa.grid(row = 3, column = 0)

root.mainloop()

