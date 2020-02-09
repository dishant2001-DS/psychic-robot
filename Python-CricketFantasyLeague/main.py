# AUTHOR- - - - - - - - - - - - - - - "DISHANT TORASKAR"


from PyQt5 import QtCore, QtGui, QtWidgets
from newteam import Ui_NewTeam
from Evaluate import Ui_Form


class Ui_MainWindow(object):

    #defining method to open evaluate team window
    def eWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()



        
    #defining method to open cteate team window
    def newWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NewTeam()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 81 16pt \"Rockwell Extra Bold\";\n"
"font: 81 22pt \"Rockwell Extra Bold\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 21))
        self.menubar.setObjectName("menubar")
        self.menuMANAGE = QtWidgets.QMenu(self.menubar)
        self.menuMANAGE.setObjectName("menuMANAGE")
        self.menuEVALUATE = QtWidgets.QMenu(self.menubar)
        self.menuEVALUATE.setObjectName("menuEVALUATE")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCREATE_TEAM = QtWidgets.QAction(MainWindow)
        self.actionCREATE_TEAM.setObjectName("actionCREATE_TEAM")
        
        #opening CreateTeam Window 
        self.actionCREATE_TEAM.triggered.connect(self.newWindow)

        
        self.actionSELECT_TEAM = QtWidgets.QAction(MainWindow)
        self.actionSELECT_TEAM.setObjectName("actionSELECT_TEAM")

        #OPENING EVALUATION WINDOW
        self.actionSELECT_TEAM.triggered.connect(self.eWindow)

        
        self.menuMANAGE.addAction(self.actionCREATE_TEAM)
        self.menuMANAGE.addSeparator()
        self.menuEVALUATE.addAction(self.actionSELECT_TEAM)
        self.menubar.addAction(self.menuMANAGE.menuAction())
        self.menubar.addAction(self.menuEVALUATE.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CRICKET FANTASY LEAGUE"))
        self.menuMANAGE.setTitle(_translate("MainWindow", "MANAGE "))
        self.menuEVALUATE.setTitle(_translate("MainWindow", "EVALUATE"))
        self.actionCREATE_TEAM.setText(_translate("MainWindow", "CREATE TEAM"))
        self.actionSELECT_TEAM.setText(_translate("MainWindow", "SELECT TEAM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
