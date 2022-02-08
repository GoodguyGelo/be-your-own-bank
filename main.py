import tkinter
from balance_calculator import BalanceCalculator

balance_calculator = BalanceCalculator()
window = tkinter.Tk()
window.title('Be Your Own Bank')
window.minsize(width=300, height=330)

window.config(background='#C0A080')

# logo

bank = tkinter.PhotoImage(file="images/bank2.png")
canvas = tkinter.Canvas(width=296, height=172)
canvas.create_image(148, 86, image=bank)
canvas.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

# labels

current_balance_label = tkinter.Label(text='Current Balance:', background='#C0A080')
current_balance_label.grid(row=1, column=0, padx=10, pady=10)

current_balance_value = tkinter.Label(text=f'{balance_calculator.current_balance}', background='#C3DBD9', width=24)
current_balance_value.grid(row=1, column=1, columnspan=2)

loan_balance_label = tkinter.Label(text='Loan Balance:', background='#C0A080')
loan_balance_label.grid(row=2, column=0, padx=10, pady=10)

loan_balance_value = tkinter.Label(text=f'{balance_calculator.loan_balance}', background='#9D5353', width=24)
loan_balance_value.grid(row=2, columnspan=2, column=1)


# buttons

loan_button = tkinter.Button(text='Loan', width=10, command=balance_calculator.loan)
loan_button.grid(row=3, column=0)

make_payment_button = tkinter.Button(text='Payment', width=10, command=balance_calculator.payment)
make_payment_button.grid(row=3, column=1)

deposit_button = tkinter.Button(text='Deposit', width=10, command=balance_calculator.deposit)
deposit_button.grid(row=3, column=2)







window.mainloop()