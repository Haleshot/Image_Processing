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



class Ui_Dialog_4(object):
    def setupUi(self, Dialog_4):
        Dialog_4.setObjectName("Dialog_4")
        Dialog_4.resize(1366, 800)
        self.lineEdit = QtWidgets.QLineEdit(Dialog_4)
        self.lineEdit.setGeometry(QtCore.QRect(550, 660, 301, 81))
        self.lineEdit.setStyleSheet("border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 11.5pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Dialog_4)
        self.label_5.setGeometry(QtCore.QRect(400, 740, 581, 41))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.Save_As = QtWidgets.QPushButton(Dialog_4)
        self.Save_As.setGeometry(QtCore.QRect(900, 660, 403, 81))
        self.Save_As.setObjectName("Save_As")
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog_4)
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
        self.Open_Image_Button = QtWidgets.QPushButton(Dialog_4)
        self.Open_Image_Button.setGeometry(QtCore.QRect(90, 660, 401, 81))
        self.Open_Image_Button.setObjectName("Open_Image_Button")
        self.scrollArea = QtWidgets.QScrollArea(Dialog_4)
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
        self.label_3 = QtWidgets.QLabel(Dialog_4)
        self.label_3.setGeometry(QtCore.QRect(660, 300, 61, 31))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog_4)
        QtCore.QMetaObject.connectSlotsByName(Dialog_4)

    def retranslateUi(self, Dialog_4):
        _translate = QtCore.QCoreApplication.translate
        Dialog_4.setWindowTitle(_translate("Dialog_4", "Dialog"))
        self.Open_Image_Button.setText(_translate("Dialog_4", "Open Image"))
        self.lineEdit.setPlaceholderText(_translate("Dialog_4", "Enter Degree of Blurring..."))
        self.label_4.setText(_translate("Dialog_4", "Output Image"))
        self.label_3.setText(_translate("Dialog_4", "=>"))


        self.Open_Image_Button.clicked.connect(self.File_Select)

    def File_Select(self):
        Blurring_Degree = self.lineEdit.text() # Accessing the value entered by the user.
        
        if not (int(Blurring_Degree.isdigit())):
            self.label_5.setText("Please enter an integer value!")
        else:
            self.label_5.setText("")
            # fname = QFileDialog.getOpenFileName(self, "Open File", "All_Project_Files\Final_Project_Files\Cam_Media", "Images (*.png *.xpm *.jpg)")
            # # Opening the Image
            # self.pixmap = QPixmap(fname[0]) # This returns a tuple and hence we mention [0].
            # # Adding the picture to the Label.
            # self.label.setPixmap(self.pixmap)
            Blurring_Degree = int(self.lineEdit.text())
            file_name, _ = QFileDialog.getOpenFileName(None, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif *.png)")
            self.label.setPixmap(QPixmap(file_name))
            img = cv2.imread(file_name)
            m, n, c = img.shape
            print("The original size of the image is ", m, " x ", n)
            blurred_image = cv2.blur(img, (Blurring_Degree, Blurring_Degree))
            m, n, c = blurred_image.shape
            print("The new size of the image is ", m, " x ", n)


            cv2.imwrite(r"All_Project_Files\Final_Project_Files\Cam_Media\Blurred_Images\Blurred_Image.png", blurred_image)
            Downsized_File_Name = r"All_Project_Files\Final_Project_Files\Cam_Media\Blurred_Images\Blurred_Image.png"
            self.label_2.setPixmap(QPixmap(Downsized_File_Name))


            # If you want these to display these in separate windows other than GUI.
            # cv2.imshow("Negative Image", negative_img)


            # cv2.imshow("Image", img)
            # cv2.waitKey(0)
    
            # # closing all open windows
            # cv2.destroyAllWindows()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_4 = QtWidgets.QDialog()
    ui = Ui_Dialog_4()
    ui.setupUi(Dialog_4)
    Dialog_4.show()
    sys.exit(app.exec_())
