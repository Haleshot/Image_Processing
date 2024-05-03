# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Image_Processing_Options.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Image_Processing_Options(object):
    def setupUi(self, Image_Processing_Options):
        if not Image_Processing_Options.objectName():
            Image_Processing_Options.setObjectName(u"Image_Processing_Options")
        Image_Processing_Options.resize(1201, 801)
        self.DownSampling_Button = QPushButton(Image_Processing_Options)
        self.DownSampling_Button.setObjectName(u"DownSampling_Button")
        self.DownSampling_Button.setGeometry(QRect(170, 180, 211, 61))
        self.DownSampling_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.UpSampling_Button = QPushButton(Image_Processing_Options)
        self.UpSampling_Button.setObjectName(u"UpSampling_Button")
        self.UpSampling_Button.setGeometry(QRect(170, 310, 211, 61))
        self.UpSampling_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Negative_Button = QPushButton(Image_Processing_Options)
        self.Negative_Button.setObjectName(u"Negative_Button")
        self.Negative_Button.setGeometry(QRect(170, 430, 211, 61))
        self.Negative_Button.setStyleSheet(u"font: 11.5pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Threshold_With_Button = QPushButton(Image_Processing_Options)
        self.Threshold_With_Button.setObjectName(u"Threshold_With_Button")
        self.Threshold_With_Button.setGeometry(QRect(170, 550, 211, 61))
        self.Threshold_With_Button.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Threshold_Without_Button = QPushButton(Image_Processing_Options)
        self.Threshold_Without_Button.setObjectName(u"Threshold_Without_Button")
        self.Threshold_Without_Button.setGeometry(QRect(770, 180, 211, 61))
        self.Threshold_Without_Button.setStyleSheet(u"font: 8.5pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Blur_Button = QPushButton(Image_Processing_Options)
        self.Blur_Button.setObjectName(u"Blur_Button")
        self.Blur_Button.setGeometry(QRect(770, 310, 211, 61))
        self.Blur_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.LPF_Button = QPushButton(Image_Processing_Options)
        self.LPF_Button.setObjectName(u"LPF_Button")
        self.LPF_Button.setGeometry(QRect(770, 430, 211, 61))
        self.LPF_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Gaussian_Button = QPushButton(Image_Processing_Options)
        self.Gaussian_Button.setObjectName(u"Gaussian_Button")
        self.Gaussian_Button.setGeometry(QRect(770, 550, 211, 61))
        self.Gaussian_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Title = QLabel(Image_Processing_Options)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(330, 60, 571, 71))
        self.Title.setStyleSheet(u"font: 24pt \"MS Shell Dlg 2\";\n"
"")
        self.Title.setAlignment(Qt.AlignCenter)
        self.Facial_Feature_Detection_Button = QPushButton(Image_Processing_Options)
        self.Facial_Feature_Detection_Button.setObjectName(u"Facial_Feature_Detection_Button")
        self.Facial_Feature_Detection_Button.setGeometry(QRect(110, 660, 366, 61))
        self.Facial_Feature_Detection_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Laplace_Button = QPushButton(Image_Processing_Options)
        self.Laplace_Button.setObjectName(u"Laplace_Button")
        self.Laplace_Button.setGeometry(QRect(770, 660, 211, 61))
        self.Laplace_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")

        self.retranslateUi(Image_Processing_Options)

        QMetaObject.connectSlotsByName(Image_Processing_Options)
    # setupUi

    def retranslateUi(self, Image_Processing_Options):
        Image_Processing_Options.setWindowTitle(QCoreApplication.translate("Image_Processing_Options", u"Dialog", None))
        self.DownSampling_Button.setText(QCoreApplication.translate("Image_Processing_Options", u"Down Sampling", None))
        self.UpSampling_Button.setText(QCoreApplication.translate("Image_Processing_Options", u"Up Sampling", None))
        self.Negative_Button.setText(QCoreApplication.translate("Image_Processing_Options", u"Negative of the Image", None))
        self.Threshold_With_Button.setText(QCoreApplication.translate("Image_Processing_Options", u"Thresholding with Background", None))
        self.Threshold_Without_Button.setText(QCoreApplication.translate("Image_Processing_Options", u"Thresholding without Background", None))
        self.Blur_Button.setText(QCoreApplication.translate("Image_Processing_Options", u"Apply Blurring", None))
        self.LPF_Button.setText(QCoreApplication.translate("Image_Processing_Options", u"LPF", None))
        self.Gaussian_Button.setText(QCoreApplication.translate("Image_Processing_Options", u"Gaussian Noise", None))
        self.Title.setText(QCoreApplication.translate("Image_Processing_Options", u"Image Processing Options:", None))
        self.Facial_Feature_Detection_Button.setText(QCoreApplication.translate("Image_Processing_Options", u"Facial Feature Detection", None))
        self.Laplace_Button.setText(QCoreApplication.translate("Image_Processing_Options", u"Laplace Edge", None))
    # retranslateUi

