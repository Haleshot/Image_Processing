import cv2
import numpy as np
import os
import tempfile
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QFileDialog,
                             QLabel, QPushButton, QStackedWidget, QVBoxLayout,
                             QWidget)
from PyQt5.uic import loadUi
from skimage.util import random_noise

class Ui_Dialog_6(object):
    def __init__(self):
        self.output_image = None
        with tempfile.NamedTemporaryFile(suffix=".png") as f:
            self.buffer_image_filename = f.name
    def __del__(self):
        if self.output_image is not None:
            os.remove(self.buffer_image_filename)
    def setupUi(self, Dialog_6):
        Dialog_6.setObjectName("Dialog_6")
        Dialog_6.resize(1366, 800)
        self.Save_As = QtWidgets.QPushButton(Dialog_6)
        self.Save_As.setGeometry(QtCore.QRect(900, 660, 403, 81))
        self.Save_As.setObjectName("Save_As")
        self.label_3 = QtWidgets.QLabel(Dialog_6)
        self.label_3.setGeometry(QtCore.QRect(660, 300, 61, 31))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog_6)
        self.label_5.setGeometry(QtCore.QRect(400, 740, 581, 41))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog_6)
        self.scrollArea_2.setGeometry(QtCore.QRect(730, 40, 571, 561))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 569, 559))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 571, 561))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.Open_Image_Button = QtWidgets.QPushButton(Dialog_6)
        self.Open_Image_Button.setGeometry(QtCore.QRect(90, 660, 401, 81))
        self.Open_Image_Button.setObjectName("Open_Image_Button")
        self.scrollArea = QtWidgets.QScrollArea(Dialog_6)
        self.scrollArea.setGeometry(QtCore.QRect(80, 40, 571, 561))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 569, 559))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 20, 571, 561))
        self.label.setText("")
        self.label.setObjectName("label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog_6)
        QtCore.QMetaObject.connectSlotsByName(Dialog_6)

    def retranslateUi(self, Dialog_6):
        _translate = QtCore.QCoreApplication.translate
        Dialog_6.setWindowTitle(_translate("Dialog_6", "Gaussian Image"))
        self.Open_Image_Button.setText(_translate("Dialog_6", "Open Image"))
        self.label_3.setText(_translate("Dialog_6", "=>"))

        self.Open_Image_Button.setText(_translate("Dialog_6", "Open Image"))
        self.Save_As.setText(_translate("Dialog_6", "Save As"))
        self.Open_Image_Button.clicked.connect(self.File_Select)
        self.Save_As.clicked.connect(self.Save_Directory)



    def File_Select(self):

        # fname = QFileDialog.getOpenFileName(self, "Open File", "All_Project_Files\Final_Project_Files\Cam_Media", "Images (*.png *.xpm *.jpg)")
        # # Opening the Image
        # self.pixmap = QPixmap(fname[0]) # This returns a tuple and hence we mention [0].
        # # Adding the picture to the Label.
        # self.label.setPixmap(self.pixmap)
        file_name, _ = QFileDialog.getOpenFileName(None, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif *.png)")
        if file_name:
            self.label.setPixmap(QPixmap(file_name))
            img = cv2.imread(file_name, 0)
            converted_image = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

            m, n = img.shape
            print("The original size of the image is ", m, " x ", n)

            self.output_image = cv2.fastNlMeansDenoisingColored(converted_image, None, 20, 20, 7, 21)


            # m, n = Gaussian_Image.shape
            print("The new size of the image is ", m, " x ", n)


            Gaussian_Image_File_Name = self.buffer_image_filename
            cv2.imwrite(Gaussian_Image_File_Name, self.output_image)
            # self.label_2.setPixmap(QPixmap(Gaussian_Image_File_Name))

            lay = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
            lay_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)

            lay.setContentsMargins(0, 0, 0, 0)
            lay_2.setContentsMargins(0, 0, 0, 0)

            lay.addWidget(self.label)
            lay_2.addWidget(self.label_2)

            self.label.setPixmap(QPixmap(file_name))
            self.label_2.setPixmap(QPixmap(Gaussian_Image_File_Name))

            # self.scrollArea.setWidgetResizable(True)
            # self.scrollArea_2.setWidgetResizable(True)

            self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            self.Open_Image_Button.setEnabled(False)

    def Save_Directory(self):
        option = QFileDialog.Options()
        save_as_path = QFileDialog.getSaveFileName(None, 'Open Image File', r"Gaussian Image", "Image files (*.jpg *.jpeg *.gif *.png)")
        if save_as_path[0].__len__() > 0:
            cv2.imwrite(save_as_path[0], self.output_image)

        # If you want these to display these in separate windows other than GUI.
        # cv2.imshow("Negative Image", negative_img)


        # cv2.imshow("Image", img)
        # cv2.waitKey(0)

        # # closing all open windows
        # cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_6 = QtWidgets.QDialog()
    ui = Ui_Dialog_6()
    ui.setupUi(Dialog_6)
    Dialog_6.show()
    sys.exit(app.exec_())
