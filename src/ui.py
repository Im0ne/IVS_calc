# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(602, 769)
        icon = QIcon()
        icon.addFile(u":/icons/calculator_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 50%;\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	width: 100%;\n"
"   height: 100%;\n"
"	font-size: 25px;\n"
"	margin: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet(u"color: #888;\n"
"font-size: 25px;\n"
"height: 50px;\n"
"margin-top: 8px;")
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.line_entry = QLineEdit(self.centralwidget)
        self.line_entry.setObjectName(u"line_entry")
        self.line_entry.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_entry.sizePolicy().hasHeightForWidth())
        self.line_entry.setSizePolicy(sizePolicy1)
        self.line_entry.setStyleSheet(u"font-size: 60px;\n"
"border: none;\n"
"text-alight: right;\n"
"")
        self.line_entry.setMaxLength(16)
        self.line_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.line_entry)

        self.buttons = QGridLayout()
        self.buttons.setObjectName(u"buttons")
        self.buttons.setContentsMargins(-1, 9, -1, -1)
        self.button_clear = QPushButton(self.centralwidget)
        self.button_clear.setObjectName(u"button_clear")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_clear.sizePolicy().hasHeightForWidth())
        self.button_clear.setSizePolicy(sizePolicy2)
        self.button_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_clear.setStyleSheet(u"*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"	background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"	background-color: #FBFBFB;\n"
"}")

        self.buttons.addWidget(self.button_clear, 0, 0, 1, 1)

        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        sizePolicy2.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy2)
        self.button_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_1.setStyleSheet(u"*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")

        self.buttons.addWidget(self.button_1, 3, 0, 1, 1)

        self.button_2 = QPushButton(self.centralwidget)
        self.button_2.setObjectName(u"button_2")
        sizePolicy2.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy2)
        self.button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_2.setStyleSheet(u"*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")

        self.buttons.addWidget(self.button_2, 3, 1, 1, 1)

        self.button_8 = QPushButton(self.centralwidget)
        self.button_8.setObjectName(u"button_8")
        sizePolicy2.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy2)
        self.button_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_8.setStyleSheet(u"*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")

        self.buttons.addWidget(self.button_8, 1, 1, 1, 1)

        self.button_3 = QPushButton(self.centralwidget)
        self.button_3.setObjectName(u"button_3")
        sizePolicy2.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy2)
        self.button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_3.setStyleSheet(u"*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")

        self.buttons.addWidget(self.button_3, 3, 2, 1, 1)

        self.button_backspace = QPushButton(self.centralwidget)
        self.button_backspace.setObjectName(u"button_backspace")
        sizePolicy2.setHeightForWidth(self.button_backspace.sizePolicy().hasHeightForWidth())
        self.button_backspace.setSizePolicy(sizePolicy2)
        self.button_backspace.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_backspace.setStyleSheet(u"*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"	background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"	background-color: #FBFBFB;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/backspace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_backspace.setIcon(icon1)
        self.button_backspace.setIconSize(QSize(40, 40))

        self.buttons.addWidget(self.button_backspace, 0, 1, 1, 1)

        self.button_6 = QPushButton(self.centralwidget)
        self.button_6.setObjectName(u"button_6")
        sizePolicy2.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy2)
        self.button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_6.setStyleSheet(u"*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")

        self.buttons.addWidget(self.button_6, 2, 2, 1, 1)

        self.button_9 = QPushButton(self.centralwidget)
        self.button_9.setObjectName(u"button_9")
        sizePolicy2.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy2)
        self.button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_9.setStyleSheet(u"*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")

        self.buttons.addWidget(self.button_9, 1, 2, 1, 1)

        self.button_5 = QPushButton(self.centralwidget)
        self.button_5.setObjectName(u"button_5")
        sizePolicy2.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy2)
        self.button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_5.setStyleSheet(u"*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")

        self.buttons.addWidget(self.button_5, 2, 1, 1, 1)

        self.button_7 = QPushButton(self.centralwidget)
        self.button_7.setObjectName(u"button_7")
        sizePolicy2.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy2)
        self.button_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_7.setStyleSheet(u"*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")

        self.buttons.addWidget(self.button_7, 1, 0, 1, 1)

        self.button_point = QPushButton(self.centralwidget)
        self.button_point.setObjectName(u"button_point")
        sizePolicy2.setHeightForWidth(self.button_point.sizePolicy().hasHeightForWidth())
        self.button_point.setSizePolicy(sizePolicy2)
        self.button_point.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_point.setStyleSheet(u"*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")

        self.buttons.addWidget(self.button_point, 5, 2, 1, 1)

        self.button_4 = QPushButton(self.centralwidget)
        self.button_4.setObjectName(u"button_4")
        sizePolicy2.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy2)
        self.button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_4.setStyleSheet(u"*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")

        self.buttons.addWidget(self.button_4, 2, 0, 1, 1)

        self.button_0 = QPushButton(self.centralwidget)
        self.button_0.setObjectName(u"button_0")
        sizePolicy2.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy2)
        self.button_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_0.setStyleSheet(u"*{\n"
"background-color: #343434;\n"
"}\n"
":hover{\n"
"background-color: #d3d3d3;\n"
"}\n"
":onclick{\n"
"background-color: #d3d3d3;\n"
"}")

        self.buttons.addWidget(self.button_0, 5, 0, 1, 2)

        self.button_div = QPushButton(self.centralwidget)
        self.button_div.setObjectName(u"button_div")
        sizePolicy2.setHeightForWidth(self.button_div.sizePolicy().hasHeightForWidth())
        self.button_div.setSizePolicy(sizePolicy2)
        self.button_div.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_div.setStyleSheet(u"*{\n"
"background-color: orange;\n"
"}\n"
":hover{\n"
"	background-color: #ff8c00;\n"
"}\n"
":onclick{\n"
"	background-color: #ff8c00;\n"
"}")

        self.buttons.addWidget(self.button_div, 1, 4, 1, 1)

        self.button_factorial = QPushButton(self.centralwidget)
        self.button_factorial.setObjectName(u"button_factorial")
        sizePolicy2.setHeightForWidth(self.button_factorial.sizePolicy().hasHeightForWidth())
        self.button_factorial.setSizePolicy(sizePolicy2)
        self.button_factorial.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_factorial.setStyleSheet(u"*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"	background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"	background-color: #FBFBFB;\n"
"}")

        self.buttons.addWidget(self.button_factorial, 0, 3, 1, 1)

        self.button_procent = QPushButton(self.centralwidget)
        self.button_procent.setObjectName(u"button_procent")
        sizePolicy2.setHeightForWidth(self.button_procent.sizePolicy().hasHeightForWidth())
        self.button_procent.setSizePolicy(sizePolicy2)
        self.button_procent.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_procent.setStyleSheet(u"*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"	background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"	background-color: #FBFBFB;\n"
"}")

        self.buttons.addWidget(self.button_procent, 0, 2, 1, 1)

        self.button_mul = QPushButton(self.centralwidget)
        self.button_mul.setObjectName(u"button_mul")
        sizePolicy2.setHeightForWidth(self.button_mul.sizePolicy().hasHeightForWidth())
        self.button_mul.setSizePolicy(sizePolicy2)
        self.button_mul.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_mul.setStyleSheet(u"*{\n"
"background-color: orange;\n"
"}\n"
":hover{\n"
"	background-color: #ff8c00;\n"
"}\n"
":onclick{\n"
"	background-color: #ff8c00;\n"
"}")

        self.buttons.addWidget(self.button_mul, 0, 4, 1, 1)

        self.button_minus = QPushButton(self.centralwidget)
        self.button_minus.setObjectName(u"button_minus")
        sizePolicy2.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy2)
        self.button_minus.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_minus.setStyleSheet(u"*{\n"
"background-color: orange;\n"
"}\n"
":hover{\n"
"	background-color: #ff8c00;\n"
"}\n"
":onclick{\n"
"	background-color: #ff8c00;\n"
"}")

        self.buttons.addWidget(self.button_minus, 2, 4, 1, 1)

        self.button_sqrt = QPushButton(self.centralwidget)
        self.button_sqrt.setObjectName(u"button_sqrt")
        sizePolicy2.setHeightForWidth(self.button_sqrt.sizePolicy().hasHeightForWidth())
        self.button_sqrt.setSizePolicy(sizePolicy2)
        self.button_sqrt.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_sqrt.setStyleSheet(u"*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"	background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"	background-color: #FBFBFB;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/square-root.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_sqrt.setIcon(icon2)
        self.button_sqrt.setIconSize(QSize(40, 40))

        self.buttons.addWidget(self.button_sqrt, 2, 3, 1, 1)

        self.button_module = QPushButton(self.centralwidget)
        self.button_module.setObjectName(u"button_module")
        sizePolicy2.setHeightForWidth(self.button_module.sizePolicy().hasHeightForWidth())
        self.button_module.setSizePolicy(sizePolicy2)
        self.button_module.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_module.setStyleSheet(u"*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"}\n"
":hover {\n"
"	background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"	background-color: #FBFBFB;\n"
"}")

        self.buttons.addWidget(self.button_module, 3, 3, 1, 1)

        self.button_sqr = QPushButton(self.centralwidget)
        self.button_sqr.setObjectName(u"button_sqr")
        sizePolicy2.setHeightForWidth(self.button_sqr.sizePolicy().hasHeightForWidth())
        self.button_sqr.setSizePolicy(sizePolicy2)
        self.button_sqr.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_sqr.setStyleSheet(u"*{\n"
"background-color: #A5A5A5;\n"
"color: black;\n"
"box-sizing: border-box;\n"
"\n"
"}\n"
":hover {\n"
"	background-color: #FDFDFD;\n"
"}\n"
"\n"
":pressed {\n"
"	background-color: #FBFBFB;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/math_square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_sqr.setIcon(icon3)
        self.button_sqr.setIconSize(QSize(76, 76))

        self.buttons.addWidget(self.button_sqr, 1, 3, 1, 1)

        self.button_go = QPushButton(self.centralwidget)
        self.button_go.setObjectName(u"button_go")
        sizePolicy2.setHeightForWidth(self.button_go.sizePolicy().hasHeightForWidth())
        self.button_go.setSizePolicy(sizePolicy2)
        self.button_go.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_go.setStyleSheet(u"*{\n"
"background-color: orange;\n"
"}\n"
":hover{\n"
"	background-color: #ff8c00;\n"
"}\n"
":onclick{\n"
"	background-color: #ff8c00;\n"
"}")

        self.buttons.addWidget(self.button_go, 5, 3, 1, 2)

        self.button_plus = QPushButton(self.centralwidget)
        self.button_plus.setObjectName(u"button_plus")
        sizePolicy2.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy2)
        self.button_plus.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_plus.setStyleSheet(u"*{\n"
"background-color: orange;\n"
"}\n"
":hover{\n"
"	background-color: #ff8c00;\n"
"}\n"
":onclick{\n"
"	background-color: #ff8c00;\n"
"}")

        self.buttons.addWidget(self.button_plus, 3, 4, 1, 1)


        self.verticalLayout.addLayout(self.buttons)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: gray;\n"
"font-size: 20px;\n"
"text-decoration: bold;\n"
"margin-top: 10px;")
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.verticalLayout.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        MainWindow.setProperty("background", "")
        self.lbl_temp.setText("")
        self.line_entry.setText("")
        self.line_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter a value", None))
        self.button_clear.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.button_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.button_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.button_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.button_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.button_backspace.setText("")
#if QT_CONFIG(shortcut)
        self.button_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.button_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.button_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.button_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.button_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.button_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.button_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.button_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.button_div.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.button_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.button_factorial.setText(QCoreApplication.translate("MainWindow", u"x!", None))
        self.button_procent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.button_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.button_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.button_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.button_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.button_sqrt.setText("")
        self.button_module.setText(QCoreApplication.translate("MainWindow", u"|x|", None))
        self.button_sqr.setText("")
        self.button_go.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.button_go.setShortcut(QCoreApplication.translate("MainWindow", u"Return, =", None))
#endif // QT_CONFIG(shortcut)
        self.button_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.button_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://github.com/Im0ne/IVS_calc\"><span style=\" font-size:8pt; font-weight:400; text-decoration: none; color:#939393;\">github.com/Im0ne/IVS_calc </span></a></p></body></html>", None))
    # retranslateUi

