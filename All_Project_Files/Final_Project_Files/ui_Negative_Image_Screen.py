# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Negative_Image_Screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Background(object):
    def setupUi(self, Background):
        if not Background.objectName():
            Background.setObjectName(u"Background")
        Background.resize(1201, 801)
        self.label_3 = QLabel(Background)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(590, 260, 61, 31))
        self.label_3.setStyleSheet(u"font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Background)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 511, 461))
        self.label_2 = QLabel(Background)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(700, 40, 481, 461))
        self.Open_Image_Button = QPushButton(Background)
        self.Open_Image_Button.setObjectName(u"Open_Image_Button")
        self.Open_Image_Button.setGeometry(QRect(80, 580, 401, 81))
        self.label_4 = QLabel(Background)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(800, 600, 281, 41))
        self.label_4.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Background)

        QMetaObject.connectSlotsByName(Background)
    # setupUi

    def retranslateUi(self, Background):
        Background.setWindowTitle(QCoreApplication.translate("Background", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Background", u"=>", None))
        self.label.setText("")
        self.label_2.setText("")
        self.Open_Image_Button.setText(QCoreApplication.translate("Background", u"Open Image", None))
        self.label_4.setText(QCoreApplication.translate("Background", u"Output Image", None))
    # retranslateUi

