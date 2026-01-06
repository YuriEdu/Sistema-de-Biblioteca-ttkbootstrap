import tkinter as tk
from random import randint

def roll():
    label['text'] = f'{randint(1, 6)}'

window = tk.Tk()

button = tk.Button(text='Roll', width=13, height=2, command=roll)
button.pack()

label = tk.Label(text='0', height=3)
label.pack()

window.mainloop()