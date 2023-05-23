# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Next_Page.ui'
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
        self.Camera_Label = QLabel(Background)
        self.Camera_Label.setObjectName(u"Camera_Label")
        self.Camera_Label.setGeometry(QRect(70, 60, 1061, 511))
        self.Camera_Label.setFrameShape(QFrame.WinPanel)
        self.Camera_Label.setFrameShadow(QFrame.Plain)
        self.Camera_Label.setLineWidth(7)
        self.Show_Cam_Save_Image_Button = QPushButton(Background)
        self.Show_Cam_Save_Image_Button.setObjectName(u"Show_Cam_Save_Image_Button")
        self.Show_Cam_Save_Image_Button.setGeometry(QRect(440, 630, 351, 61))
        self.Show_Cam_Save_Image_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);\n"
"")
        self.Proceed_Button = QPushButton(Background)
        self.Proceed_Button.setObjectName(u"Proceed_Button")
        self.Proceed_Button.setGeometry(QRect(490, 710, 251, 61))
        self.Proceed_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Note_Label = QLabel(Background)
        self.Note_Label.setObjectName(u"Note_Label")
        self.Note_Label.setGeometry(QRect(370, 770, 511, 21))

        self.retranslateUi(Background)

        QMetaObject.connectSlotsByName(Background)
    # setupUi

    def retranslateUi(self, Background):
        Background.setWindowTitle(QCoreApplication.translate("Background", u"Dialog", None))
        self.Camera_Label.setText("")
        self.Show_Cam_Save_Image_Button.setText(QCoreApplication.translate("Background", u"Show Camera/Save Image", None))
        self.Proceed_Button.setText(QCoreApplication.translate("Background", u"Proceed", None))
        self.Note_Label.setText(QCoreApplication.translate("Background", u"Note - Proceeding to the Next Page where various operations on the Image can be done.", None))
    # retranslateUi

