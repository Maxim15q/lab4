import tkinter as tk
import random as rnd


def clicked():
    let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dig = '0123456789'
    d = ''
    for i in range(3):
        a = []
        for j in range(3):
            a += let[rnd.randrange(26)]
        for j in range(2):
            a += dig[rnd.randrange(10)]
        rnd.shuffle(a)
        d += ''.join(a) + '-'
    mma.delete(0, 'end')
    mma.insert(0, d[:17])


window = tk.Tk()
window.title('game')
window.geometry('1300x775')
window.resizable(width=False, height=False)
bg = tk.PhotoImage(file='braw.png')

frame = tk.Frame(window, width=1300, height=775)
frame.place(relx=0, rely=0)

label_bg = tk.Label(frame, image=bg)
label_bg.place(relx=0, rely=0)

mma = tk.Entry(frame, font=('Arial', 30), width=25)
mma.place(relx=0.5, rely=0.4, anchor='center')

bt = tk.Button(frame, text='Key', font=("Arial", 20), command=clicked)
bt.place(relx=0.5, rely=0.5, anchor='center')

window.mainloop()
