# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alena.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1304, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 0, 121, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.sexBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.sexBox.setEditable(False)
        self.sexBox.setObjectName("sexBox")
        self.sexBox.addItem("")
        self.sexBox.addItem("")
        self.gridLayout.addWidget(self.sexBox, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(140, 0, 294, 501))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.sexBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.sexBox_5.setEditable(False)
        self.sexBox_5.setObjectName("sexBox_5")
        self.sexBox_5.addItem("")
        self.sexBox_5.addItem("")
        self.gridLayout_2.addWidget(self.sexBox_5, 4, 1, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_2.addWidget(self.doubleSpinBox_5, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
        self.sexBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.sexBox_2.setEditable(False)
        self.sexBox_2.setObjectName("sexBox_2")
        self.sexBox_2.addItem("")
        self.sexBox_2.addItem("")
        self.gridLayout_2.addWidget(self.sexBox_2, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 5, 0, 1, 1)
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.gridLayout_2.addWidget(self.doubleSpinBox_10, 3, 1, 1, 1)
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.gridLayout_2.addWidget(self.doubleSpinBox_11, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)
        self.sexBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.sexBox_4.setEditable(False)
        self.sexBox_4.setObjectName("sexBox_4")
        self.sexBox_4.addItem("")
        self.sexBox_4.addItem("")
        self.gridLayout_2.addWidget(self.sexBox_4, 1, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(420, 0, 252, 501))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 0, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_3.addWidget(self.spinBox_3, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)
        self.sexBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.sexBox_3.setEditable(False)
        self.sexBox_3.setObjectName("sexBox_3")
        self.sexBox_3.addItem("")
        self.sexBox_3.addItem("")
        self.gridLayout_3.addWidget(self.sexBox_3, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 5, 0, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout_3.addWidget(self.doubleSpinBox_7, 3, 1, 1, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout_3.addWidget(self.doubleSpinBox_8, 4, 1, 1, 1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout_3.addWidget(self.doubleSpinBox_9, 5, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)
        self.sexBox_6 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.sexBox_6.setEditable(False)
        self.sexBox_6.setObjectName("sexBox_6")
        self.sexBox_6.addItem("")
        self.sexBox_6.addItem("")
        self.gridLayout_3.addWidget(self.sexBox_6, 0, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(670, 0, 243, 501))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.sexBox_9 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.sexBox_9.setEditable(False)
        self.sexBox_9.setObjectName("sexBox_9")
        self.sexBox_9.addItem("")
        self.sexBox_9.addItem("")
        self.gridLayout_4.addWidget(self.sexBox_9, 3, 1, 1, 1)
        self.sexBox_10 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.sexBox_10.setEditable(False)
        self.sexBox_10.setObjectName("sexBox_10")
        self.sexBox_10.addItem("")
        self.sexBox_10.addItem("")
        self.gridLayout_4.addWidget(self.sexBox_10, 4, 1, 1, 1)
        self.sexBox_8 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.sexBox_8.setEditable(False)
        self.sexBox_8.setObjectName("sexBox_8")
        self.sexBox_8.addItem("")
        self.sexBox_8.addItem("")
        self.gridLayout_4.addWidget(self.sexBox_8, 0, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 4, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 1, 0, 1, 1)
        self.sexBox_7 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.sexBox_7.setEditable(False)
        self.sexBox_7.setObjectName("sexBox_7")
        self.sexBox_7.addItem("")
        self.sexBox_7.addItem("")
        self.gridLayout_4.addWidget(self.sexBox_7, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 3, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 2, 0, 1, 1)
        self.sexBox_11 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.sexBox_11.setEditable(False)
        self.sexBox_11.setObjectName("sexBox_11")
        self.sexBox_11.addItem("")
        self.sexBox_11.addItem("")
        self.gridLayout_4.addWidget(self.sexBox_11, 2, 1, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(1130, 0, 161, 501))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_33.setObjectName("label_33")
        self.gridLayout_6.addWidget(self.label_33, 2, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 1, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 0, 0, 1, 1)
        self.doubleSpinBox_18 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_6)
        self.doubleSpinBox_18.setObjectName("doubleSpinBox_18")
        self.gridLayout_6.addWidget(self.doubleSpinBox_18, 0, 1, 1, 1)
        self.doubleSpinBox_17 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_6)
        self.doubleSpinBox_17.setObjectName("doubleSpinBox_17")
        self.gridLayout_6.addWidget(self.doubleSpinBox_17, 1, 1, 1, 1)
        self.doubleSpinBox_19 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_6)
        self.doubleSpinBox_19.setObjectName("doubleSpinBox_19")
        self.gridLayout_6.addWidget(self.doubleSpinBox_19, 2, 1, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(910, 0, 221, 501))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 4, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 3, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 1, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 2, 0, 1, 1)
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_5)
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.gridLayout_5.addWidget(self.doubleSpinBox_12, 0, 1, 1, 1)
        self.doubleSpinBox_13 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_5)
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.gridLayout_5.addWidget(self.doubleSpinBox_13, 1, 1, 1, 1)
        self.doubleSpinBox_15 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_5)
        self.doubleSpinBox_15.setObjectName("doubleSpinBox_15")
        self.gridLayout_5.addWidget(self.doubleSpinBox_15, 2, 1, 1, 1)
        self.doubleSpinBox_14 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_5)
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.gridLayout_5.addWidget(self.doubleSpinBox_14, 3, 1, 1, 1)
        self.doubleSpinBox_16 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_5)
        self.doubleSpinBox_16.setObjectName("doubleSpinBox_16")
        self.gridLayout_5.addWidget(self.doubleSpinBox_16, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 520, 591, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1304, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.sexBox.setCurrentIndex(0)
        self.sexBox_5.setCurrentIndex(0)
        self.sexBox_2.setCurrentIndex(0)
        self.sexBox_4.setCurrentIndex(0)
        self.sexBox_3.setCurrentIndex(0)
        self.sexBox_6.setCurrentIndex(0)
        self.sexBox_9.setCurrentIndex(0)
        self.sexBox_10.setCurrentIndex(0)
        self.sexBox_8.setCurrentIndex(0)
        self.sexBox_7.setCurrentIndex(0)
        self.sexBox_11.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Пол"))
        self.label_2.setText(_translate("MainWindow", "Возраст"))
        self.sexBox.setCurrentText(_translate("MainWindow", "Мужской"))
        self.sexBox.setItemText(0, _translate("MainWindow", "Мужской"))
        self.sexBox.setItemText(1, _translate("MainWindow", "Женский"))
        self.label_6.setText(_translate("MainWindow", "живот"))
        self.sexBox_5.setCurrentText(_translate("MainWindow", "однородный"))
        self.sexBox_5.setItemText(0, _translate("MainWindow", "однородный"))
        self.sexBox_5.setItemText(1, _translate("MainWindow", "неоднородный"))
        self.label_7.setText(_translate("MainWindow", "Просвет пузыря"))
        self.sexBox_2.setCurrentText(_translate("MainWindow", "мягкий"))
        self.sexBox_2.setItemText(0, _translate("MainWindow", "мягкий"))
        self.sexBox_2.setItemText(1, _translate("MainWindow", "твердый"))
        self.label_8.setText(_translate("MainWindow", "Размеры желчного пузыря (длина)"))
        self.label_9.setText(_translate("MainWindow", "толщина стенок"))
        self.label_16.setText(_translate("MainWindow", "Размеры желчного пузыря (ширина)"))
        self.label_17.setText(_translate("MainWindow", "Желчный пузырь (форма)"))
        self.sexBox_4.setCurrentText(_translate("MainWindow", "овальная"))
        self.sexBox_4.setItemText(0, _translate("MainWindow", "овальная"))
        self.sexBox_4.setItemText(1, _translate("MainWindow", "грушевидная"))
        self.label_11.setText(_translate("MainWindow", "Эхогенность паренхимы"))
        self.label_12.setText(_translate("MainWindow", "Длина тела"))
        self.label_13.setText(_translate("MainWindow", "Толщина головки"))
        self.sexBox_3.setCurrentText(_translate("MainWindow", "низкая"))
        self.sexBox_3.setItemText(0, _translate("MainWindow", "низкая"))
        self.sexBox_3.setItemText(1, _translate("MainWindow", "высокая"))
        self.label_14.setText(_translate("MainWindow", "Длина хвоста"))
        self.label_15.setText(_translate("MainWindow", "Ширина протока"))
        self.label_18.setText(_translate("MainWindow", "поджулудочная (контуры)"))
        self.sexBox_6.setCurrentText(_translate("MainWindow", "ровные, четкие"))
        self.sexBox_6.setItemText(0, _translate("MainWindow", "ровные, четкие"))
        self.sexBox_6.setItemText(1, _translate("MainWindow", "нечеткие"))
        self.sexBox_9.setCurrentText(_translate("MainWindow", "есть"))
        self.sexBox_9.setItemText(0, _translate("MainWindow", "есть"))
        self.sexBox_9.setItemText(1, _translate("MainWindow", "нет"))
        self.sexBox_10.setCurrentText(_translate("MainWindow", "смыкается"))
        self.sexBox_10.setItemText(0, _translate("MainWindow", "смыкается"))
        self.sexBox_10.setItemText(1, _translate("MainWindow", "не смыкается"))
        self.sexBox_8.setCurrentText(_translate("MainWindow", "розовый"))
        self.sexBox_8.setItemText(0, _translate("MainWindow", "розовый"))
        self.sexBox_8.setItemText(1, _translate("MainWindow", "красный"))
        self.label_24.setText(_translate("MainWindow", "ФГДС (цвет)"))
        self.label_20.setText(_translate("MainWindow", "ФГДС (КАРДИЯ)"))
        self.label_19.setText(_translate("MainWindow", "ФГДС (стенки)"))
        self.sexBox_7.setCurrentText(_translate("MainWindow", "гладкие"))
        self.sexBox_7.setItemText(0, _translate("MainWindow", "гладкие"))
        self.sexBox_7.setItemText(1, _translate("MainWindow", "не гладкие"))
        self.label_21.setText(_translate("MainWindow", "ФГДС(Деффекты)"))
        self.label_22.setText(_translate("MainWindow", "ФГДС (стенки, слизь))"))
        self.sexBox_11.setCurrentText(_translate("MainWindow", "есть"))
        self.sexBox_11.setItemText(0, _translate("MainWindow", "есть"))
        self.sexBox_11.setItemText(1, _translate("MainWindow", "нет"))
        self.label_33.setText(_translate("MainWindow", "трипсин"))
        self.label_31.setText(_translate("MainWindow", "липаза"))
        self.label_29.setText(_translate("MainWindow", "СОЭ"))
        self.label_25.setText(_translate("MainWindow", "альфа-Амилаза"))
        self.label_23.setText(_translate("MainWindow", "билирубин(прям)"))
        self.label_27.setText(_translate("MainWindow", "билирубин(общ)"))
        self.label_26.setText(_translate("MainWindow", "панкпреатическая"))
        self.label_28.setText(_translate("MainWindow", "щелочная фостфаза"))
        self.pushButton.setText(_translate("MainWindow", "далее"))

