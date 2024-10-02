# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiprikol.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1214, 818)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 130, 1101, 361))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(72)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 390, 1211, 321))
        font1 = QFont()
        font1.setPointSize(72)
        self.label_2.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0420\u0418\u041a\u041e\u041b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0410 \u041e\u041d \u0422\u0415\u0411\u042f \u041d\u0415 \u0425\u041e\u0427\u0415\u0422", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0410\u0425\u0410\u0425\u0410\u0425\u0410\u0425\u0410\u0425\u0410\u0425\u0410\u0425\u0410\u0425\u0410\u0425\u0410\u0425\u0410\u0425\u0410\u0425", None))
    # retranslateUi

