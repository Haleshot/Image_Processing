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
        self.Save_As = QPushButton(Dialog_6)
        self.Save_As.setObjectName(u"Save_As")
        self.Save_As.setGeometry(QRect(900, 660, 403, 81))
        self.label_3 = QLabel(Dialog_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(660, 300, 61, 31))
        self.label_3.setStyleSheet(u"font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Dialog_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(400, 740, 581, 41))
        self.label_5.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.scrollArea_2 = QScrollArea(Dialog_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(730, 40, 571, 561))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 569, 559))
        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 571, 561))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.Open_Image_Button = QPushButton(Dialog_6)
        self.Open_Image_Button.setObjectName(u"Open_Image_Button")
        self.Open_Image_Button.setGeometry(QRect(90, 660, 401, 81))
        self.scrollArea = QScrollArea(Dialog_6)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(80, 40, 571, 561))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 569, 559))
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 571, 561))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog_6)

        QMetaObject.connectSlotsByName(Dialog_6)
    # setupUi

    def retranslateUi(self, Dialog_6):
        Dialog_6.setWindowTitle(QCoreApplication.translate("Dialog_6", u"Dialog", None))
        self.Save_As.setText(QCoreApplication.translate("Dialog_6", u"Save As", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_6", u"=>", None))
        self.label_5.setText("")
        self.label_2.setText("")
        self.Open_Image_Button.setText(QCoreApplication.translate("Dialog_6", u"Open Image", None))
        self.label.setText("")
    # retranslateUi

