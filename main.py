from tkinter import *
import random

root = Tk()
root.title('Password Generator App')

root.geometry("350x350")

pwdstr = StringVar()

pwdlength = IntVar()

pwdlength.set(0)

def generate():

    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
            '*', '(', ')']

    password = ""
    for x in range(pwdlength.get()):
        password = password + random.choice(pass1)

    pwdstr.set(password)


Label(root, text="Password Generator \n Application", font="calibri 20 bold").pack()

Label(root, text="Enter password length").pack(pady=3)

Entry(root, textvariable=pwdlength).pack(pady=3)

Button(root, text="Generate Password", command=generate).pack(pady=7)

Entry(root, textvariable=pwdstr).pack(pady=3)

root.mainloop()