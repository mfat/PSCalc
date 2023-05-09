import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import pyperclip

class PositionSizeCalculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Position Size Calculator")

        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)

        account_balance_label = QtWidgets.QLabel("Account balance:")
        grid.addWidget(account_balance_label, 0, 0)

        self.account_balance_entry = QtWidgets.QLineEdit()
        grid.addWidget(self.account_balance_entry, 0, 1)

        account_balance_copy_button = QtWidgets.QPushButton("Copy")
        account_balance_copy_button.clicked.connect(lambda: self.copy_to_clipboard(self.account_balance_entry))
        grid.addWidget(account_balance_copy_button, 0, 2)

        risk_percentage_label = QtWidgets.QLabel("Risk percentage (%):")
        grid.addWidget(risk_percentage_label, 1, 0)

        self.risk_percentage_entry = QtWidgets.QLineEdit()
        grid.addWidget(self.risk_percentage_entry, 1, 1)

        risk_percentage_copy_button = QtWidgets.QPushButton("Copy")
        risk_percentage_copy_button.clicked.connect(lambda: self.copy_to_clipboard(self.risk_percentage_entry))
        grid.addWidget(risk_percentage_copy_button, 1, 2)

        entry_price_label = QtWidgets.QLabel("Entry price:")
        grid.addWidget(entry_price_label, 2, 0)

        self.entry_price_entry = QtWidgets.QLineEdit()
        grid.addWidget(self.entry_price_entry, 2, 1)

        entry_price_copy_button = QtWidgets.QPushButton("Copy")
        entry_price_copy_button.clicked.connect(lambda: self.copy_to_clipboard(self.entry_price_entry))
        grid.addWidget(entry_price_copy_button, 2, 2)

        exit_price_label = QtWidgets.QLabel("Exit price:")
        grid.addWidget(exit_price_label, 3, 0)

        self.exit_price_entry = QtWidgets.QLineEdit()
        grid.addWidget(self.exit_price_entry, 3, 1)

        exit_price_copy_button = QtWidgets.QPushButton("Copy")
        exit_price_copy_button.clicked.connect(lambda: self.copy_to_clipboard(self.exit_price_entry))
        grid.addWidget(exit_price_copy_button, 3, 2)

        stop_loss_label = QtWidgets.QLabel("Stop loss:")
        grid.addWidget(stop_loss_label, 4, 0)

        self.stop_loss_entry = QtWidgets.QLineEdit()
        grid.addWidget(self.stop_loss_entry, 4, 1)

        stop_loss_copy_button = QtWidgets.QPushButton("Copy")
        stop_loss_copy_button.clicked.connect(lambda: self.copy_to_clipboard(self.stop_loss_entry))
        grid.addWidget(stop_loss_copy_button, 4, 2)

        calculate_button = QtWidgets.QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_position_size)
        grid.addWidget(calculate_button, 5, 0, 1, 3)

        self.position_size_label = QtWidgets.QLabel("Position size: ")
        grid.addWidget(self.position_size_label, 6, 0, 1, 2)

        position_size_copy_button = QtWidgets.QPushButton("Copy")
        position_size_copy_button.clicked.connect(self.copy_position_size)
        grid.addWidget(position_size_copy_button, 6, 2)

    def copy_to_clipboard(self, entry):
        pyperclip.copy(entry.text())

    def copy_position_size(self):
        position_size = self.position_size_label.text().split(": ")[1]
        pyperclip.copy("{:.2f}".format(float(position_size)))

    def calculate_position_size(self):
        account_balance = float(self.account_balance_entry.text())
        risk_percentage = float(self.risk_percentage_entry.text()) / 100
        entry_price = float(self.entry_price_entry.text())
        exit_price = float(self.exit_price_entry.text())
        stop_loss = float(self.stop_loss_entry.text())
        position_size = (account_balance * risk_percentage) / (entry_price - stop_loss)
        self.position_size_label.setText(f"Position size: {position_size:.2f}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PositionSizeCalculator()
    window.show()
    sys.exit(app.exec_())
