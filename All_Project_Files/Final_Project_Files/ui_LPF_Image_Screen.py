# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LPF_Image_Screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_5(object):
    def setupUi(self, Dialog_5):
        if not Dialog_5.objectName():
            Dialog_5.setObjectName(u"Dialog_5")
        Dialog_5.resize(1366, 800)
        self.lineEdit = QLineEdit(Dialog_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(530, 620, 301, 81))
        self.lineEdit.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 11.5pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(Dialog_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 730, 581, 41))
        self.label_5.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Open_Image_Button = QPushButton(Dialog_5)
        self.Open_Image_Button.setObjectName(u"Open_Image_Button")
        self.Open_Image_Button.setGeometry(QRect(70, 620, 401, 81))
        self.label = QLabel(Dialog_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 571, 561))
        self.label_4 = QLabel(Dialog_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(870, 640, 281, 41))
        self.label_4.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Dialog_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(590, 260, 61, 31))
        self.label_3.setStyleSheet(u"font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Dialog_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(690, 20, 571, 561))

        self.retranslateUi(Dialog_5)

        QMetaObject.connectSlotsByName(Dialog_5)
    # setupUi

    def retranslateUi(self, Dialog_5):
        Dialog_5.setWindowTitle(QCoreApplication.translate("Dialog_5", u"Dialog", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog_5", u"Enter Mask Size...", None))
        self.label_5.setText("")
        self.Open_Image_Button.setText(QCoreApplication.translate("Dialog_5", u"Open Image", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog_5", u"Output Image", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_5", u"=>", None))
        self.label_2.setText("")
    # retranslateUi

