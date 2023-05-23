# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Thresholding_With_Background.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_3(object):
    def setupUi(self, Dialog_3):
        if not Dialog_3.objectName():
            Dialog_3.setObjectName(u"Dialog_3")
        Dialog_3.resize(1366, 800)
        self.lineEdit = QLineEdit(Dialog_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(530, 620, 301, 41))
        self.lineEdit.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 11.5pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(Dialog_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(530, 670, 301, 41))
        self.lineEdit_2.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 11.5pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Dialog_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(870, 640, 281, 41))
        self.label_4.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Dialog_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(690, 20, 571, 561))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Dialog_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 571, 561))
        self.label.setAlignment(Qt.AlignCenter)
        self.Open_Image_Button = QPushButton(Dialog_3)
        self.Open_Image_Button.setObjectName(u"Open_Image_Button")
        self.Open_Image_Button.setGeometry(QRect(70, 620, 401, 81))
        self.label_3 = QLabel(Dialog_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(590, 260, 61, 31))
        self.label_3.setStyleSheet(u"font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Dialog_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 730, 581, 41))
        self.label_5.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.retranslateUi(Dialog_3)

        QMetaObject.connectSlotsByName(Dialog_3)
    # setupUi

    def retranslateUi(self, Dialog_3):
        Dialog_3.setWindowTitle(QCoreApplication.translate("Dialog_3", u"Dialog", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog_3", u"Enter Lower Limit...", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog_3", u"Enter Upper Limit...", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_3", u"Output Image", None))
        self.label_2.setText("")
        self.label.setText("")
        self.Open_Image_Button.setText(QCoreApplication.translate("Dialog_3", u"Open Image", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_3", u"=>", None))
        self.label_5.setText("")
    # retranslateUi

