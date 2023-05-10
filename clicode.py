def calculate_position_size(self):
    account_balance = float(self.account_balance_field.text())
    risk_pct_str = self.risk_pct_field.text()
    if risk_pct_str.endswith('%'):
        risk_pct_str = risk_pct_str[:-1]
    risk_pct = float(risk_pct_str) / 100
    entry_price = float(self.entry_price_field.text())
    exit_price = float(self.exit_price_field.text())
    stop_loss_price = float(self.stop_loss_price_field.text())

    risk_amt = account_balance * risk_pct
    risk_per_share = entry_price - stop_loss_price
    position_size = round(risk_amt / risk_per_share, 2)

    self.result_label.setText(f"Position size: {position_size}")
