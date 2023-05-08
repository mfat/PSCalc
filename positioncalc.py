# Get user input
account_balance = float(input("Enter your account balance: "))
risk_pct = float(input("Enter your risk percentage (as a decimal): "))
entry_price = float(input("Enter your entry price: "))
exit_price = float(input("Enter your exit price: "))
stop_loss_price = float(input("Enter your stop loss price: "))

# Calculate position size
risk_amt = account_balance * risk_pct
risk_per_share = entry_price - stop_loss_price
position_size = round(risk_amt / risk_per_share, 2)

# Print results
print("Position size: ", position_size)
