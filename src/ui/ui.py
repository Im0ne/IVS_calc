# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 769)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/calculator_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 50%;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    width: 100%;\n"
"   height: 100%;\n"
"    font-size: 25px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"\n"
"")
        MainWindow.setProperty("background", "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_temp = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet("color: #888;\n"
"font-size: 25px;\n"
"height: 50px;\n"
"margin-top: 8px;")
        self.lbl_temp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_temp.setObjectName("lbl_temp")
        self.verticalLayout.addWidget(self.lbl_temp)
        self.line_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.line_entry.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_entry.sizePolicy().hasHeightForWidth())
        self.line_entry.setSizePolicy(sizePolicy)
        self.line_entry.setStyleSheet("font-size: 60px;\n"
"border: none;\n"
"text-alight: right;\n"
"")
        self.line_entry.setMaxLength(16)
        self.line_entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_entry.setReadOnly(True)
        self.line_entry.setObjectName("line_entry")
        self.verticalLayout.addWidget(self.line_entry)
        self.buttons = QtWidgets.QGridLayout()
        self.buttons.setContentsMargins(-1, 9, -1, -1)
        self.buttons.setObjectName("buttons")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_clear.sizePolicy().hasHeightForWidth())
        self.button_clear.setSizePolicy(sizePolicy)
        self.button_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_clear.setStyleSheet("*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"    background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"    background-color: #FBFBFB;\n"
"}")
        self.button_clear.setObjectName("button_clear")
        self.buttons.addWidget(self.button_clear, 0, 0, 1, 1)
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_1.setStyleSheet("*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")
        self.button_1.setObjectName("button_1")
        self.buttons.addWidget(self.button_1, 3, 0, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_2.setStyleSheet("*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")
        self.button_2.setObjectName("button_2")
        self.buttons.addWidget(self.button_2, 3, 1, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_8.setStyleSheet("*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")
        self.button_8.setObjectName("button_8")
        self.buttons.addWidget(self.button_8, 1, 1, 1, 1)
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_3.setStyleSheet("*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")
        self.button_3.setObjectName("button_3")
        self.buttons.addWidget(self.button_3, 3, 2, 1, 1)
        self.button_backspace = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_backspace.sizePolicy().hasHeightForWidth())
        self.button_backspace.setSizePolicy(sizePolicy)
        self.button_backspace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_backspace.setStyleSheet("*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"    background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"    background-color: #FBFBFB;\n"
"}")
        self.button_backspace.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/backspace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_backspace.setIcon(icon1)
        self.button_backspace.setIconSize(QtCore.QSize(40, 40))
        self.button_backspace.setObjectName("button_backspace")
        self.buttons.addWidget(self.button_backspace, 0, 1, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_6.setStyleSheet("*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")
        self.button_6.setObjectName("button_6")
        self.buttons.addWidget(self.button_6, 2, 2, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_9.setStyleSheet("*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")
        self.button_9.setObjectName("button_9")
        self.buttons.addWidget(self.button_9, 1, 2, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_5.setStyleSheet("*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")
        self.button_5.setObjectName("button_5")
        self.buttons.addWidget(self.button_5, 2, 1, 1, 1)
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_7.setStyleSheet("*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")
        self.button_7.setObjectName("button_7")
        self.buttons.addWidget(self.button_7, 1, 0, 1, 1)
        self.button_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_point.sizePolicy().hasHeightForWidth())
        self.button_point.setSizePolicy(sizePolicy)
        self.button_point.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_point.setStyleSheet("*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")
        self.button_point.setObjectName("button_point")
        self.buttons.addWidget(self.button_point, 5, 2, 1, 1)
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_4.setStyleSheet("*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")
        self.button_4.setObjectName("button_4")
        self.buttons.addWidget(self.button_4, 2, 0, 1, 1)
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        self.button_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_0.setStyleSheet("*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")
        self.button_0.setObjectName("button_0")
        self.buttons.addWidget(self.button_0, 5, 0, 1, 2)
        self.button_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_div.sizePolicy().hasHeightForWidth())
        self.button_div.setSizePolicy(sizePolicy)
        self.button_div.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_div.setStyleSheet("*{\n"
"background-color: orange;\n"
"}\n"
":hover{\n"
"    background-color: #ff8c00;\n"
"}\n"
":onclick{\n"
"    background-color: #ff8c00;\n"
"}")
        self.button_div.setObjectName("button_div")
        self.buttons.addWidget(self.button_div, 1, 4, 1, 1)
        self.button_factorial = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_factorial.sizePolicy().hasHeightForWidth())
        self.button_factorial.setSizePolicy(sizePolicy)
        self.button_factorial.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_factorial.setStyleSheet("*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"    background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"    background-color: #FBFBFB;\n"
"}")
        self.button_factorial.setObjectName("button_factorial")
        self.buttons.addWidget(self.button_factorial, 0, 3, 1, 1)
        self.button_procent = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_procent.sizePolicy().hasHeightForWidth())
        self.button_procent.setSizePolicy(sizePolicy)
        self.button_procent.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_procent.setStyleSheet("*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"    background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"    background-color: #FBFBFB;\n"
"}")
        self.button_procent.setObjectName("button_procent")
        self.buttons.addWidget(self.button_procent, 0, 2, 1, 1)
        self.button_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_mul.sizePolicy().hasHeightForWidth())
        self.button_mul.setSizePolicy(sizePolicy)
        self.button_mul.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_mul.setStyleSheet("*{\n"
"background-color: orange;\n"
"}\n"
":hover{\n"
"    background-color: #ff8c00;\n"
"}\n"
":onclick{\n"
"    background-color: #ff8c00;\n"
"}")
        self.button_mul.setObjectName("button_mul")
        self.buttons.addWidget(self.button_mul, 0, 4, 1, 1)
        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy)
        self.button_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_minus.setStyleSheet("*{\n"
"background-color: orange;\n"
"}\n"
":hover{\n"
"    background-color: #ff8c00;\n"
"}\n"
":onclick{\n"
"    background-color: #ff8c00;\n"
"}")
        self.button_minus.setObjectName("button_minus")
        self.buttons.addWidget(self.button_minus, 2, 4, 1, 1)
        self.button_sqrt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_sqrt.sizePolicy().hasHeightForWidth())
        self.button_sqrt.setSizePolicy(sizePolicy)
        self.button_sqrt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_sqrt.setStyleSheet("*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"    background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"    background-color: #FBFBFB;\n"
"}")
        self.button_sqrt.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/square-root.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_sqrt.setIcon(icon2)
        self.button_sqrt.setIconSize(QtCore.QSize(40, 40))
        self.button_sqrt.setObjectName("button_sqrt")
        self.buttons.addWidget(self.button_sqrt, 2, 3, 1, 1)
        self.button_module = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_module.sizePolicy().hasHeightForWidth())
        self.button_module.setSizePolicy(sizePolicy)
        self.button_module.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_module.setStyleSheet("*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"    background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"    background-color: #FBFBFB;\n"
"}")
        self.button_module.setObjectName("button_module")
        self.buttons.addWidget(self.button_module, 3, 3, 1, 1)
        self.button_sqr = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_sqr.sizePolicy().hasHeightForWidth())
        self.button_sqr.setSizePolicy(sizePolicy)
        self.button_sqr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_sqr.setStyleSheet("*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"box-sizing: border-box;\n"
"\n"
"}\n"
":hover {\n"
"    background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"    background-color: #FBFBFB;\n"
"}")
        self.button_sqr.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/math_square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_sqr.setIcon(icon3)
        self.button_sqr.setIconSize(QtCore.QSize(76, 76))
        self.button_sqr.setObjectName("button_sqr")
        self.buttons.addWidget(self.button_sqr, 1, 3, 1, 1)
        self.button_go = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_go.sizePolicy().hasHeightForWidth())
        self.button_go.setSizePolicy(sizePolicy)
        self.button_go.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_go.setStyleSheet("*{\n"
"background-color: orange;\n"
"}\n"
":hover{\n"
"    background-color: #ff8c00;\n"
"}\n"
":onclick{\n"
"    background-color: #ff8c00;\n"
"}")
        self.button_go.setObjectName("button_go")
        self.buttons.addWidget(self.button_go, 5, 3, 1, 2)
        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy)
        self.button_plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_plus.setStyleSheet("*{\n"
"background-color: orange;\n"
"}\n"
":hover{\n"
"    background-color: #ff8c00;\n"
"}\n"
":onclick{\n"
"    background-color: #ff8c00;\n"
"}")
        self.button_plus.setObjectName("button_plus")
        self.buttons.addWidget(self.button_plus, 3, 4, 1, 1)
        self.verticalLayout.addLayout(self.buttons)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: gray;\n"
"font-size: 20px;\n"
"text-decoration: none;\n"
"margin-top: 10px;")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.lbl_temp.setText(_translate("MainWindow", "0"))
        self.line_entry.setText(_translate("MainWindow", "0"))
        self.button_clear.setText(_translate("MainWindow", "С"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_1.setShortcut(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_2.setShortcut(_translate("MainWindow", "2"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_8.setShortcut(_translate("MainWindow", "8"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_3.setShortcut(_translate("MainWindow", "3"))
        self.button_backspace.setShortcut(_translate("MainWindow", "Backspace"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_6.setShortcut(_translate("MainWindow", "6"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_9.setShortcut(_translate("MainWindow", "9"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_5.setShortcut(_translate("MainWindow", "5"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_7.setShortcut(_translate("MainWindow", "7"))
        self.button_point.setText(_translate("MainWindow", "."))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_4.setShortcut(_translate("MainWindow", "4"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_0.setShortcut(_translate("MainWindow", "0"))
        self.button_div.setText(_translate("MainWindow", "÷"))
        self.button_div.setShortcut(_translate("MainWindow", "/"))
        self.button_factorial.setText(_translate("MainWindow", "x!"))
        self.button_procent.setText(_translate("MainWindow", "%"))
        self.button_mul.setText(_translate("MainWindow", "×"))
        self.button_mul.setShortcut(_translate("MainWindow", "*"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_minus.setShortcut(_translate("MainWindow", "-"))
        self.button_module.setText(_translate("MainWindow", "|x|"))
        self.button_go.setText(_translate("MainWindow", "="))
        self.button_go.setShortcut(_translate("MainWindow", "Return, ="))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_plus.setShortcut(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><a href=\"https://github.com/Im0ne/IVS_calc\"><span style=\" font-size:8pt; font-weight:400; text-decoration: none; color:#939393;\">github.com/Im0ne/IVS_calc </span></a></p></body></html>"))
import files_rc
