from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2
from skimage.util import random_noise
import numpy as np



class Ui_Dialog_8(object):
    def setupUi(self, Dialog_8):
        self.counter = 0
        Dialog_8.setObjectName("Dialog_8")
        Dialog_8.resize(1366, 800)
        self.scrollArea = QtWidgets.QScrollArea(Dialog_8)
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
        self.label_3 = QtWidgets.QLabel(Dialog_8)
        self.label_3.setGeometry(QtCore.QRect(660, 300, 61, 31))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog_8)
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
        self.Save_As = QtWidgets.QPushButton(Dialog_8)
        self.Save_As.setGeometry(QtCore.QRect(900, 660, 403, 81))
        self.Save_As.setObjectName("Save_As")
        self.label_5 = QtWidgets.QLabel(Dialog_8)
        self.label_5.setGeometry(QtCore.QRect(400, 740, 581, 41))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.Open_Image_Button = QtWidgets.QPushButton(Dialog_8)
        self.Open_Image_Button.setGeometry(QtCore.QRect(90, 660, 401, 81))
        self.Open_Image_Button.setObjectName("Open_Image_Button")

        self.retranslateUi(Dialog_8)
        QtCore.QMetaObject.connectSlotsByName(Dialog_8)

    def retranslateUi(self, Dialog_8):
        _translate = QtCore.QCoreApplication.translate
        Dialog_8.setWindowTitle(_translate("Dialog_8", "Laplace Edge Detection"))
        self.Open_Image_Button.setText(_translate("Dialog_8", "Open Image"))
        self.label_3.setText(_translate("Dialog_8", "=>"))

        self.Open_Image_Button.setText(_translate("Dialog_8", "Open Image"))
        self.Save_As.setText(_translate("Dialog_8", "Save As"))
        self.Open_Image_Button.clicked.connect(self.File_Select)
        self.Save_As.clicked.connect(self.Save_Directory)


    def laplacian_filter(self, img, kernel_size=3):
        # Define the Laplacian kernel
        kernel = np.array([
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0]
        ], dtype=np.float32)
        
        # Pad the image with zeros
        padded_img = np.pad(img, pad_width=kernel_size//2, mode='constant')
        
        # Apply the Laplacian filter to the image
        filtered_img = np.zeros_like(img, dtype=np.float32)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                filtered_img[i, j] = np.sum(padded_img[i:i+kernel_size, j:j+kernel_size] * kernel)
        
        # Normalize the filtered image to the range [0, 255]
        filtered_img = cv2.normalize(filtered_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        
        return filtered_img


    def File_Select(self):
        file_name, _ = QFileDialog.getOpenFileName(None, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif *.png)")
        if file_name:
            self.label.setPixmap(QPixmap(file_name))
            self.counter += 1
            img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

            # Apply the Laplacian filter to the image
            filtered_img = self.laplacian_filter(img)

            cv2.imwrite(r"All_Project_Files\Final_Project_Files\Cam_Media\Laplacian_Images\Laplacian_Image.png", filtered_img)
            Laplacian_File_Name = r"All_Project_Files\Final_Project_Files\Cam_Media\Laplacian_Images\Laplacian_Image.png"
            # self.label_2.setPixmap(QPixmap(Laplacian_File_Name))

            lay = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
            lay_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        
            lay.setContentsMargins(0, 0, 0, 0)
            lay_2.setContentsMargins(0, 0, 0, 0)

            lay.addWidget(self.label)
            lay_2.addWidget(self.label_2)

            self.label.setPixmap(QPixmap(file_name))
            self.label_2.setPixmap(QPixmap(Laplacian_File_Name))

            self.label_5.setText("")

            # self.scrollArea.setWidgetResizable(True)
            # self.scrollArea_2.setWidgetResizable(True)

            self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            self.Open_Image_Button.setEnabled(False)

    def Save_Directory(self):
        image_laplace = cv2.imread(r"All_Project_Files\Final_Project_Files\Cam_Media\Laplacian_Images\Laplacian_Image.png")
        option = QFileDialog.Options()
        
        if self.counter > 0:
            save_as_path = QFileDialog.getSaveFileName(None, 'Open Image File', r"Laplacian Image", "Image files (*.jpg *.jpeg *.gif *.png)")

            if option:
                cv2.imwrite(save_as_path[0], image_laplace)

        else:
            self.label_5.setText("Please select a file first!")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_8 = QtWidgets.QDialog()
    ui = Ui_Dialog_8()
    ui.setupUi(Dialog_8)
    Dialog_8.show()
    sys.exit(app.exec_())
