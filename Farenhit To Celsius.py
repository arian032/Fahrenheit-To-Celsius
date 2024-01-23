# from curses.ascii import 
import tkinter as tk
from tkinter import E, W
from webbrowser import get

window = tk.Tk()

tk.geometry("300x200")

textvar = tk.StringVar(
    master=window,
    value='Resualt show here...'
    )
fahrenheit_label = tk.Label(
    master=window,
    text='Fahrenheit:'
    )
fahrenheit_entry = tk.Entry(
    master=window,
    width=10,
    )

def fahrenheit_to_celsius():
    
    if fahrenheit_entry.get().isalpha():
        textvar.set('Pleas Enter only a number')
    else:
        textvar.set((int(fahrenheit_entry.get()) - 32) / 1.8)

Calc_button = tk.Button(
    master=window,
    text='Calc',
    command=fahrenheit_to_celsius,
    )



celsius_label = tk.Label(
    master=window,
    text='Celsius:',
    )
answer_label = tk.Label(
    master=window,
    textvariable=textvar,
    )



fahrenheit_label.grid(row=0, column=0)
fahrenheit_entry.grid(row=0, column=1)
Calc_button.grid(row=0, column=3, sticky=(E, W))
celsius_label.grid(row=1, column=0)
answer_label.grid(row=1, column=1)

window.mainloop()

