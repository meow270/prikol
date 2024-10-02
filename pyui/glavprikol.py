# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'glavprikol.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(787, 592)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(48)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: black;\n"
"font-family: Arial;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 150, 561, 171))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(36)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"text-color: black;")
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(400, 320, 281, 221))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(28)
        self.pushButton.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/close_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(100, 100))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 320, 281, 221))
        self.pushButton_2.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/check_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(50, 50))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(560, 0, 231, 211))
        self.label_2.setPixmap(QPixmap(u":/icons/gjirlfriend.gif"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"prikol", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0425\u041e\u0427\u0415\u0428\u042c \u041f\u0420\u0438\u041a\u041e\u041b???", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0415\u0422", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0410", None))
        self.label_2.setText("")
    # retranslateUi

