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


class Ui_Dialog_7(object):
    def setupUi(self, Dialog_7):
        Dialog_7.setObjectName("Dialog_7")
        Dialog_7.resize(1366, 801)
        self.Open_Image_Button = QtWidgets.QPushButton(Dialog_7)
        self.Open_Image_Button.setGeometry(QtCore.QRect(90, 660, 401, 81))
        self.Open_Image_Button.setObjectName("Open_Image_Button")
        self.label_3 = QtWidgets.QLabel(Dialog_7)
        self.label_3.setGeometry(QtCore.QRect(660, 300, 61, 31))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog_7)
        self.label_5.setGeometry(QtCore.QRect(400, 740, 581, 41))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.scrollArea = QtWidgets.QScrollArea(Dialog_7)
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
        self.Save_As = QtWidgets.QPushButton(Dialog_7)
        self.Save_As.setGeometry(QtCore.QRect(900, 660, 403, 81))
        self.Save_As.setObjectName("Save_As")
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog_7)
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

        self.retranslateUi(Dialog_7)
        QtCore.QMetaObject.connectSlotsByName(Dialog_7)

    def retranslateUi(self, Dialog_7):
        _translate = QtCore.QCoreApplication.translate
        Dialog_7.setWindowTitle(_translate("Dialog_7", "Facial Features Detection"))
        self.Open_Image_Button.setText(_translate("Dialog_7", "Open Image"))
        self.label_3.setText(_translate("Dialog_7", "=>"))

        self.Open_Image_Button.setText(_translate("Dialog_7", "Open Image"))
        self.Save_As.setText(_translate("Dialog_7", "Save As"))
        self.Open_Image_Button.clicked.connect(self.File_Select)
        self.Save_As.clicked.connect(self.Save_Directory)


    def File_Select(self):
        
        
        # Load the classifier
        face_cascade = cv2.CascadeClassifier("All_Project_Files\haarcascade_frontalface_default.xml")
        eye_cascade = cv2.CascadeClassifier("All_Project_Files\haarcascade_eye.xml")


        self.label_5.setText("")
        # fname = QFileDialog.getOpenFileName(self, "Open File", "All_Project_Files\Final_Project_Files\Cam_Media", "Images (*.png *.xpm *.jpg)")
        # # Opening the Image
        # self.pixmap = QPixmap(fname[0]) # This returns a tuple and hence we mention [0].
        # # Adding the picture to the Label.
        # self.label.setPixmap(self.pixmap)
        
        file_name, _ = QFileDialog.getOpenFileName(None, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif *.png)")
        if file_name:
            self.label.setPixmap(QPixmap(file_name))
            img = cv2.imread(file_name)
            m, n, c = img.shape
            print("The original size of the image is ", m, " x ", n)
            Face_Detected_img = img.copy()
            
            # Convert the image to grayscale
            gray = cv2.cvtColor(Face_Detected_img, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            # Iterate over each face
            for (x, y, w, h) in faces:
                # Draw a rectangle around the face
                cv2.rectangle(Face_Detected_img, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # Detect eyes
                roi_gray = gray[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    # Draw a rectangle around the eyes
                    cv2.rectangle(Face_Detected_img, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
                



            
            m, n, c = Face_Detected_img.shape
            print("The new size of the image is ", m, " x ", n)

            
            cv2.imwrite(r"All_Project_Files\Final_Project_Files\Cam_Media\Face_Detection_Images\Face_Detected_Image.png", Face_Detected_img)
            Face_Detected_Image_File_Name = r"All_Project_Files\Final_Project_Files\Cam_Media\Face_Detection_Images\Face_Detected_Image.png"
            
            # self.label_2.setPixmap(QPixmap(Face_Detected_Image_File_Name))

            lay = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
            lay_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        
            lay.setContentsMargins(0, 0, 0, 0)
            lay_2.setContentsMargins(0, 0, 0, 0)

            lay.addWidget(self.label)
            lay_2.addWidget(self.label_2)

            self.label.setPixmap(QPixmap(file_name))
            self.label_2.setPixmap(QPixmap(Face_Detected_Image_File_Name))

            # self.scrollArea.setWidgetResizable(True)
            # self.scrollArea_2.setWidgetResizable(True)

            self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            self.Open_Image_Button.setEnabled(False)


        # If you want these to display these in separate windows other than GUI.
        # cv2.imshow("Negative Image", negative_img)


        # cv2.imshow("Image", img)
        # cv2.waitKey(0)

        # # closing all open windows
        # cv2.destroyAllWindows()

    def Save_Directory(self):
        image_facial_feature_detection = cv2.imread(r"All_Project_Files\Final_Project_Files\Cam_Media\Face_Detection_Images\Face_Detected_Image.png")
        option = QFileDialog.Options()
        save_as_path = QFileDialog.getSaveFileName(None, 'Open Image File', r"Facial Features Detected Image", "Image files (*.jpg *.jpeg *.gif *.png)")

        if option:
            cv2.imwrite(save_as_path[0], image_facial_feature_detection)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_7 = QtWidgets.QDialog()
    ui = Ui_Dialog_7()
    ui.setupUi(Dialog_7)
    Dialog_7.show()
    sys.exit(app.exec_())