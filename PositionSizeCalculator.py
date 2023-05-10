import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import pyperclip

class PositionSizeCalculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Position Size Calculator by mFat")

        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)

        account_balance_label = QtWidgets.QLabel("Account balance:")
        grid.addWidget(account_balance_label, 0, 0)

        self.account_balance_entry = QtWidgets.QLineEdit()
        grid.addWidget(self.account_balance_entry, 0, 1)

        account_balance_copy_button = QtWidgets.QPushButton("Copy")
        account_balance_copy_button.clicked.connect(lambda: self.copy_to_clipboard(self.account_balance_entry))
        grid.addWidget(account_balance_copy_button, 0, 2)

        account_balance_paste_button = QtWidgets.QPushButton("Paste")
        account_balance_paste_button.clicked.connect(lambda: self.paste_entry_from_clipboard(self.account_balance_entry))
        grid.addWidget(account_balance_paste_button, 0, 3)


        account_balance_clear_button = QtWidgets.QPushButton("Clear")
        account_balance_clear_button.clicked.connect(self.account_balance_entry.clear)
        grid.addWidget(account_balance_clear_button, 0, 4)


        risk_percentage_label = QtWidgets.QLabel("Risk percentage (%):")
        grid.addWidget(risk_percentage_label, 1, 0)

        self.risk_percentage_entry = QtWidgets.QLineEdit()
        grid.addWidget(self.risk_percentage_entry, 1, 1)

        risk_percentage_copy_button = QtWidgets.QPushButton("Copy")
        risk_percentage_copy_button.clicked.connect(lambda: self.copy_to_clipboard(self.risk_percentage_entry))
        grid.addWidget(risk_percentage_copy_button, 1, 2)

        risk_percentage_paste_button = QtWidgets.QPushButton("Paste")
        risk_percentage_paste_button.clicked.connect(lambda: self.paste_entry_from_clipboard(self.risk_percentage_entry))
        grid.addWidget(risk_percentage_paste_button, 1, 3)

        risk_percentage_clear_button = QtWidgets.QPushButton("Clear")
        risk_percentage_clear_button.clicked.connect(self.risk_percentage_entry.clear)
        grid.addWidget(risk_percentage_clear_button, 1, 4)

        entry_price_label = QtWidgets.QLabel("Entry price:")
        grid.addWidget(entry_price_label, 2, 0)

        self.entry_price_entry = QtWidgets.QLineEdit()
        grid.addWidget(self.entry_price_entry, 2, 1)

        entry_price_copy_button = QtWidgets.QPushButton("Copy")
        entry_price_copy_button.clicked.connect(lambda: self.copy_to_clipboard(self.entry_price_entry))
        grid.addWidget(entry_price_copy_button, 2, 2)

        entry_price_paste_button = QtWidgets.QPushButton("Paste")
        entry_price_paste_button.clicked.connect(lambda: self.paste_entry_from_clipboard(self.entry_price_entry))
        grid.addWidget(entry_price_paste_button, 2, 3)

        entry_price_clear_button = QtWidgets.QPushButton("Clear")
        entry_price_clear_button.clicked.connect(self.entry_price_entry.clear)
        grid.addWidget(entry_price_clear_button, 2, 4)


        exit_price_label = QtWidgets.QLabel("Exit price (Optional):")
        grid.addWidget(exit_price_label, 3, 0)

        self.exit_price_entry = QtWidgets.QLineEdit()
        grid.addWidget(self.exit_price_entry, 3, 1)

        exit_price_copy_button = QtWidgets.QPushButton("Copy")
        exit_price_copy_button.clicked.connect(lambda: self.copy_to_clipboard(self.exit_price_entry))
        grid.addWidget(exit_price_copy_button, 3, 2)

        exit_price_paste_button = QtWidgets.QPushButton("Paste")
        exit_price_paste_button.clicked.connect(lambda: self.paste_entry_from_clipboard(self.exit_price_entry))
        grid.addWidget(exit_price_paste_button, 3, 3)

        exit_price_clear_button = QtWidgets.QPushButton("Clear")
        exit_price_clear_button.clicked.connect(self.exit_price_entry.clear)
        grid.addWidget(exit_price_clear_button, 3, 4)

        stop_loss_label = QtWidgets.QLabel("Stop loss:")
        grid.addWidget(stop_loss_label, 4, 0)

        self.stop_loss_entry = QtWidgets.QLineEdit()
        grid.addWidget(self.stop_loss_entry, 4, 1)

        stop_loss_copy_button = QtWidgets.QPushButton("Copy")
        stop_loss_copy_button.clicked.connect(lambda: self.copy_to_clipboard(self.stop_loss_entry))
        grid.addWidget(stop_loss_copy_button, 4, 2)

        stop_loss_paste_button = QtWidgets.QPushButton("Paste")
        stop_loss_paste_button.clicked.connect(lambda: self.paste_entry_from_clipboard(self.stop_loss_entry))
        grid.addWidget(stop_loss_paste_button, 4, 3)

        stop_loss_clear_button = QtWidgets.QPushButton("Clear")
        stop_loss_clear_button.clicked.connect(self.stop_loss_entry.clear)
        grid.addWidget(stop_loss_clear_button, 4, 4)

        profit_label = QtWidgets.QLabel("Profit ($): ")
        grid.addWidget(profit_label, 5, 0, 1, 2)

        self.profit_value_label = QtWidgets.QLabel("")
        grid.addWidget(self.profit_value_label, 5, 2, 1, 2)

        loss_label = QtWidgets.QLabel("Loss ($): ")
        grid.addWidget(loss_label, 6, 0, 1, 2)

        self.loss_value_label = QtWidgets.QLabel("")
        grid.addWidget(self.loss_value_label, 6, 2, 1, 2)

        calculate_button = QtWidgets.QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_position_size)
        grid.addWidget(calculate_button, 7, 0, 1, 3)


        self.position_size_label = QtWidgets.QLabel("Position size: ")
        grid.addWidget(self.position_size_label, 8, 0, 1, 2)

        position_size_copy_button = QtWidgets.QPushButton("Copy")
        position_size_copy_button.clicked.connect(self.copy_position_size)
        grid.addWidget(position_size_copy_button, 8, 2)

        self.position_size_usd_label = QtWidgets.QLabel("Position size (USD): ")
        grid.addWidget(self.position_size_usd_label, 9, 0, 1, 2)

        position_size_copy_button_usd = QtWidgets.QPushButton("Copy")
        position_size_copy_button_usd.clicked.connect(self.copy_position_size_usd)
        grid.addWidget(position_size_copy_button_usd, 9, 2)

        # About button
        about_button = QtWidgets.QPushButton("About")
        about_button.setMaximumSize(50,20)
        about_button.setMinimumSize(50,20)
        about_button.clicked.connect(self.show_about_dialog)
        grid.addWidget(about_button, 9, 5)




    def copy_to_clipboard(self, entry):
        pyperclip.copy(entry.text())

    def paste_entry_from_clipboard(self, entry):
        text = pyperclip.paste()
        entry.setText(text)

    def copy_position_size(self):
        position_size = self.position_size_label.text().split(": ")[1]
        pyperclip.copy("{:.2f}".format(float(position_size)))

    def copy_position_size_usd(self):
        position_size_usd = self.position_size_usd_label.text().split(": ")[1]
        pyperclip.copy("{:.2f}".format(float(position_size_usd)))

    def calculate_position_size(self):
        account_balance = float(self.account_balance_entry.text())
        risk_percentage = float(self.risk_percentage_entry.text()) / 100
        entry_price = float(self.entry_price_entry.text())
        stop_loss = float(self.stop_loss_entry.text())

        if self.exit_price_entry.text() != "":
            exit_price = float(self.exit_price_entry.text())
            position_size = min((account_balance * risk_percentage) / abs(stop_loss - entry_price),
                                (account_balance * risk_percentage) / abs(exit_price - entry_price))
            profit = abs(exit_price - entry_price) * position_size
            loss = abs(stop_loss - entry_price) * position_size
            position_size_usd = position_size * entry_price
            self.position_size_label.setText(f"Position size: {position_size:.2f}")
            self.position_size_usd_label.setText(f"Position size (USD): {position_size_usd:.2f}")
            self.profit_value_label.setText(f"{profit:.2f}")
            self.loss_value_label.setText(f"{loss:.2f}")
        else:
            position_size = abs((account_balance * risk_percentage) / (entry_price - stop_loss))
            position_size_usd = position_size * entry_price
            self.position_size_label.setText(f"Position size: {position_size:.2f}")
            self.position_size_usd_label.setText(f"Position size (USD): {position_size_usd:.2f}")
            self.profit_value_label.setText("")
            self.loss_value_label.setText("")

    def show_about_dialog(self):
        author_url = "<a href='https://github.com/mfat/qtpositioncalc'>https://github.com/mfat/qtpositioncalc</a>"
        QtWidgets.QMessageBox.about(
            self, "About Position Size Calculator",
            f"<p>This app was created by mFat using PyQt5. Check out the code on GitHub:</p><p align='center'>{author_url}</p>"
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PositionSizeCalculator()
    window.show()
    sys.exit(app.exec_())
