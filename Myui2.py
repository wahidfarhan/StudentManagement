# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Myui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1001, 842)
        Form.setMinimumSize(QtCore.QSize(1001, 842))
        Form.setStyleSheet("#frame QComboBox\n"
"{\n"
"    margin-left: 10px;\n"
"    padding-left: 3px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid white;\n"
"    padding-top: 7px;\n"
"    padding-bottom: 7px;\n"
"    font-family: Sogoe Ul Semibold;\n"
"    font-size: 17px;\n"
"    color: white;\n"
"}\n"
"#frame QComboBox::drop-down\n"
"{\n"
"    margin-left: 15px;\n"
"    padding-left: 3px;\n"
"    padding-top: 7px;\n"
"    padding-bottom: 7px;\n"
"\n"
"}\n"
"#frame QLineEdit\n"
"{\n"
"    margin-left: 10px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid white;\n"
"    padding-top: 7px;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 7px;\n"
"    font-family: Sogoe Ul Semibold;\n"
"    font-size: 17px;\n"
"    color: white;\n"
"}\n"
"#frame QLabel\n"
"{\n"
"    font-family: Sogoe Ul Semibold;\n"
"    font-size: 17px;\n"
"}\n"
"\n"
"#frame\n"
"{\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgb(106, 110, 118);\n"
"}\n"
"#frame_3\n"
"{\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgb(106, 110, 118);\n"
"    padding-top: 7px;\n"
"    padding-bottom: 7px;\n"
"}\n"
"QWidget\n"
"{\n"
"    background-color:#35374B;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(0, 170, 127);\n"
"    font-size: 14px;\n"
"    font: bold;\n"
"    color: white;\n"
"    padding: 5px 10px;\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(162, 162, 162);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    border-color:rgb(206, 228, 255);\n"
"    font-size: 15px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(100, 100, 100); /* Example pressed color */\n"
"    border-color: rgb(200, 200, 200);     /* Slight border color change */\n"
"    padding-top: 6px;  /* Pressed effect by shifting down slightly */\n"
"    padding-bottom: 4px;\n"
"}\n"
"QTableWidget\n"
"{\n"
"    border-radius: 5px;\n"
"    border:1px solid rgb(106, 110, 118);\n"
"}\n"
"QHeaderView::section\n"
"{\n"
"    color: white;\n"
"    background-color:rgb(81, 81, 81);\n"
"    border: 1px solid;\n"
"    border-bottom: 1px solid #505050;\n"
"    text-align: left;\n"
"    padding: 3px 5px;\n"
"}\n"
"QTableWidget::item {\n"
"               border: 1px solid rgb(106, 110, 118);\n"
"            }\n"
"QTableWidget::item:selected\n"
"{\n"
"    background-color: #0078d7;  /* Blue background */\n"
"    color: white;\n"
"    \n"
"\n"
"}\n"
"QTableWidget::row:hover\n"
"{\n"
"    background-color:#C0C9EE;\n"
"}")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(320, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-left:10px;")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("background-color: #31363F;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_3.setHorizontalSpacing(15)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(40)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(5, -1, -1, -1)
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(40)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setStyleSheet("background-color: #31363F;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Add_Button = QtWidgets.QPushButton(self.frame_3)
        self.Add_Button.setStyleSheet("background-color: #0E2954;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Python Programs/Icons/add_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Add_Button.setIcon(icon)
        self.Add_Button.setIconSize(QtCore.QSize(30, 30))
        self.Add_Button.setObjectName("Add_Button")
        self.horizontalLayout.addWidget(self.Add_Button)
        self.Select_Button = QtWidgets.QPushButton(self.frame_3)
        self.Select_Button.setStyleSheet("background-color: #0E2954;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Python Programs/Icons/select_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Select_Button.setIcon(icon1)
        self.Select_Button.setIconSize(QtCore.QSize(30, 30))
        self.Select_Button.setObjectName("Select_Button")
        self.horizontalLayout.addWidget(self.Select_Button)
        self.Search_Button = QtWidgets.QPushButton(self.frame_3)
        self.Search_Button.setStyleSheet("background-color: #0E2954;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Python Programs/Icons/search_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Search_Button.setIcon(icon2)
        self.Search_Button.setIconSize(QtCore.QSize(30, 30))
        self.Search_Button.setObjectName("Search_Button")
        self.horizontalLayout.addWidget(self.Search_Button)
        self.Update_Button = QtWidgets.QPushButton(self.frame_3)
        self.Update_Button.setStyleSheet("background-color: #0E2954;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Python Programs/Icons/update_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Update_Button.setIcon(icon3)
        self.Update_Button.setIconSize(QtCore.QSize(30, 30))
        self.Update_Button.setObjectName("Update_Button")
        self.horizontalLayout.addWidget(self.Update_Button)
        self.Clear_Button = QtWidgets.QPushButton(self.frame_3)
        self.Clear_Button.setStyleSheet("background-color: #0E2954;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Python Programs/Icons/clear_all_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Clear_Button.setIcon(icon4)
        self.Clear_Button.setIconSize(QtCore.QSize(30, 30))
        self.Clear_Button.setObjectName("Clear_Button")
        self.horizontalLayout.addWidget(self.Clear_Button)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setStyleSheet("background-color: #CD1818;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Python Programs/Icons/delete_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setStyleSheet("background-color: #31363F;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout_5.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "Student Information"))
        self.label_8.setText(_translate("Form", "Total Students: "))
        self.label_3.setText(_translate("Form", "Student Id"))
        self.label_2.setText(_translate("Form", "First Name"))
        self.label.setText(_translate("Form", "Last Name"))
        self.label_4.setText(_translate("Form", "District"))
        self.label_5.setText(_translate("Form", "Phone Number"))
        self.label_6.setText(_translate("Form", "Email Address"))
        self.Add_Button.setText(_translate("Form", "Add"))
        self.Select_Button.setText(_translate("Form", "Load"))
        self.Search_Button.setText(_translate("Form", "Search"))
        self.Update_Button.setText(_translate("Form", "Update"))
        self.Clear_Button.setText(_translate("Form", "Clear"))
        self.pushButton_6.setText(_translate("Form", "Delete"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Student ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "District"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Phone Number"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Email Address"))
