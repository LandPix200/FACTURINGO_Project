# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_doc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(853, 595)
        font = QtGui.QFont()
        font.setPointSize(13)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_reset = QtWidgets.QPushButton(Dialog)
        self.btn_reset.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reset.setFont(font)
        self.btn_reset.setObjectName("btn_reset")
        self.gridLayout.addWidget(self.btn_reset, 1, 1, 1, 1)
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(534, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 0, 1, 1, 1)
        self.table_stock = QtWidgets.QTableWidget(self.tab)
        self.table_stock.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"gridline-color: rgb(32, 74, 135);\n"
"selection-background-color: rgba(215, 110, 30, 150);\n"
"")
        self.table_stock.setGridStyle(QtCore.Qt.SolidLine)
        self.table_stock.setRowCount(1000)
        self.table_stock.setColumnCount(3)
        self.table_stock.setObjectName("table_stock")
        item = QtWidgets.QTableWidgetItem()
        self.table_stock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_stock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_stock.setHorizontalHeaderItem(2, item)
        self.table_stock.horizontalHeader().setDefaultSectionSize(390)
        self.table_stock.horizontalHeader().setStretchLastSection(True)
        self.table_stock.verticalHeader().setDefaultSectionSize(30)
        self.table_stock.verticalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.table_stock, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_3.addWidget(self.toolButton_2, 0, 1, 1, 1)
        self.table_client = QtWidgets.QTableWidget(self.tab_2)
        self.table_client.setEnabled(True)
        self.table_client.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"gridline-color: rgb(32, 74, 135);\n"
"selection-background-color: rgba(215, 110, 30, 150);")
        self.table_client.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_client.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.table_client.setRowCount(10000)
        self.table_client.setColumnCount(3)
        self.table_client.setObjectName("table_client")
        item = QtWidgets.QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(2, item)
        self.table_client.horizontalHeader().setDefaultSectionSize(350)
        self.table_client.horizontalHeader().setStretchLastSection(True)
        self.table_client.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout_3.addWidget(self.table_client, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 3)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SGBD FACTURINGO"))
        self.btn_reset.setText(_translate("Dialog", "     &ANNULER     "))
        self.btn_save.setText(_translate("Dialog", "     &ENREGISTRER     "))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Rechercher un article en stock"))
        self.toolButton.setText(_translate("Dialog", "     RECHERHCER     "))
        item = self.table_stock.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Désignation"))
        item = self.table_stock.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Quantité en stock"))
        item = self.table_stock.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Prix unitaire"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Données &Stock marchandise"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Rechercher un nom parmi les clients"))
        self.toolButton_2.setText(_translate("Dialog", "     RECHERCHER     "))
        item = self.table_client.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nom"))
        item = self.table_client.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Téléphone"))
        item = self.table_client.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Données &clients"))