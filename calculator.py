import sys
import math_lib
from math_lib import MathLib
from typing import Union
from PySide6.QtWidgets import QApplication, QMainWindow

from gui import Ui_MainWindow

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to functions
        self.ui.button_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.button_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.button_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.button_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.button_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.button_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.button_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.button_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.button_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.button_9.clicked.connect(lambda: self.add_digit('9'))

        # Connect operators to functions
        self.ui.button_clear.clicked.connect(lambda: self.clear_all_digits())
        self.ui.button_backspace.clicked.connect(lambda: self.clear_entry())
        self.ui.button_point.clicked.connect(lambda: self.add_point())


        # Connect math operators to functions
        self.ui.button_plus.clicked.connect(lambda: self.add_temprorary('+'))
        self.ui.button_minus.clicked.connect(lambda: self.add_temprorary('-'))
        self.ui.button_mul.clicked.connect(lambda: self.add_temprorary('x'))
        self.ui.button_div.clicked.connect(lambda: self.add_temprorary('/'))
        self.ui.button_sqr.clicked.connect(lambda: self.add_temprorary('^'))
        self.ui.button_sqrt.clicked.connect(lambda: self.add_temprorary('root'))
        self.ui.button_factorial.clicked.connect(lambda: self.add_temprorary('!'))
        #self.ui.button_.clicked.connect(lambda: self.add_temprorary('abs'))
        self.ui.button_go.clicked.connect(lambda: self.calculate())

        
    def add_digit(self, btn_text: str) -> None:
        if self.ui.line_entry.text() == '0':
            self.ui.line_entry.setText(btn_text)
        else:
            self.ui.line_entry.setText(self.ui.line_entry.text() + btn_text)
    
    def add_point(self) -> None:
        if '.' not in self.ui.line_entry.text():
            self.ui.line_entry.setText(self.ui.line_entry.text() + '.')
        
    def add_temprorary(self, math_operator: str) -> None:
        if self.ui.lbl_temp.text() == '':
            self.ui.lbl_temp.setText(f'{self.remove_zeroes(self.ui.line_entry.text())} {math_operator}')
            self.ui.line_entry.setText('0')
    
    def get_entry_number(self) -> Union[int, float]:
        entry_number = self.ui.line_entry.text().strip('.')
        return float(entry_number) if '.' in entry_number else int(entry_number)
    
    def get_temprorary_number(self) -> Union[int, float, None]:
        if self.ui.lbl_temp.text():
            temprorary_number = self.ui.lbl_temp.text().split()[0].strip('.')
            return float(temprorary_number) if '.' in temprorary_number else int(temprorary_number)
    
    def get_math_sign(self)-> Union[str, None]:
        if self.ui.lbl_temp.text():
            return self.ui.lbl_temp.text().split()[1]

    def clear_all_digits(self) -> None:
        self.ui.line_entry.setText('0')
        self.ui.lbl_temp.clear()

    def clear_entry(self) -> None:
        self.ui.line_entry.setText('0')

    @staticmethod
    def remove_zeroes(string: str) -> str:
        if '.' in string:
            return string.rstrip('0').rstrip('.')
        else:
            return string
    
    def calculate(self) -> Union[str, None]:
        if self.ui.lbl_temp.text():
            math_operator = self.get_math_sign()
            if math_operator == '+':
                result = MathLib.add(self.get_temprorary_number(), self.get_entry_number())
            elif math_operator == '-':
                result = MathLib.sub(self.get_temprorary_number(), self.get_entry_number())
            elif math_operator == 'x':
                result = MathLib.mul(self.get_temprorary_number(), self.get_entry_number())
            elif math_operator == '/':
                result = MathLib.div(self.get_temprorary_number(), self.get_entry_number())
            elif math_operator == '^':
                result = MathLib.pow(self.get_temprorary_number(), self.get_entry_number())
            elif math_operator == 'root':
                result = MathLib.root(self.get_temprorary_number(), self.get_entry_number())
            elif math_operator == '!':
                result = MathLib.fact(self.get_temprorary_number())
            self.ui.line_entry.setText(str(result))
            self.ui.lbl_temp.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())