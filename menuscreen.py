

from PyQt5 import QtCore, QtGui, QtWidgets

from wordscreen import Wordscreen_window


class Menuscreen_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 637)
        MainWindow.setMinimumSize(QtCore.QSize(789, 637))
        MainWindow.setMaximumSize(QtCore.QSize(789, 637))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(789, 637))
        self.centralwidget.setMaximumSize(QtCore.QSize(789, 637))
        self.centralwidget.setObjectName("centralwidget")
        self.mainmenu_widget = QtWidgets.QWidget(self.centralwidget)
        self.mainmenu_widget.setGeometry(QtCore.QRect(0, 0, 881, 721))
        self.mainmenu_widget.setMinimumSize(QtCore.QSize(881, 721))
        self.mainmenu_widget.setMaximumSize(QtCore.QSize(881, 721))
        self.mainmenu_widget.setContextMenuPolicy(
            QtCore.Qt.NoContextMenu)
        self.mainmenu_widget.setToolTipDuration(0)
        self.mainmenu_widget.setAutoFillBackground(False)
        self.mainmenu_widget.setStyleSheet(
            "background-color: rgb(85, 85, 255);")
        self.mainmenu_widget.setObjectName("mainmenu_widget")
        self.mainmenu_label = QtWidgets.QLabel(self.mainmenu_widget)
        self.mainmenu_label.setGeometry(QtCore.QRect(260, 40, 301, 54))
        self.mainmenu_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainmenu_label.setStyleSheet("font: 25pt \"Berlin Sans FB\";\n"
                                          "\n"
                                          "color: rgb(255, 255, 255);")
        self.mainmenu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mainmenu_label.setObjectName("mainmenu_label")
        self.playbutton = QtWidgets.QPushButton(self.mainmenu_widget)
        self.playbutton.setGeometry(QtCore.QRect(410, 380, 231, 71))
        self.playbutton.setStyleSheet("border-radius:20px;\n"
                                      "font: 40pt \"Berlin Sans FB\";\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "color :rgb(0, 0, 127)")
        self.playbutton.setObjectName("playbutton")
        self.username_label = QtWidgets.QLabel(self.mainmenu_widget)
        self.username_label.setGeometry(
            QtCore.QRect(310, 130, 201, 31))
        self.username_label.setStyleSheet("font: 25pt \"Berlin Sans FB\";\n"
                                          "\n"
                                          "color: rgb(255, 255, 255);")
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.quitbutton = QtWidgets.QPushButton(self.mainmenu_widget)
        self.quitbutton.setGeometry(QtCore.QRect(160, 380, 231, 71))
        self.quitbutton.setStyleSheet("border-radius:20px;font: 40pt \"Berlin Sans FB\";\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "color :rgb(0, 0, 127)")
        self.quitbutton.setObjectName("quitbutton")
        self.progress_progressBar = QtWidgets.QProgressBar(
            self.mainmenu_widget)
        self.progress_progressBar.setGeometry(
            QtCore.QRect(350, 220, 141, 41))
        self.progress_progressBar.setProperty("value", 24)
        self.progress_progressBar.setObjectName("progress_progressBar")
        self.level_label = QtWidgets.QLabel(self.mainmenu_widget)
        self.level_label.setGeometry(QtCore.QRect(330, 290, 161, 51))
        self.level_label.setStyleSheet("font: 25pt \"Berlin Sans FB\";\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "color :rgb(0, 0, 127)")
        self.level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.level_label.setObjectName("level_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.mainmenu_label.setText(
            _translate("MainWindow", "Main Menu"))
        self.playbutton.setText(_translate("MainWindow", "Play"))
        self.username_label.setText(
            _translate("MainWindow", "User Name"))
        self.quitbutton.setText(_translate("MainWindow", "Quit"))
        self.level_label.setText(_translate("MainWindow", "Level :"))
        self.playbutton.clicked.connect(self.play)

    def play(self):
        self.wordscreen = Wordscreen_window()
        self.wordscreen.setupUi(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Menuscreen_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
