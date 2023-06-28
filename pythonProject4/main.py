
########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2 import *
from PySide2.QtGui import QPixmap
import cv2
########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        self.show()
        # EXPAND CENTER WIDGET SIZE
        self.ui.settingBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        # CLOSED CENTER WIDGET
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        # EXPAND RIGHT WIDGET
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

        # CLOSED RIGHT WIDGET
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        # CLOSED NOTIFICATION WIDGET
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        # OPEN TEXT FILE BUTTON
        self.ui.pushButton_text.clicked.connect(self.slot_fileopen)

    def slot_fileopen(self):
        file_path = 'C:/Users/Administrator/PycharmProjects/pythonProject/pythonProject4/car.txt'
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = file.read()
                    self.ui.textEdit.setText(data)
            except FileNotFoundError:
                print(f"Error: File '{file_path}' not found.")
            except IOError:
                print(f"Error: Unable to read file '{file_path}'.")

        # OPEN IMAGE BUTTON
        self.ui.pushButton_Image.clicked.connect(self.addimage)

    def addimage(self):
        pixmap = QPixmap('C:/Users/Administrator/PycharmProjects/pythonProject/pythonProject4/image/images.jpg')
        self.ui.imageLabel.setPixmap(pixmap)
        self.ui.imageLabel.setScaledContents(True)  # Set the aspect ratio mode for the image label

        # OPEN CAMERA BUTTON
        self.ui.cameraButton.clicked.connect(self.update_drone_camera)
        # DRONE CAMERA UPDATE
        self.drone_camera_timer = QTimer(self)
        self.drone_camera_timer.timeout.connect(self.update_drone_camera)
        self.drone_camera_timer.start(1000)  # Update every 1 second
    def update_drone_camera(self):
            # Update the drone camera image here
            # You can use a library like OpenCV or other methods to capture the drone camera feed
            # and update the pixmap of the image label accordingly
            # Example code to update the image (replace with your actual implementation):
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()

            if ret:
                # Convert the frame to QImage
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channels = rgb_image.shape
                bytes_per_line = channels * width
                qimage = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

                # Create QPixmap from QImage and display it in the label
                pixmap = QPixmap.fromImage(qimage)
                self.ui.cameraLabel.setPixmap(pixmap)
                self.ui.cameraLabel.setScaledContents(True)

            cap.release()
########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################