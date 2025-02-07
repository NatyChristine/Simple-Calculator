import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap, QCursor, QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.numbers = QLabel("0", self)
        self.multi_button = QPushButton("*", self, clicked = lambda: self.on_click("*"))
        self.div_button = QPushButton("/", self, clicked = lambda: self.on_click("/"))
        self.equal_button = QPushButton("=", self, clicked = lambda: self.math())
        self.one = QPushButton("1", self, clicked = lambda: self.on_click("1"))
        self.two = QPushButton("2", self, clicked = lambda: self.on_click("2"))
        self.three = QPushButton("3", self, clicked = lambda: self.on_click("3"))
        self.four = QPushButton("4", self, clicked = lambda: self.on_click("4"))
        self.five = QPushButton("5", self, clicked = lambda: self.on_click("5"))
        self.six = QPushButton("6", self, clicked = lambda: self.on_click("6"))
        self.seven = QPushButton("7", self, clicked = lambda: self.on_click("7"))
        self.eight = QPushButton("8", self, clicked = lambda: self.on_click("8"))
        self.nine = QPushButton("9", self, clicked = lambda: self.on_click("9"))
        self.zero = QPushButton("0", self, clicked = lambda: self.on_click("0"))
        self.clear = QPushButton("C", self, clicked = lambda: self.on_click("C"))
        self.sub_button = QPushButton("-", self, clicked = lambda: self.on_click("-"))
        self.add_button = QPushButton("+", self, clicked = lambda: self.on_click("+"))
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Simple Calculator")
        self.setFixedSize(364, 567)
        self.setWindowIcon(QIcon("files\icon.png"))

        #layout menagement
        mainLayout = QVBoxLayout()
        display = QHBoxLayout()
        display.addWidget(self.numbers)
        row_1 = QHBoxLayout()
        row_1.addWidget(self.multi_button)
        row_1.addWidget(self.div_button)
        row_1.addWidget(self.equal_button)
        row_2 = QHBoxLayout()
        keyboard = QGridLayout()
        keyboard.addWidget(self.one, 0, 0)
        keyboard.addWidget(self.two, 0, 1)
        keyboard.addWidget(self.three, 0, 2)
        keyboard.addWidget(self.four, 1, 0)
        keyboard.addWidget(self.five, 1, 1)
        keyboard.addWidget(self.six, 1, 2)
        keyboard.addWidget(self.seven, 2, 0)
        keyboard.addWidget(self.eight, 2, 1)
        keyboard.addWidget(self.nine, 2, 2)
        keyboard.addWidget(self.zero, 3, 1)
        keyboard.addWidget(self.clear, 3, 2)
        row_2.addLayout(keyboard)
        buttons = QVBoxLayout()
        buttons.addWidget(self.sub_button)
        buttons.addWidget(self.add_button)
        row_2.addLayout(buttons)
        mainLayout.addLayout(display)
        mainLayout.addLayout(row_1)
        mainLayout.addLayout(row_2)
        self.setLayout(mainLayout)

        #setObjectName
        self.numbers.setObjectName("display")
        self.multi_button.setObjectName("multi")
        self.div_button.setObjectName("div")
        self.equal_button.setObjectName("equal")
        self.one.setObjectName("one")
        self.two.setObjectName("two")
        self.three.setObjectName("three")
        self.four.setObjectName("four")
        self.five.setObjectName("five")
        self.six.setObjectName("six")
        self.seven.setObjectName("seven")
        self.eight.setObjectName("eight")
        self.nine.setObjectName("nine")
        self.zero.setObjectName("zero")
        self.clear.setObjectName("clear")
        self.sub_button.setObjectName("sub")
        self.add_button.setObjectName("add")
        
        #styleSheet
        app.setStyleSheet("""
            Calculator {
                background-color: #D2B7DC;
            }
            QLabel#display {
                background: #C893DC;
                min-height: 170px;
                max-height: 170px;
                font-size: 80px;
                border-radius: 4px;
                text-align: right;
                margin: 5px;
            }
            QPushButton#multi, #div {
                height: 60px;
                background: #B449DC;
                font-size: 20px;
                color: #D2B7DC;
                border-radius: 4px;
            }
            QPushButton#equal {
                height: 60px;
                background: #B449DC;
                font-size: 20px;
                width: 40px;
                color: #D2B7DC;
                border-radius: 4px;
            }
            QPushButton#one, #two, #three, #four, #five, #six, #seven, #eight, #nine, #zero, #clear {
                height: 40px;
                font-size: 20px;
                background: #D2B7DC;
                border-radius: 4px;
            }
            QPushButton#sub, #add {
                height: 100px;
                font-size: 20px;
                background: #B449DC;
                color: #D2B7DC;
                border-radius: 4px;
                min-width: 60px;
                max-width: 60px;
            }
        """)
    
    def on_click(self, pressed):
        if pressed == "C":
            self.numbers.setText("0")
        else:
            if self.numbers.text() == "0":
                self.numbers.setText("")
            self.numbers.setText(f"{self.numbers.text()}{pressed:.2f}") 

    #operations
    def math(self):
        screen = self.numbers.text()
        result = eval(screen)
        self.numbers.setText(str(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())