"""will contain all the calculations"""
from tkinter import *


class BalanceCalculator:
    def __init__(self):
        self.current_balance = 0
        self.loan_balance = 0

    def deposit(self):
        new_window = Tk()
        new_window.title('Make a deposit')
        new_window.minsize(width=250, height=200)
        amount_label = Label(new_window, text='Amount:')
        entry = Entry(new_window, width=20)
        entry.grid(row=0, column=1, columnspan=2, padx=10)
        amount_label.grid(column=0, row=0, padx=20, pady=30)
        ok_button = Button(new_window, text='submit')
        ok_button.grid(row=2, column=1)
        new_window.mainloop()

    def loan(self):
        new_window = Tk()
        new_window.title('Make a loan')
        new_window.minsize(width=250, height=250)
        amount_label = Label(new_window, text='Amount:')
        amount_label.grid(column=0, row=0, padx=10, pady=30)
        new_window.mainloop()

    def payment(self):
        new_window = Tk()
        new_window.title('Make payment')
        new_window.minsize(width=250, height=250)
        amount_label = Label(new_window, text='Amount:')
        amount_label.grid(column=0, row=0, padx=10, pady=30)
        new_window.mainloop()