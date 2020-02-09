# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DBENTRY.ui'
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
        Form.resize(407, 228)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 391, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Name = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Name.setObjectName("Name")
        self.horizontalLayout.addWidget(self.Name)
        self.Name.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 110, 391, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Bat = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.Bat.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.Bat.setObjectName("Bat")
        self.horizontalLayout_2.addWidget(self.Bat)
        self.Bowl = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.Bowl.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.Bowl.setObjectName("Bowl")
        self.horizontalLayout_2.addWidget(self.Bowl)
        self.WK = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.WK.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.WK.setObjectName("WK")
        self.horizontalLayout_2.addWidget(self.WK)
        self.AR = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.AR.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.AR.setObjectName("AR")
        self.horizontalLayout_2.addWidget(self.AR)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 261, 20))
        self.label_2.setStyleSheet("font: 75 15pt \"MS Serif\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 160, 391, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.Score = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.Score.setObjectName("Score")
        self.horizontalLayout_3.addWidget(self.Score)
        self.Score.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 311, 20))
        self.label_4.setStyleSheet("font: 75 18pt \"MS Serif\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 200, 75, 23))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 200, 75, 23))
        self.pushButton_2.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.Score.clear)
        self.pushButton_2.clicked.connect(self.Name.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.savePlayer)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "PLayer_Name"))
        self.Bat.setText(_translate("Form", "Bat"))
        self.Bowl.setText(_translate("Form", "Bowl"))
        self.WK.setText(_translate("Form", "W-K"))
        self.AR.setText(_translate("Form", "A-R"))
        self.label_2.setText(_translate("Form", "CHOOSE ROLE OF PLAYER"))
        self.label_3.setText(_translate("Form", "Score"))
        self.label_4.setText(_translate("Form", "PLAYER ENTRY"))
        self.pushButton.setText(_translate("Form", "SAVE"))
        self.pushButton_2.setText(_translate("Form", "RESET"))


    def savePlayer(self):
        Name = self.Name.text()
        Score = self.Score.text()

        if self.Bat.isChecked() == True:
            Role = "Bat"
            c.execute("INSERT INTO Players('Player_Name','ROLE','Score') VALUES('%s','%s','%s')"%(Name,Role,Score))
            db.commit()

        if self.Bowl.isChecked() == True:
            Role = "Bowl"
            c.execute("INSERT INTO Players('Player_Name','ROLE','Score') VALUES('%s','%s','%s')"%(Name,Role,Score))
            db.commit()


        if self.WK.isChecked() == True:
            Role = "W-K"
            c.execute("INSERT INTO Players('Player_Name','ROLE','Score') VALUES('%s','%s','%s')"%(Name,Role,Score))
            db.commit()


        if self.AR.isChecked() == True:
            Role = "A-R"
            c.execute("INSERT INTO Players('Player_Name','ROLE','Score') VALUES('%s','%s','%s')"%(Name,Role,Score))
            db.commit()
   
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
