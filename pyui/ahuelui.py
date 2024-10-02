# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ahuelui.ui'
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
import iconsd_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1209, 814)
        Dialog.setStyleSheet(u"backgroung-color: white;\n"
"font: 36pt \"Arial\";")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 70, 881, 551))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-330, -90, 1561, 931))
        self.label_2.setPixmap(QPixmap(u":/iconsd/Iv_EngkyJ1Jp2hodZCgeUFNFsoo-1920.jpg"))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0410\u0425\u0423\u0415\u041b?", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0423 \u0418 \u0418\u0414\u0418 \u041d\u0410\u0425\u0423\u0419", None))
        self.label_2.setText("")
    # retranslateUi

