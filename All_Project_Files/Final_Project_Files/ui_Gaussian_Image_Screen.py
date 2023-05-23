# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gaussian_Image_Screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_6(object):
    def setupUi(self, Dialog_6):
        if not Dialog_6.objectName():
            Dialog_6.setObjectName(u"Dialog_6")
        Dialog_6.resize(1366, 800)
        self.label_2 = QLabel(Dialog_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(690, 20, 571, 561))
        self.Open_Image_Button = QPushButton(Dialog_6)
        self.Open_Image_Button.setObjectName(u"Open_Image_Button")
        self.Open_Image_Button.setGeometry(QRect(70, 620, 401, 81))
        self.label = QLabel(Dialog_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 571, 561))
        self.label_4 = QLabel(Dialog_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(870, 640, 281, 41))
        self.label_4.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Dialog_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 730, 581, 41))
        self.label_5.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_3 = QLabel(Dialog_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(610, 290, 61, 31))
        self.label_3.setStyleSheet(u"font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog_6)

        QMetaObject.connectSlotsByName(Dialog_6)
    # setupUi

    def retranslateUi(self, Dialog_6):
        Dialog_6.setWindowTitle(QCoreApplication.translate("Dialog_6", u"Dialog", None))
        self.label_2.setText("")
        self.Open_Image_Button.setText(QCoreApplication.translate("Dialog_6", u"Open Image", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog_6", u"Output Image", None))
        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog_6", u"=>", None))
    # retranslateUi

