import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PositionSizeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('mFat Position Size Calculator')
        self.resize(300, 200)

        # create labels and input fields
        self.account_balance_label = QLabel('Account Balance:')
        self.account_balance_field = QLineEdit()
        self.risk_pct_label = QLabel('Risk Percentage:')
        self.risk_pct_field = QLineEdit()
        self.entry_price_label = QLabel('Entry Price:')
        self.entry_price_field = QLineEdit()
        self.exit_price_label = QLabel('Exit Price:')
        self.exit_price_field = QLineEdit()
        self.stop_loss_price_label = QLabel('Stop Loss Price:')
        self.stop_loss_price_field = QLineEdit()

        # create calculate button
        self.calculate_button = QPushButton('Calculate Position Size')
        self.calculate_button.clicked.connect(self.calculate_position_size)

        # create result label
        self.result_label = QLabel()

        # create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.account_balance_label)
        layout.addWidget(self.account_balance_field)
        layout.addWidget(self.risk_pct_label)
        layout.addWidget(self.risk_pct_field)
        layout.addWidget(self.entry_price_label)
        layout.addWidget(self.entry_price_field)
        layout.addWidget(self.exit_price_label)
        layout.addWidget(self.exit_price_field)
        layout.addWidget(self.stop_loss_price_label)
        layout.addWidget(self.stop_loss_price_field)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = PositionSizeCalculator()
    calculator.show()
    sys.exit(app.exec_())
