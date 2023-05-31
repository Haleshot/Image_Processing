

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Image_Processing_Options(object):
    def setupUi(self, Image_Processing_Options):
        Image_Processing_Options.setObjectName("Image_Processing_Options")
        Image_Processing_Options.resize(1201, 801)
        self.DownSampling_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.DownSampling_Button.setGeometry(QtCore.QRect(170, 180, 211, 61))
        self.DownSampling_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.DownSampling_Button.setObjectName("DownSampling_Button")
        self.UpSampling_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.UpSampling_Button.setGeometry(QtCore.QRect(170, 310, 211, 61))
        self.UpSampling_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.UpSampling_Button.setObjectName("UpSampling_Button")
        self.Negative_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Negative_Button.setGeometry(QtCore.QRect(170, 430, 211, 61))
        self.Negative_Button.setStyleSheet("font: 11.5pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Negative_Button.setObjectName("Negative_Button")
        self.Threshold_With_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Threshold_With_Button.setGeometry(QtCore.QRect(170, 550, 211, 61))
        self.Threshold_With_Button.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Threshold_With_Button.setObjectName("Threshold_With_Button")
        self.Threshold_Without_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Threshold_Without_Button.setGeometry(QtCore.QRect(770, 180, 211, 61))
        self.Threshold_Without_Button.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Threshold_Without_Button.setObjectName("Threshold_Without_Button")
        self.Blur_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Blur_Button.setGeometry(QtCore.QRect(770, 310, 211, 61))
        self.Blur_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Blur_Button.setObjectName("Blur_Button")
        self.LPF_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.LPF_Button.setGeometry(QtCore.QRect(770, 430, 211, 61))
        self.LPF_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.LPF_Button.setObjectName("LPF_Button")
        self.Gaussian_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Gaussian_Button.setGeometry(QtCore.QRect(770, 550, 211, 61))
        self.Gaussian_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Gaussian_Button.setObjectName("Gaussian_Button")
        self.Title = QtWidgets.QLabel(Image_Processing_Options)
        self.Title.setGeometry(QtCore.QRect(330, 60, 571, 71))
        self.Title.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Facial_Feature_Detection_Button = QtWidgets.QPushButton(Image_Processing_Options)
        self.Facial_Feature_Detection_Button.setGeometry(QtCore.QRect(110, 660, 366, 61))
        self.Facial_Feature_Detection_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Facial_Feature_Detection_Button.setObjectName("Facial_Feature_Detection_Button")
        self.Gaussian_Button_2 = QtWidgets.QPushButton(Image_Processing_Options)
        self.Gaussian_Button_2.setGeometry(QtCore.QRect(770, 660, 211, 61))
        self.Gaussian_Button_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Gaussian_Button_2.setObjectName("Gaussian_Button_2")

        self.retranslateUi(Image_Processing_Options)
        QtCore.QMetaObject.connectSlotsByName(Image_Processing_Options)

    def retranslateUi(self, Image_Processing_Options):
        _translate = QtCore.QCoreApplication.translate
        Image_Processing_Options.setWindowTitle(_translate("Image_Processing_Options", "Dialog"))
        self.DownSampling_Button.setText(_translate("Image_Processing_Options", "Down Sampling"))
        self.UpSampling_Button.setText(_translate("Image_Processing_Options", "Up Sampling"))
        self.Negative_Button.setText(_translate("Image_Processing_Options", "Negative of the Image"))
        self.Threshold_With_Button.setText(_translate("Image_Processing_Options", "Thresholding with Background"))
        self.Threshold_Without_Button.setText(_translate("Image_Processing_Options", "Thresholding without Background"))
        self.Blur_Button.setText(_translate("Image_Processing_Options", "Apply Blurring"))
        self.LPF_Button.setText(_translate("Image_Processing_Options", "LPF"))
        self.Gaussian_Button.setText(_translate("Image_Processing_Options", "Gaussian Noise"))
        self.Title.setText(_translate("Image_Processing_Options", "Image Processing Options:"))
        self.Facial_Feature_Detection_Button.setText(_translate("Image_Processing_Options", "Facial Feature Detection"))
        self.Gaussian_Button_2.setText(_translate("Image_Processing_Options", "Laplace Edge"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Image_Processing_Options = QtWidgets.QDialog()
    ui = Ui_Image_Processing_Options()
    ui.setupUi(Image_Processing_Options)
    Image_Processing_Options.show()
    sys.exit(app.exec_())
