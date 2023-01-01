from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import sys
from PyQt5.QtWidgets import QFileDialog
from PIL import Image

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(7)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/qr-code.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
                                 "background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.area = QtWidgets.QFrame(self.content)
        self.area.setMaximumSize(QtCore.QSize(450, 550))
        self.area.setStyleSheet("border-radius: 10px;")
        self.area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.area.setObjectName("area")
        self.lineEdit_user = QtWidgets.QLineEdit(self.area)
        self.lineEdit_user.setGeometry(QtCore.QRect(80, 400, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
       
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setStyleSheet("QLineEdit {\n"
                                         "    border: 2px solid rgb(45, 45, 45);\n"
                                         "    border-radius: 5px;\n"
                                         "    padding: 15px;\n"
                                         "    background-color: rgb(30, 30, 30);    \n"
                                         "    color: rgb(100, 100, 100);\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid #3fb950;\n"
                                         "}\n"
                                         "QLineEdit:focus {\n"
                                         "    border: 2px solid  #3fb950;    \n"
                                         "    color: rgb(200, 200, 200);\n"
                                         "}")
        self.lineEdit_user.setMaxLength(32)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.pushButton = QtWidgets.QPushButton(self.area)
        self.pushButton.setGeometry(QtCore.QRect(80, 240, 280, 50))
        self.pushButton.setStyleSheet("QPushButton {    \n"
                                      "    background-color: rgb(50, 50, 50);\n"
                                      "    border: 2px solid rgb(60, 60, 60);\n"
                                      "    border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover {    \n"
                                      "    background-color: rgb(60, 60, 60);\n"
                                      "    border: 2px solid #58A6FF;\n"
                                      "}\n"
                                      "QPushButton:pressed {    \n"
                                      "    background-color: #3fb950;\n"
                                      "    border: 2px solid #58A6FF;    \n"
                                      "    color: rgb(35, 35, 35);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.area)
        self.pushButton2.setGeometry(QtCore.QRect(80, 320, 280, 50))
        self.pushButton2.setStyleSheet("QPushButton {    \n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "    border: 2px solid rgb(60, 60, 60);\n"
                                       "    border-radius: 5px;\n"
                                       "}\n"
                                       "QPushButton:hover {    \n"
                                       "    background-color: rgb(60, 60, 60);\n"
                                       "    border: 2px solid #58A6FF;\n"
                                       "}\n"
                                       "QPushButton:pressed {    \n"
                                      "    background-color: #3fb950;\n"
                                      "    border: 2px solid #58A6FF;    \n"
                                       "    color: rgb(35, 35, 35);\n"
                                       "}")
        self.pushButton2.setObjectName("pushButton2")
        self.graphicsView = QtWidgets.QGraphicsView(self.area)
        self.graphicsView.setGeometry(QtCore.QRect(80, 10, 281, 191))
        self.graphicsView.setMaximumSize(QtCore.QSize(300, 300))
        self.graphicsView.setStyleSheet("background-Image:url(Assets/logo.png);\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-position: center;\n"
                                        "")
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.area)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 50))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15)")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_credits = QtWidgets.QLabel(self.bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(75, 75, 75);")
        self.label_credits.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_2.addWidget(self.label_credits)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.cam)
        self.pushButton2.clicked.connect(self.openFileNameDialog)

    def openFileNameDialog(self):
        filename = QFileDialog.getOpenFileName(None, "Select QR Image")
        if filename != "":
            file =str(filename[0])
            # print(file)
            barcode = decode(Image.open(file))
            #print(barcode[0].data.decode("utf-8"))
            self.lineEdit_user.setText(barcode[0].data.decode("utf-8"))

            
    def cam(self):
        def decoder(image):
            gray_img = cv2.cvtColor(image, 0)
            barcode = decode(gray_img)

            for obj in barcode:
                points = obj.polygon
                (x, y, w, h) = obj.rect
                pts = np.array(points, np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(image, [pts], True, (0, 255, 0), 3)

                barcodeData = obj.data.decode("utf-8")
                barcodeType = obj.type
                string = "Data: " + str(barcodeData) + \
                    " | Type " + str(barcodeType)

                cv2.putText(frame, string, (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
  #              print("Data: "+barcodeData + " | Type: "+barcodeType)
                self.lineEdit_user.setText(barcodeData )
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            decoder(frame)
            cv2.imshow('QR-Barcode Reader (Press Q to Exit)', frame)
            code = cv2.waitKey(10)
            if code == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "QR -BarCode Reader"))
        MainWindow.setWindowIcon(QtGui.QIcon('Assets/qr-code.png'))    
        self.lineEdit_user.setText(_translate("MainWindow", "Decode"))
        self.lineEdit_user.setPlaceholderText(
            _translate("MainWindow", "Decode"))
        self.pushButton.setText(_translate(
            "MainWindow", "Decode With Device Camera"))
        self.pushButton2.setText(
            _translate("MainWindow", "Upload Image"))
        self.label_credits.setText(_translate(
            "MainWindow", "Created by: Umer Ahmed"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())