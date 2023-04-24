import sys
import math_lib
from math_lib import MathLib
from typing import Union
from PySide6.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap

from ui import Ui_MainWindow

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
        self.ui.button_module.clicked.connect(lambda: self.add_temprorary('|x|'))
        self.ui.button_procent.clicked.connect(lambda: self.add_temprorary('%'))
        self.ui.button_go.clicked.connect(lambda: self.calculate())
        
    # Functions

    # Function for adding digits to the entry line
    def add_digit(self, btn_text: str) -> None:
        if self.ui.line_entry.text() == '0':
            self.ui.line_entry.setText(btn_text)
        else:
            self.ui.line_entry.setText(self.ui.line_entry.text() + btn_text)

    # Function for adding point to the entry line
    def add_point(self) -> None:
        if '.' not in self.ui.line_entry.text():
            self.ui.line_entry.setText(self.ui.line_entry.text() + '.')
        
    # Function for adding temprorary number and math operator    
    def add_temprorary(self, math_operator: str) -> None:
        if self.ui.lbl_temp.text() == '':
            self.ui.lbl_temp.setText(f'{self.remove_zeroes(self.ui.line_entry.text())} {math_operator}')
            self.ui.line_entry.setText('0')
    
    # Function for getting entry number from the entry line
    def get_second_number(self) -> Union[int, float]:
        entry_number = self.ui.line_entry.text().strip('.')
        return float(entry_number) if '.' in entry_number else int(entry_number)
    
    # Function for getting temprorary number from the temprorary line
    def get_first_number(self) -> Union[int, float, None]:
        if self.ui.lbl_temp.text():
            temprorary_number = self.ui.lbl_temp.text().split()[0].strip('.')
            return float(temprorary_number) if '.' in temprorary_number else int(temprorary_number)
    
    # Function for getting math operator from the temprorary line
    def get_math_sign(self)-> Union[str, None]:
        if self.ui.lbl_temp.text():
            return self.ui.lbl_temp.text().split()[1]
    
    # Function for clearing entry line and temprorary line
    def clear_all_digits(self) -> None:
        self.ui.line_entry.setText('0')
        self.ui.lbl_temp.clear()

    # Function for clearing entry line
    def clear_entry(self) -> None:
        self.ui.line_entry.setText('0')

    # Static method for math operations and removing zeroes
    @staticmethod
    def remove_zeroes(string: str) -> str:
        if '.' in string: # If string has a point
            return string.rstrip('0').rstrip('.') # Remove zeroes and point if they are at the end of the string
        else:
            return string # If string has no point, return it as it is
    
    # Main function for math operations
    def calculate(self) -> Union[str, None]:
        if self.ui.lbl_temp.text():
            math_operator = self.get_math_sign()
            if math_operator == '+':
                result = MathLib.add(self.get_first_number(), self.get_second_number())
            elif math_operator == '-':
                result = MathLib.sub(self.get_first_number(), self.get_second_number())
            elif math_operator == 'x':
                result = MathLib.mul(self.get_first_number(), self.get_second_number())
            elif math_operator == '/':
                if(self.get_second_number() == 0):
                    self.ui.line_entry.setText('Error! Divide 0!')
                    self.ui.lbl_temp.clear()
                    return
                else:
                    result = MathLib.div(self.get_first_number(), self.get_second_number())
            elif math_operator == '^':
                if(self.get_first_number() == 0 and self.get_second_number() == 0):
                    self.ui.line_entry.setText('Error! 0^0!')
                    self.ui.lbl_temp.clear()
                    return
                else:
                    result = MathLib.pow(self.get_first_number(), self.get_second_number())
            elif math_operator == 'root':
                if(self.get_first_number() < 0):
                    self.ui.line_entry.setText('Error! root(-x)!')
                    self.ui.lbl_temp.clear()
                    return
                if(self.get_second_number() == 0):
                    self.ui.line_entry.setText('Err! root(x,0)!')
                    self.ui.lbl_temp.clear()
                    return
                else:
                    result = MathLib.root(self.get_first_number(), self.get_second_number())
            elif math_operator == '!':
                if(self.get_first_number() < 0):
                    self.ui.line_entry.setText('Error! fact(-x)!')
                    self.ui.lbl_temp.clear()
                    return
                if(self.get_first_number() != int(self.get_first_number())): 
                    self.ui.line_entry.setText('Error! fact(x.y)!')
                    self.ui.lbl_temp.clear()
                    return
                else:
                    result = MathLib.fact(self.get_first_number())
            elif math_operator == '|x|':
                result = MathLib.abs(self.get_first_number())
            elif math_operator == '%':
                if(self.get_first_number() == 0):
                    self.ui.line_entry.setText('Error! x%0!')
                    self.ui.lbl_temp.clear()
                    return
                if(self.get_second_number() == 0):
                    self.ui.line_entry.setText('Error! 0''%''x!')
                    self.ui.lbl_temp.clear()
                    return
                else:
                    result = MathLib.mod(self.get_first_number(), self.get_second_number())
            self.ui.line_entry.setText(str(result))
            self.ui.line_entry.setText(self.remove_zeroes(self.ui.line_entry.text()))
            self.ui.lbl_temp.clear()

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())