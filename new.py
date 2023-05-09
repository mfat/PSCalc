import tkinter as tk
import pyperclip


def copy_to_clipboard(entry):
    pyperclip.copy(entry.get())


def copy_position_size():
    position_size = position_size_label.cget("text").split(": ")[1]
    pyperclip.copy(position_size)


def calculate_position_size():
    account_balance = float(account_balance_entry.get())
    risk_percentage = float(risk_percentage_entry.get()) / 100
    entry_price = float(entry_price_entry.get())
    exit_price = float(exit_price_entry.get())
    stop_loss = float(stop_loss_entry.get())

    risk_amount = account_balance * risk_percentage
    dollar_risk_per_share = entry_price - stop_loss
    shares_to_buy = risk_amount / dollar_risk_per_share
    position_size = shares_to_buy * entry_price

    position_size_label.config(text=f"Position size: {position_size:.2f}")


root = tk.Tk()
root.title("Position Size Calculator")

account_balance_label = tk.Label(root, text="Account balance:")
account_balance_label.grid(row=0, column=0)

account_balance_entry = tk.Entry(root)
account_balance_entry.grid(row=0, column=1)

account_balance_copy_button = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(account_balance_entry))
account_balance_copy_button.grid(row=0, column=2)

risk_percentage_label = tk.Label(root, text="Risk percentage (%):")
risk_percentage_label.grid(row=1, column=0)

risk_percentage_entry = tk.Entry(root)
risk_percentage_entry.grid(row=1, column=1)

risk_percentage_copy_button = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(risk_percentage_entry))
risk_percentage_copy_button.grid(row=1, column=2)

entry_price_label = tk.Label(root, text="Entry price:")
entry_price_label.grid(row=2, column=0)

entry_price_entry = tk.Entry(root)
entry_price_entry.grid(row=2, column=1)

entry_price_copy_button = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(entry_price_entry))
entry_price_copy_button.grid(row=2, column=2)

exit_price_label = tk.Label(root, text="Exit price:")
exit_price_label.grid(row=3, column=0)

exit_price_entry = tk.Entry(root)
exit_price_entry.grid(row=3, column=1)

exit_price_copy_button = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(exit_price_entry))
exit_price_copy_button.grid(row=3, column=2)

stop_loss_label = tk.Label(root, text="Stop loss:")
stop_loss_label.grid(row=4, column=0)

stop_loss_entry = tk.Entry(root)
stop_loss_entry.grid(row=4, column=1)

stop_loss_copy_button = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(stop_loss_entry))
stop_loss_copy_button.grid(row=4, column=2)

calculate_button = tk.Button(root, text="Calculate", command=calculate_position_size)
calculate_button.grid(row=5, columnspan=3)

position_size_label = tk.Label(root, text="Position size ($): ")
position_size_label.grid(row=6, columnspan=2)

position_size_copy_button = tk.Button(root, text="Copy", command=copy_position_size)
position_size_copy_button.grid(row=6, column=2)

root.mainloop()
