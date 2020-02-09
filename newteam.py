#--------------AUTHOR--------------"DISHANT TORASKAR"

from PyQt5 import QtCore, QtGui, QtWidgets
from Evaluate import Ui_Form
import sqlite3
import sys

DreamTeam = sqlite3.connect('DREAMTEAM.db')
c = DreamTeam.cursor()


class Ui_NewTeam(object):
    def eWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

        
    def setupUi(self, NewTeam):
        self.totalCount = 0
        NewTeam.setObjectName("NewTeam")
        NewTeam.resize(558, 532)
        self.label = QtWidgets.QLabel(NewTeam)
        self.label.setGeometry(QtCore.QRect(0, 40, 561, 51))
        self.label.setStyleSheet("font: 16pt \"Cooper Black\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(NewTeam)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 541, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_4.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(NewTeam)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 170, 541, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setStyleSheet("font: 18pt \"Cooper Black\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(NewTeam)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 541, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setStyleSheet("font: 75 15pt \"MS Serif\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_3.setStyleSheet("font: 18pt \"Cooper Black\";")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.lineEdit.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.pushButton = QtWidgets.QPushButton(NewTeam)
        self.pushButton.setGeometry(QtCore.QRect(230, 470, 101, 23))
        self.pushButton.setStyleSheet("font: 75 12pt \"MS Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(NewTeam)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 500, 101, 23))
        self.pushButton_2.setStyleSheet("font: 75 15pt \"MS Sans Serif\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font: 75 12pt \"MS Sans Serif\";")
        self.pushButton_2.setObjectName("pushButton_2")

        #METHOD TO OPEN EVALUATION WINDOW WHEN CLICKED EVALUATE BUTTON
        self.pushButton_2.clicked.connect(self.eWindow)


        self.listWidget = QtWidgets.QListWidget(NewTeam)
        self.listWidget.setGeometry(QtCore.QRect(10, 210, 241, 251))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(NewTeam)
        self.listWidget_2.setGeometry(QtCore.QRect(300, 211, 251, 251))
        self.listWidget_2.setObjectName("listWidget_2")
        self.retranslateUi(NewTeam)
        QtCore.QMetaObject.connectSlotsByName(NewTeam)




        #ADDING FUNCTIONALITIES

        #Loading Player Names For selecting
        self.radioButton_4.clicked.connect(self.load)
        self.radioButton_3.clicked.connect(self.load)
        self.radioButton_2.clicked.connect(self.load)
        self.radioButton.clicked.connect(self.load)


        #Selecting Players and Displaying On Other List
        self.listWidget.itemDoubleClicked.connect(self.removeList1)
        self.listWidget_2.itemDoubleClicked.connect(self.removeList2)
        

        self.items = []



        #SAVING TEAM AND UPDATING DATABASE
        self.pushButton.clicked.connect(self.saveTeam)

    def retranslateUi(self, NewTeam):
        _translate = QtCore.QCoreApplication.translate
        NewTeam.setWindowTitle(_translate("NewTeam", "Form"))
        self.label.setText(_translate("NewTeam", " SELECT  YOUR  11  PLAYERS"))
        self.radioButton_4.setText(_translate("NewTeam", "Batsman"))
        self.radioButton_3.setText(_translate("NewTeam", "Bowler"))
        self.radioButton_2.setText(_translate("NewTeam", "Wicket-Keeper"))
        self.radioButton.setText(_translate("NewTeam", "All-Rounder"))
        self.label_2.setText(_translate("NewTeam", "No. OF Players Selected :"))
        self.label_4.setText(_translate("NewTeam", "ENTER TEAM NAME"))
        self.pushButton.setText(_translate("NewTeam", "SAVE TEAM"))
        self.pushButton_2.setText(_translate("NewTeam", "EVALUATE"))

    #METHOD TO LOAD NAMES
    def load(self):
        sql = "select Player_Name from Players where ROLE = 'Bat';"
        sql2 = "select Player_Name from Players where ROLE = 'Bowl';"
        sql3 = "select Player_Name from Players where ROLE = 'W-K';"
        sql4 = "select Player_Name from Players where ROLE = 'A-R';"
        
        if self.radioButton_4.isChecked()==True:
            c.execute(sql)
            bt = c.fetchall()
            self.listWidget.clear()
            for i in range(len(bt)):
                item = QtWidgets.QListWidgetItem(bt[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.listWidget.addItem(item)

        if self.radioButton_3.isChecked()==True:
            c.execute(sql2)
            bl = c.fetchall()
            self.listWidget.clear()
            for i in range(len(bl)):
                item = QtWidgets.QListWidgetItem(bl[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.listWidget.addItem(item)

        if self.radioButton_2.isChecked()==True:
            c.execute(sql3)
            wk = c.fetchall()
            self.listWidget.clear()
            for i in range(len(wk)):
                item = QtWidgets.QListWidgetItem(wk[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.listWidget.addItem(item)

        if self.radioButton.isChecked()==True:
            c.execute(sql4)
            ar = c.fetchall()
            self.listWidget.clear()
            for i in range(len(ar)):
                item = QtWidgets.QListWidgetItem(ar[i][0])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.listWidget.addItem(item)




    #METHODS TO ADD AND REMOVE PLAYERS FROM A TEAM
    def removeList1(self,item):
        self.listWidget.takeItem(self.listWidget.row(item))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        self.totalCount = self.listWidget_2.count()
        self.error()
        self.label_3.setText(str(self.totalCount))
        
    def removeList2(self,item):
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.totalCount = self.listWidget_2.count()
        self.label_3.setText(str(self.totalCount))


    #SAVING TEAM
    def saveTeam(self):
        if self.totalCount <= 11:
            for index in range(self.listWidget_2.count()):
                self.items.append(str(self.listWidget_2.item(index).text()))
            actual_score = []
            for player in self.items:
                c.execute("SELECT Score FROM Players WHERE Player_Name = '"+player+"';")
                actual_score.append(c.fetchone())
            score = []
            for i in range(len(actual_score)):
                score.append(actual_score[i][0])
            List= tuple(zip(self.items,score))
            teamName= self.lineEdit.text()
            for i in range(len(List)):
                c.execute("INSERT INTO Teams('Team_Name','Player','Score') VALUES('%s','%s','%d')"%(teamName,List[i][0],List[i][1]))
            DreamTeam.commit()
        else:
            self.error()

    #ERROR HANDLING IF PLAYERS MORE THAN 11
    def error(self):
        error_dialog = QtWidgets.QErrorMessage()
        
        if self.totalCount > 11:
            error_dialog.showMessage("Not More Than 6 Players Allowed")
            error_dialog.exec_()
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewTeam = QtWidgets.QWidget()
    ui = Ui_NewTeam()
    ui.setupUi(NewTeam)
    NewTeam.show()
    sys.exit(app.exec_())
