from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sys



from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

# import files of various UI pages used in the Project (Workflow)
from Image_Processing_Options import Ui_Image_Processing_Options





# TO DO:
"""
1. Save the original image according to the size of the image with cv2.imwrite parameter.

"""





counter = 0

Capture_counter = 0


class Ui_Background(QDialog, object):
    global Capture
    def setupUi(self, Background):
        Background.setObjectName("Background")
        Background.resize(1201, 801)
        self.Camera_Label = QtWidgets.QLabel(Background)
        self.Camera_Label.setGeometry(QtCore.QRect(280, 60, 640, 480))
        self.Camera_Label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Camera_Label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Camera_Label.setLineWidth(7)
        self.Camera_Label.setText("")
        self.Camera_Label.setObjectName("Camera_Label")
        self.Show_Cam_Save_Image_Button = QtWidgets.QPushButton(Background)
        self.Show_Cam_Save_Image_Button.setGeometry(QtCore.QRect(440, 630, 351, 61))
        self.Show_Cam_Save_Image_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);\n"
"")
        self.Show_Cam_Save_Image_Button.setObjectName("Show_Cam_Save_Image_Button")
        self.Proceed_Button = QtWidgets.QPushButton(Background)
        self.Proceed_Button.setGeometry(QtCore.QRect(490, 720, 251, 61))
        self.Proceed_Button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Proceed_Button.setObjectName("Proceed_Button")


        self.Note_Label = QLabel(Background)
        self.Note_Label.setObjectName(u"Note_Label")
        self.Note_Label.setGeometry(QRect(23, 780, 1500, 21))

        self.retranslateUi(Background)
        QtCore.QMetaObject.connectSlotsByName(Background)

    def retranslateUi(self, Background):
        _translate = QtCore.QCoreApplication.translate
        Background.setWindowTitle(_translate("Background", "Dialog"))
        self.Show_Cam_Save_Image_Button.setText(_translate("Background", "Show Camera/Save Image"))
        self.Proceed_Button.setText(_translate("Background", "Proceed"))
        self.Note_Label.setText(_translate("Background", "<html><head/><body><p><span style=\" color:#ff0000;\">Note - Proceeding to the Next Page where various operations on the Image can be done. It also saves your image in the Self Photos Folder in Cam Media Directory which can be used for the operations.</span></p></body></html>"))


        global counter # When user clicks on Show Camera/Save Image button, this value will first be -1 as Show Camera is clicked. \
        # after which we increment it to 0 1 etc
        self.value = 1

        # When user clicks the Show Camera/Save Image button:
        self.Show_Cam_Save_Image_Button.clicked.connect(self.Cam_Save_Img)

        # When user clicks the Proceed button:
        self.Proceed_Button.clicked.connect(self.Proceed_Function)
        

    def Cam_Save_Img(self):

        global counter
        global Capture_counter
        
        
        counter += 1 # Incrementing the counter here so that when user Clicks on the Show Camera/Save Image button, it will Save the image in the folder.
        Capture = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Explicitly specifying the Source of the Device - Webcam.
        print(type(Capture))
        while Capture.isOpened():
            
            ret, frame = Capture.read()
            if ret:
                # Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # FlippedImage = cv2.flip(Image, 1)
                # ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                # Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                # self.ImageUpdate.emit(Pic)

                self.Show_Cam(frame, 1) # Portrays the Camera input to the GUI QLabel in PyQt5.
                cv2.waitKey()

                if counter > 1:
                    self.value += 1
                    cv2.imwrite("Image_Processing\All_Project_Files\Final_Project_Files\Cam_Media\Self_Photos\%s.png" %(self.value), frame)
                    # If you want the same image to be overwritten everytime you Save the Image, then:
                    # cv2.imwrite("Image_Processing\All_Project_Files\Final_Project_Files\Cam_Media\Self_Photos\Image.png", frame)
                    # The image will be overwritten with the name of Image.png

                    counter = 1 # Reinitializing the value of logic so that user can click multiple pics.
            # Capture.release()
            if Capture_counter == 1:
                Capture.release()

        

    def Show_Cam(self, img, window = 1):
        
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if(img.shape[2] == 4):
                qformat = QImage.Format_RGBA888

            else:
                qformat = QImage.Format_RGB888
            

        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.Camera_Label.setPixmap(QPixmap.fromImage(img))
        self.Camera_Label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        
                

    def Proceed_Function(self):
        global Capture_counter
        Capture_counter += 1
        self.Cam_Save_Img()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Image_Processing_Options()
        self.ui.setupUi(self.window)

        # When running in this file, it is working but running the Main File prompts the error - Background is not defined.
        # Background.hide() # Hides the MainWindow and moves over to the Next Page window (so we won't have multiple windows open - saves memory as well).
        self.window.show()
        
        

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Background = QtWidgets.QDialog()
    ui = Ui_Background()
    ui.setupUi(Background)
    Background.show()
    sys.exit(app.exec_())


