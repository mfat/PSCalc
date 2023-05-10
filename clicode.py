# Import decimal module for precision arithmetic
from decimal import Decimal, ROUND_HALF_UP

# Ask for user input
balance = Decimal(input("Enter account balance: "))
risk_percent = Decimal(input("Enter risk percentage (as percentage): ")) / 100
entry_price = Decimal(input("Enter entry price: "))
exit_price = Decimal(input("Enter exit price: "))
stop_loss_price = Decimal(input("Enter stop loss price: "))

# Calculate position size
risk_amount = balance * risk_percent
risk_per_share = entry_price - stop_loss_price
position_size = risk_amount / risk_per_share

# Round position size to two decimal places
position_size = position_size.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

# Print result
print("Position size:", position_size)
 
