#----------------------AUTHOR-----------------------"DISHANT TORASKAR"


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

db = sqlite3.connect('DREAMTEAM.db')
c = db.cursor()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(440, 415)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 0, 351, 20))
        self.label.setStyleSheet("font: 75 16pt \"MS Serif\";")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(35, 340, 201, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setStyleSheet("font: 75 16pt \"MS Serif\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("font: 75 16pt \"MS Serif\";\n"
"")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(260, 340, 221, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setStyleSheet("font: 75 16pt \"MS Serif\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("font: 75 16pt \"MS Serif\";\n"
"")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 380, 251, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 16pt \"Lucida Calligraphy\";")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 171, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("font: 75 14pt \"MS Serif\";\n"
"")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(248, 30, 171, 22))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setStyleSheet("font: 75 14pt \"MS Serif\";\n"
"")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 161, 241))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(230, 90, 161, 241))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(Form)
        self.listWidget_3.setGeometry(QtCore.QRect(170, 90, 41, 241))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_4 = QtWidgets.QListWidget(Form)
        self.listWidget_4.setGeometry(QtCore.QRect(390, 90, 41, 241))
        self.listWidget_4.setObjectName("listWidget_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        #CALLING COMBOBOX FUNCTION FOR SETTING DEFAULT TEAMS PLAYERS TO BE DISPLAYED IN LIST
        self.combo1()
        self.combo2()

        #CALLING COMBOBOX FUNTION FOR SELECTING DIFFERENT TEAM
        self.comboBox.currentTextChanged.connect(self.combo1)
        self.comboBox_2.currentTextChanged.connect(self.combo2)
        
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "  SELECT TWO TEAMS TO EVALUATE"))
        self.label_3.setText(_translate("Form", "Points Scored  "))
        self.label_5.setText(_translate("Form", "Points Scored "))

        #CODE FOR ADDING TEAM TO COMBOBOX
        sql = "SELECT Team_Name from Teams;"
        c.execute(sql)
        team= c.fetchall()
        teamlist=[]
        for i in range(len(team)):
            teamlist.append(team[i][0])
        for name in set(teamlist):
            self.comboBox.addItem(name)
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
           
            self.comboBox_2.addItem(name)
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            



    #COMBO FUNCTIONS TO DISPLAY LIST OF PLAYERS AND THIER SCORE FOR PARTICULAR TEAM
    def combo1(self):
        self.listWidget.clear()
        self.listWidget_3.clear()
        team_1 = self.comboBox.currentText()
        c.execute("SELECT Player FROM Teams WHERE Team_Name = '"+team_1+"';")
        player = c.fetchall()
        for i in range(len(player)):
            item = QtWidgets.QListWidgetItem(player[i][0])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('#ffff99'))
            self.listWidget.addItem(item)

        c.execute("SELECT Score FROM Teams Where Team_Name = '"+team_1+"';")
        score = c.fetchall()
        global t1_score
        self.teamscore = []
        for i in range(len(score)):
            self.teamscore.append(score[i][0])
        t1_score = sum(self.teamscore)
        for i in range(len(score)):
            items= QtWidgets.QListWidgetItem(str(score[i][0]))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            items.setFont(font)
            items.setBackground(QtGui.QColor('#fdc086'))
            self.listWidget_3.addItem(items)
        self.label_2.setText(str(sum(self.teamscore)))

    def combo2(self):
        self.listWidget_2.clear()
        self.listWidget_4.clear()
        team_2 = self.comboBox_2.currentText()
        c.execute("SELECT Player FROM Teams WHERE Team_Name = '"+team_2+"';")
        player = c.fetchall()
        for i in range(len(player)):
            item = QtWidgets.QListWidgetItem(player[i][0])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('#ffff99'))
            self.listWidget_2.addItem(item)

        c.execute("SELECT Score FROM Teams Where Team_Name = '"+team_2+"';")
        score = c.fetchall()
        self.teamscore = []
        global t2_score
        for i in range(len(score)):
            self.teamscore.append(score[i][0])
        t2_score = sum(self.teamscore)
        for i in range(len(score)):
            items= QtWidgets.QListWidgetItem(str(score[i][0]))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            items.setFont(font)
            items.setBackground(QtGui.QColor('#fdc086'))
            self.listWidget_4.addItem(items)
        self.label_4.setText(str(sum(self.teamscore)))

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
