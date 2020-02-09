# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DBUPDATE.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

db = sqlite3.connect('DREAMTEAM.db')
c = db.cursor()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 405)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(72, 10, 251, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 75 16pt \"MS Serif\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 161, 20))
        self.label_2.setStyleSheet("font: 75 16pt \"MS Serif\";")
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(90, 90, 201, 211))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 320, 181, 20))
        self.label_3.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 346, 171, 20))
        self.label_4.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 345, 191, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 370, 81, 23))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 370, 75, 23))
        self.pushButton_2.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(190, 320, 191, 20))
        self.label_5.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.lineEdit_2.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.listWidget.itemDoubleClicked.connect(self.load)
        self.pushButton.clicked.connect(self.update)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "UPDATE PLAYER SCORE"))
        self.label_2.setText(_translate("Form", "SELECT PLAYER"))
        self.label_3.setText(_translate("Form", "SELECTED PLAYER"))
        self.label_4.setText(_translate("Form", "UPDATE SCORE"))
        self.pushButton.setText(_translate("Form", "UPDATE"))
        self.pushButton_2.setText(_translate("Form", "RESET"))

        #CODE FOR LOADING PLAYERS NAME INTO LIST
        sql = "SELECT Player_Name FROM Players"
        c.execute(sql)
        p = c.fetchall()
        for i in range(len(p)):
            item = QtWidgets.QListWidgetItem(p[i][0])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.listWidget.addItem(item)

            
    #FUNCTION FOR DISPLAYING NAME FOR SELECTED PLAYER
    def load(self):
        player = self.listWidget.currentItem()
        global pName
        pName = player.text()
        self.label_5.setText(str(pName))

    
    #FUNCTION FOR UPDATING SCORE IN DATABASE    
    def update(self):
        score = self.lineEdit_2.text()
        c.execute("UPDATE Players SET Score = '"+score+"' WHERE Player_Name = '"+pName+"'")
        db.commit()
        c.execute("UPDATE Teams SET Score = '"+score+"' WHERE Player = '"+pName+"';")
        db.commit()

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
