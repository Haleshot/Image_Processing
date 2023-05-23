# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Thresholding_Without_Background.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_2(object):
    def setupUi(self, Dialog_2):
        if not Dialog_2.objectName():
            Dialog_2.setObjectName(u"Dialog_2")
        Dialog_2.resize(1366, 800)
        self.Open_Image_Button = QPushButton(Dialog_2)
        self.Open_Image_Button.setObjectName(u"Open_Image_Button")
        self.Open_Image_Button.setGeometry(QRect(70, 620, 401, 81))
        self.label_4 = QLabel(Dialog_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(870, 640, 281, 41))
        self.label_4.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Dialog_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(590, 260, 61, 31))
        self.label_3.setStyleSheet(u"font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(Dialog_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(530, 620, 301, 41))
        self.lineEdit.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 11.5pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Dialog_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(690, 20, 571, 561))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Dialog_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 571, 561))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Dialog_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 730, 581, 41))
        self.label_5.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.lineEdit_2 = QLineEdit(Dialog_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(530, 670, 301, 41))
        self.lineEdit_2.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 11.5pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog_2)

        QMetaObject.connectSlotsByName(Dialog_2)
    # setupUi

    def retranslateUi(self, Dialog_2):
        Dialog_2.setWindowTitle(QCoreApplication.translate("Dialog_2", u"Dialog", None))
        self.Open_Image_Button.setText(QCoreApplication.translate("Dialog_2", u"Open Image", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_2", u"Output Image", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_2", u"=>", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog_2", u"Enter Lower Limit...", None))
        self.label_2.setText("")
        self.label.setText("")
        self.label_5.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog_2", u"Enter Upper Limit...", None))
    # retranslateUi

