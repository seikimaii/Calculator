from PySide2.QtCore import QRect, QCoreApplication, QMetaObject
from PySide2.QtGui import QFont, Qt
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QButtonGroup, QLineEdit


button_style = '''QPushButton {color: rgb(0, 0, 0);
                            background: rgba(126, 198, 224, 1);
                            border: 2px;
                            border-radius: 8px;
                            
                            }
            QPushButton:hover {
                                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                stop: 0 rgba(46, 138, 240, 0.5), stop: 1 rgba(46, 138, 240, 1));
                                }
            QPushButton:pressed {
                                background: qlineargradient(x1: 0.1, y1: 0.3, x2: 0.5, y2: 0.5,
                                stop: 0 rgba(30, 122, 220, 0.5), stop: 1 rgba(30, 122, 220, 1));
                                border: 2px;
                                border-radius: 8px;
                                
                                }
            '''

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle("Calculator")

        font = QFont()
        font.setPointSize(23)        

        GridLayout = QGridLayout()
        GridLayout.setObjectName(u"gridLayout")
        GridLayout.setContentsMargins(2, 2, 2, 5)
        GridLayout.setMargin(5)


        self.negative = QPushButton()
        self.negative.setObjectName(u"negative")
        self.negative.setText("\u00b1")
        self.negative.setStyleSheet(button_style)
        self.negative.setFont(font)

        self.zero = QPushButton()
        self.zero.setObjectName(u"zero")
        self.zero.setText("0")
        self.zero.setStyleSheet(button_style)
        self.zero.setFont(font)

        self.one = QPushButton()
        self.one.setObjectName(u"one")
        self.one.setText("1")
        self.one.setStyleSheet(button_style)
        self.one.setFont(font)

        self.two = QPushButton()
        self.two.setObjectName(u"two")
        self.two.setText("2")
        self.two.setStyleSheet(button_style)
        self.two.setFont(font)

        self.three = QPushButton()
        self.three.setObjectName(u"three")
        self.three.setText("3")
        self.three.setStyleSheet(button_style)
        self.three.setFont(font)

        self.four = QPushButton()
        self.four.setObjectName(u"four")
        self.four.setText("4")
        self.four.setStyleSheet(button_style)
        self.four.setFont(font)

        self.five = QPushButton()
        self.five.setObjectName(u"five")
        self.five.setText("5")
        self.five.setStyleSheet(button_style)
        self.five.setFont(font)

        self.six = QPushButton()
        self.six.setObjectName(u"six")
        self.six.setText("6")
        self.six.setStyleSheet(button_style)
        self.six.setFont(font)

        self.seven = QPushButton()
        self.seven.setObjectName(u"seven")
        self.seven.setText("7")
        self.seven.setStyleSheet(button_style)
        self.seven.setFont(font)

        self.eight = QPushButton()
        self.eight.setObjectName(u"eight")
        self.eight.setText("8")
        self.eight.setStyleSheet(button_style)
        self.eight.setFont(font)

        self.nine = QPushButton()
        self.nine.setObjectName(u"nine")
        self.nine.setText("9")
        self.nine.setStyleSheet(button_style)
        self.nine.setFont(font)

        self.plus = QPushButton()
        self.plus.setObjectName(u"plus")
        self.plus.setText("+")
        self.plus.setStyleSheet(button_style)
        self.plus.setFont(font)

        self.minus = QPushButton()
        self.minus.setObjectName(u"minus")
        self.minus.setText("–")
        self.minus.setStyleSheet(button_style)
        self.minus.setFont(font)

        self.multi = QPushButton()
        self.multi.setObjectName(u"multi")
        self.multi.setText("\u00d7")
        self.multi.setStyleSheet(button_style)
        self.multi.setFont(font)

        self.divide = QPushButton()
        self.divide.setObjectName(u"divide")
        self.divide.setText("\u00f7")
        self.divide.setStyleSheet(button_style)
        self.divide.setFont(font)

        self.percent = QPushButton()
        self.percent.setObjectName(u"percent")
        self.percent.setText("%")
        self.percent.setStyleSheet(button_style)
        self.percent.setFont(font)

        self.clear = QPushButton()
        self.clear.setObjectName(u"clear")
        self.clear.setText("C")
        self.clear.setStyleSheet('''QPushButton {color: rgb(0, 0, 0);
                                                background: rgba(220, 0, 51, 1);
                                                border: 2px;
                                                border-radius: 8px;
                                                
                                                }
                                    QPushButton:hover {
                                                        background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                                        stop: 0 rgba(244, 25, 70, 0.5), stop: 1 rgba(244, 25, 70, 1));
                                                        }
                                    QPushButton:pressed {
                                                        background: qlineargradient(x1: 0.1, y1: 0.3, x2: 0.5, y2: 0.5,
                                                        stop: 0 rgba(178, 25, 71, 0.5), stop: 1 rgba(178, 25, 71, 1));
                                                        border: 2px;
                                                        border-radius: 8px;
                                                        
                                                        }
                                    ''')
        self.clear.setFont(font)

        self.clear_error = QPushButton()
        self.clear_error.setObjectName(u"clear_error")
        self.clear_error.setText("CE")
        self.clear_error.setStyleSheet('''QPushButton {color: rgb(0, 0, 0);
                                                        background: rgba(220, 0, 51, 1);
                                                        border: 2px;
                                                        border-radius: 8px;
                                                        
                                                        }
                                            QPushButton:hover {
                                                                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                                                stop: 0 rgba(244, 25, 70, 0.5), stop: 1 rgba(244, 25, 70, 1));
                                                                }
                                            QPushButton:pressed {
                                                                background: qlineargradient(x1: 0.1, y1: 0.3, x2: 0.5, y2: 0.5,
                                                                stop: 0 rgba(178, 25, 71, 0.5), stop: 1 rgba(178, 25, 71, 1));
                                                                border: 2px;
                                                                border-radius: 8px;
                                                                
                                                                }
                                            ''')
        self.clear_error.setFont(font)

        self.back = QPushButton()
        self.back.setObjectName(u"back")
        self.back.setText("Back")
        self.back.setStyleSheet('''QPushButton {color: rgb(0, 0, 0);
                                                background: rgba(126, 198, 224, 1);
                                                border: 2px;
                                                border-radius: 8px;
                                                
                                                }
                                    QPushButton:hover {
                                                        background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                                        stop: 0 rgba(46, 138, 240, 0.5), stop: 1 rgba(46, 138, 240, 1));
                                                        }
                                    QPushButton:pressed {
                                                        background: qlineargradient(x1: 0.1, y1: 0.3, x2: 0.5, y2: 0.5,
                                                        stop: 0 rgba(30, 122, 220, 0.5), stop: 1 rgba(30, 122, 220, 1));
                                                        border: 2px;
                                                        border-radius: 8px;
                                                        
                                                        }
                                    ''')
        self.back.setFont(font)

        self.equal = QPushButton()
        self.equal.setObjectName(u"equal")
        self.equal.setText("=")
        self.equal.setStyleSheet('''QPushButton {color: rgb(0, 0, 0);
                                                    background: rgba(26, 119, 107, 1);
                                                    border: 2px;
                                                    border-radius: 8px;
                                                    
                                                    }
                                    QPushButton:hover {
                                                        background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                                        stop: 0 rgba(26, 147, 128, 0.5), stop: 1 rgba(26, 147, 128, 1));
                                                        }
                                    QPushButton:pressed {
                                                        background: qlineargradient(x1: 0.1, y1: 0.3, x2: 0.5, y2: 0.5,
                                                        stop: 0 rgba(6, 92, 61, 0.5), stop: 1 rgba(6, 92, 61, 1));
                                                        border: 2px;
                                                        border-radius: 8px;
                                                        
                                                        }
                                    ''')
        self.equal.setFont(font)

        self.dot = QPushButton()
        self.dot.setObjectName(u"dot")
        self.dot.setText(".")
        self.dot.setStyleSheet(button_style)
        self.dot.setFont(font)


        font.setPointSize(60)

        # self.Blabel = QLabel()
        self.Blabel = QLineEdit()
        self.Blabel.setObjectName(u"BLabel")
        self.Blabel.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.Blabel.setText("0")
        self.Blabel.setFont(font)
        self.Blabel.setContentsMargins(1, 1, 10, 1)
        self.Blabel.setReadOnly(True)
        self.Blabel.setMaxLength(12)
        # self.Blabel.setLineWidth(50)



        font.setPointSize(30)
        self.slabel = QLabel()
        self.slabel.setObjectName("sLabel")
        self.slabel.setText("")
        self.slabel.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.slabel.setFont(font)

        GridLayout.addWidget(self.five, 5, 1, 1, 1)
        GridLayout.addWidget(self.percent, 3, 0, 1, 1)
        GridLayout.addWidget(self.clear, 3, 2, 1, 1)
        GridLayout.addWidget(self.back, 2, 3, 1, 1)
        GridLayout.addWidget(self.divide, 3, 3, 1, 1)
        GridLayout.addWidget(self.minus, 5, 3, 1, 1)
        GridLayout.addWidget(self.zero, 7, 1, 1, 1)
        GridLayout.addWidget(self.two, 6, 1, 1, 1)
        GridLayout.addWidget(self.clear_error, 3, 1, 1, 1)
        GridLayout.addWidget(self.multi, 4, 3, 1, 1)
        GridLayout.addWidget(self.equal, 7, 3, 1, 1)
        GridLayout.addWidget(self.eight, 4, 1, 1, 1)
        GridLayout.addWidget(self.dot, 7, 2, 1, 1)
        GridLayout.addWidget(self.negative, 7, 0, 1, 1)
        GridLayout.addWidget(self.six, 5, 2, 1, 1)
        GridLayout.addWidget(self.plus, 6, 3, 1, 1)
        GridLayout.addWidget(self.nine, 4, 2, 1, 1)
        GridLayout.addWidget(self.three, 6, 2, 1, 1)
        GridLayout.addWidget(self.seven, 4, 0, 1, 1)
        GridLayout.addWidget(self.four, 5, 0, 1, 1)
        GridLayout.addWidget(self.one, 6, 0, 1, 1)
        GridLayout.addWidget(self.Blabel, 1, 0, 1, 4)
        GridLayout.addWidget(self.slabel, 0, 2, 1, 2)

        # GridLayout.setRowStretch(0, 3)
        # GridLayout.setRowStretch(1, 1)
        # GridLayout.setRowStretch(2, 1)
        # GridLayout.setRowStretch(3, 1)
        # GridLayout.setRowStretch(4, 1)
        # GridLayout.setRowStretch(5, 1)
        # GridLayout.setRowStretch(6, 1)
        # self.setFont(font)
        self.setLayout(GridLayout)
        
        self.btngrp_number = QButtonGroup()
        self.btngrp_operator = QButtonGroup()
        self.btngrp_attr = QButtonGroup()
        
        for btn in [self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, \
                    self.eight, self.nine]:
            
            self.btngrp_number.addButton(btn)

        for btn in [self.plus, self.minus, self.multi, self.divide]:
            self.btngrp_operator.addButton(btn)
        
        # for btn in [self.equal, self.clear, self.clear_error, self.back]:
            # self.btngrp_function.addButton(btn)
        
        for btn in [self.dot, self.percent, self.negative]:
            self.btngrp_attr.addButton(btn)

        self.back.clicked.connect(self.Back)
        self.clear.clicked.connect(self.Clear)
        self.equal.clicked.connect(self.Equal)

        self.temp_btn = ''
        self.btngrp_attr.buttonClicked.connect(self.changeAttr)
        self.btngrp_operator.buttonClicked.connect(self.operate)
        self.btngrp_number.buttonClicked.connect(self.num)

    def changeAttr(self, btn):
        print(btn.objectName())

    def Back(self):
        
        curr_text = self.Blabel.text()

        if self.temp_btn == self.equal:
            self.slabel = ""
            self.Blabel.setText('0')
        else:

            if len(curr_text) > 1:
                self.Blabel.setText(curr_text[1:])

            elif curr_text != '0':
                self.Blabel.setText('0')
        
        self.temp_btn = self.back

    def Clear(self):
        self.slabel.setText("")
        self.Blabel.setText('0')
        self.temp_btn = None
        

    def Equal(self):
        
        temp_text = self.slabel.text() + ' ' + self.Blabel.text()
        num1, op, num2 = temp_text.split(' ')

        if num1.isnumeric():
            num1 = int(num1)
        else:
            num1 = float(num1)
        
        if num2.isnumeric():
            num2 = int(num2)
        else:
            num2 = float(num2)

        ret = 0
        if op == "+":
            ret = num1 + num2
        elif op == "–":
            ret = num1 - num2
        elif op == "×":
            ret = num1 * num2
        else:
            ret = num1 / num2
            if ret == round(ret):
                ret = round(ret)
            else:
                pass
        
        self.Blabel.setText(f"{ret}")
        self.slabel.setText(f"{num1} {op} {num2} =")
        self.temp_btn = self.equal
    
    def operate(self, btn):
        
        curr_text = self.Blabel.text()
        self.slabel.setText(curr_text + " " + btn.text())

        self.temp_btn = btn
        
        
        
    
    def num(self, btn):
        # 1 空白時 -> 直接往後加
        # 2 按過數字 -> 直接往後加
        # 3 按過op -> 如果同一個數字:忽略, 如果不同數字,取代
        # 4 按過 =
        
        number = btn.text()
        curr_text = self.Blabel.text()
        


        if not self.temp_btn or curr_text == '0':
            self.Blabel.setText(number)
            self.temp_btn = btn

        elif self.temp_btn == self.equal:
            self.Clear()
            self.temp_btn = btn

            self.Blabel.setText(number)

        elif self.temp_btn.text() != '0' and self.temp_btn.text().isdigit():
            
            self.Blabel.setText(curr_text+number)
            self.temp_btn = btn

        else:
            if curr_text == number:
                self.temp_btn = None
            else:
                self.Blabel.setText(number)
                self.temp_btn = btn
    
    
    def infix_to_postfix(self, infix_expression):
        precedence = {"+": 1, "–": 1, "×": 2, "÷": 2} #+–×÷
        postfix = []
        stack = []

        for token in infix_expression:
            if token.isdigit():
                postfix.append(token)
            elif token in precedence:
                while stack and stack[-1] in precedence and precedence[token] <= precedence[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(token)
            elif token == "(":
                stack.append(token)
            elif token == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()

        while stack:
            postfix.append(stack.pop())

        return postfix

    def evaluate_postfix(self, postfix_expression):
        stack = []

        for token in postfix_expression:
            
            if token in "+-*/":
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == "+":
                    stack.append(operand1 + operand2)
                elif token == "-":
                    stack.append(operand1 - operand2)
                elif token == "*":
                    stack.append(operand1 * operand2)
                elif token == "/":
                    stack.append(operand1 / operand2)
            else:
                try:
                    token = int(token)
                except:
                    token = float(token)
                stack.append(token)

        return stack[0]


    
if __name__ == "__main__":
    import sys
    app = QApplication()

    # win = QWidget()
    ui = MainWindow()
    # ui.setupUi(win)

    ui.show()
    
    sys.exit(app.exec_())

