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



class Ui_Background(object):
    def __init__(self):
        self.output_image = None
        with tempfile.NamedTemporaryFile(suffix=".png") as f:
            self.buffer_image_filename = f.name
    def __del__(self):
        if self.output_image is not None:
            os.remove(self.buffer_image_filename)
    def setupUi(self, Background):
        self.counter = 0
        Background.setObjectName("Background")
        Background.resize(1366, 801)
        self.label_5 = QtWidgets.QLabel(Background)
        self.label_5.setGeometry(QtCore.QRect(400, 740, 581, 41))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.Save_As = QtWidgets.QPushButton(Background)
        self.Save_As.setGeometry(QtCore.QRect(900, 660, 403, 81))
        self.Save_As.setObjectName("Save_As")
        self.scrollArea_2 = QtWidgets.QScrollArea(Background)
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
        self.Open_Image_Button = QtWidgets.QPushButton(Background)
        self.Open_Image_Button.setGeometry(QtCore.QRect(90, 660, 401, 81))
        self.Open_Image_Button.setObjectName("Open_Image_Button")
        self.scrollArea = QtWidgets.QScrollArea(Background)
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
        self.label_3 = QtWidgets.QLabel(Background)
        self.label_3.setGeometry(QtCore.QRect(660, 300, 61, 31))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Background)
        QtCore.QMetaObject.connectSlotsByName(Background)

    def retranslateUi(self, Background):
        _translate = QtCore.QCoreApplication.translate
        Background.setWindowTitle(_translate("Background", "Negative Image"))
        self.label_3.setText(_translate("Background", "=>"))

        self.Open_Image_Button.setText(_translate("Dialog", "Open Image"))
        self.Save_As.setText(_translate("Dialog", "Save As"))
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
            self.counter += 1
            img = cv2.imread(file_name)
            maximum = np.amax(img)
            self.output_image = maximum - img
            Negative_File_Name = self.buffer_image_filename
            cv2.imwrite(Negative_File_Name, self.output_image)
            # self.label_2.setPixmap(QPixmap(Negative_File_Name))


            lay = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
            lay_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)

            lay.setContentsMargins(0, 0, 0, 0)
            lay_2.setContentsMargins(0, 0, 0, 0)

            lay.addWidget(self.label)
            lay_2.addWidget(self.label_2)

            self.label.setPixmap(QPixmap(file_name))
            self.label_2.setPixmap(QPixmap(Negative_File_Name))

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
        option = QFileDialog.Options()
        if self.counter > 0:
            save_as_path = QFileDialog.getSaveFileName(None, 'Open Image File', r"Negative Image", "Image files (*.jpg *.jpeg *.gif *.png)")

            if save_as_path[0].__len__() > 0:
                self.label_5.setText("")
                cv2.imwrite(save_as_path[0], self.output_image)
        else:
            self.label_5.setText("Please select a file first!")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Background = QtWidgets.QDialog()
    ui = Ui_Background()
    ui.setupUi(Background)
    Background.show()
    sys.exit(app.exec_())
