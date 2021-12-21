# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 839)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainWindow.setMaximumSize(QtCore.QSize(999999, 999999))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ressources/F1-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(215, 110, 30, 228);")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_reset_clt_values = QtWidgets.QPushButton(self.groupBox)
        self.btn_reset_clt_values.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_reset_clt_values.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ressources/Clear-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reset_clt_values.setIcon(icon1)
        self.btn_reset_clt_values.setIconSize(QtCore.QSize(32, 32))
        self.btn_reset_clt_values.setObjectName("btn_reset_clt_values")
        self.gridLayout.addWidget(self.btn_reset_clt_values, 3, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.groupBox)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nomLabel = QtWidgets.QLabel(self.groupBox)
        self.nomLabel.setObjectName("nomLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nomLabel)
        self.nomLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nomLineEdit.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.nomLineEdit.setObjectName("nomLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nomLineEdit)
        self.bPLabel = QtWidgets.QLabel(self.groupBox)
        self.bPLabel.setObjectName("bPLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bPLabel)
        self.bPSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.bPSpinBox.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.bPSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.bPSpinBox.setMaximum(9999)
        self.bPSpinBox.setObjectName("bPSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bPSpinBox)
        self.telLabel = QtWidgets.QLabel(self.groupBox)
        self.telLabel.setObjectName("telLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.telLabel)
        self.telSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.telSpinBox.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.telSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.telSpinBox.setSpecialValueText("")
        self.telSpinBox.setProperty("showGroupSeparator", False)
        self.telSpinBox.setSuffix("")
        self.telSpinBox.setMaximum(999999999)
        self.telSpinBox.setProperty("value", 6)
        self.telSpinBox.setObjectName("telSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.telSpinBox)
        self.faxLabel = QtWidgets.QLabel(self.groupBox)
        self.faxLabel.setObjectName("faxLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.faxLabel)
        self.emailLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.emailLineEdit.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.emailLineEdit.setText("")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.emailLineEdit)
        self.modeDePayementLabel = QtWidgets.QLabel(self.groupBox)
        self.modeDePayementLabel.setObjectName("modeDePayementLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.modeDePayementLabel)
        self.modeDePayementComboBox = QtWidgets.QComboBox(self.groupBox)
        self.modeDePayementComboBox.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.modeDePayementComboBox.setObjectName("modeDePayementComboBox")
        self.modeDePayementComboBox.addItem("")
        self.modeDePayementComboBox.addItem("")
        self.modeDePayementComboBox.addItem("")
        self.modeDePayementComboBox.addItem("")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.modeDePayementComboBox)
        self.lb_alert_nom = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_alert_nom.setFont(font)
        self.lb_alert_nom.setObjectName("lb_alert_nom")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lb_alert_nom)
        self.lb_alert_num = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_alert_num.setFont(font)
        self.lb_alert_num.setObjectName("lb_alert_num")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lb_alert_num)
        self.lb_alert_email = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_alert_email.setFont(font)
        self.lb_alert_email.setObjectName("lb_alert_email")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lb_alert_email)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_open_database = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_database.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_open_database.setFont(font)
        self.btn_open_database.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(206, 92, 0);")
        self.btn_open_database.setObjectName("btn_open_database")
        self.horizontalLayout.addWidget(self.btn_open_database)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(206, 92, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ressources/Floppy-Small-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon2)
        self.btn_save.setIconSize(QtCore.QSize(32, 32))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_export = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_export.setFont(font)
        self.btn_export.setStyleSheet("color: rgb(243, 243, 243);\n"
"background-color: rgb(206, 92, 0);")
        self.btn_export.setObjectName("btn_export")
        self.horizontalLayout.addWidget(self.btn_export)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 4, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(215, 110, 30, 228);")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_ajouter_achat = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_ajouter_achat.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ajouter_achat.setFont(font)
        self.btn_ajouter_achat.setObjectName("btn_ajouter_achat")
        self.gridLayout_4.addWidget(self.btn_ajouter_achat, 2, 0, 1, 2)
        self.line_7 = QtWidgets.QFrame(self.groupBox_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_4.addWidget(self.line_7, 0, 0, 1, 2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.articleLabel_2 = QtWidgets.QLabel(self.groupBox_3)
        self.articleLabel_2.setObjectName("articleLabel_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.articleLabel_2)
        self.articleComboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.articleComboBox.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.articleComboBox.setEditable(False)
        self.articleComboBox.setMaxVisibleItems(15)
        self.articleComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.articleComboBox.setObjectName("articleComboBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.articleComboBox)
        self.quantitLabel = QtWidgets.QLabel(self.groupBox_3)
        self.quantitLabel.setObjectName("quantitLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.quantitLabel)
        self.quantitSpinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.quantitSpinBox.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.quantitSpinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.quantitSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.quantitSpinBox.setProperty("showGroupSeparator", True)
        self.quantitSpinBox.setMaximum(99999)
        self.quantitSpinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.quantitSpinBox.setProperty("value", 1)
        self.quantitSpinBox.setObjectName("quantitSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.quantitSpinBox)
        self.prixLabel = QtWidgets.QLabel(self.groupBox_3)
        self.prixLabel.setObjectName("prixLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.prixLabel)
        self.prixSpinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.prixSpinBox.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.prixSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prixSpinBox.setReadOnly(True)
        self.prixSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.prixSpinBox.setProperty("showGroupSeparator", True)
        self.prixSpinBox.setMaximum(999999999)
        self.prixSpinBox.setObjectName("prixSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.prixSpinBox)
        self.prixTotalLabel = QtWidgets.QLabel(self.groupBox_3)
        self.prixTotalLabel.setObjectName("prixTotalLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.prixTotalLabel)
        self.prixTotalSpinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.prixTotalSpinBox.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.prixTotalSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prixTotalSpinBox.setReadOnly(True)
        self.prixTotalSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.prixTotalSpinBox.setProperty("showGroupSeparator", True)
        self.prixTotalSpinBox.setPrefix("")
        self.prixTotalSpinBox.setMaximum(999999999)
        self.prixTotalSpinBox.setObjectName("prixTotalSpinBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.prixTotalSpinBox)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.obs_edit = QtWidgets.QLineEdit(self.groupBox_3)
        self.obs_edit.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.obs_edit.setObjectName("obs_edit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.obs_edit)
        self.gridLayout_4.addLayout(self.formLayout_2, 1, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 0, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 1, 1, 1, 2)
        self.btn_rein = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_rein.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_rein.setFont(font)
        self.btn_rein.setIcon(icon1)
        self.btn_rein.setIconSize(QtCore.QSize(32, 32))
        self.btn_rein.setObjectName("btn_rein")
        self.gridLayout_3.addWidget(self.btn_rein, 2, 1, 1, 2)
        self.table_achats = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_achats.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.table_achats.setFont(font)
        self.table_achats.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_achats.setAutoFillBackground(False)
        self.table_achats.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 236);\n"
"")
        self.table_achats.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.table_achats.setLineWidth(1)
        self.table_achats.setMidLineWidth(0)
        self.table_achats.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_achats.setAlternatingRowColors(True)
        self.table_achats.setShowGrid(True)
        self.table_achats.setGridStyle(QtCore.Qt.CustomDashLine)
        self.table_achats.setWordWrap(False)
        self.table_achats.setCornerButtonEnabled(True)
        self.table_achats.setRowCount(10)
        self.table_achats.setObjectName("table_achats")
        self.table_achats.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.table_achats.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_achats.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_achats.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_achats.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_achats.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_achats.setItem(0, 1, item)
        self.table_achats.horizontalHeader().setVisible(True)
        self.table_achats.horizontalHeader().setCascadingSectionResizes(False)
        self.table_achats.horizontalHeader().setDefaultSectionSize(175)
        self.table_achats.horizontalHeader().setHighlightSections(True)
        self.table_achats.horizontalHeader().setMinimumSectionSize(5)
        self.table_achats.horizontalHeader().setSortIndicatorShown(False)
        self.table_achats.horizontalHeader().setStretchLastSection(True)
        self.table_achats.verticalHeader().setCascadingSectionResizes(False)
        self.table_achats.verticalHeader().setDefaultSectionSize(50)
        self.table_achats.verticalHeader().setSortIndicatorShown(False)
        self.table_achats.verticalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.table_achats, 0, 1, 1, 3)
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(12)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 2, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 948, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(238, 238, 236);\n"
"selection-color: rgb(52, 101, 164);")
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuEdition = QtWidgets.QMenu(self.menubar)
        self.menuEdition.setObjectName("menuEdition")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.statusBar.setFont(font)
        self.statusBar.setStyleSheet("color: rgb(204, 0, 0);")
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNouveau = QtWidgets.QAction(MainWindow)
        self.actionNouveau.setObjectName("actionNouveau")
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ressources/Folder-Open-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOuvrir.setIcon(icon3)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionEnregistrer = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionEnregistrer_2 = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_2.setObjectName("actionEnregistrer_2")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ressources/Actions-window-close-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuitter.setIcon(icon4)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionArri_re = QtWidgets.QAction(MainWindow)
        self.actionArri_re.setObjectName("actionArri_re")
        self.actionAvancer = QtWidgets.QAction(MainWindow)
        self.actionAvancer.setObjectName("actionAvancer")
        self.actionCopier = QtWidgets.QAction(MainWindow)
        self.actionCopier.setObjectName("actionCopier")
        self.actionCouper = QtWidgets.QAction(MainWindow)
        self.actionCouper.setObjectName("actionCouper")
        self.actionColler = QtWidgets.QAction(MainWindow)
        self.actionColler.setObjectName("actionColler")
        self.actionContacter_le_developpeur = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../ressources/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionContacter_le_developpeur.setIcon(icon5)
        self.actionContacter_le_developpeur.setObjectName("actionContacter_le_developpeur")
        self.actionEnregistrer_3 = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_3.setIcon(icon2)
        self.actionEnregistrer_3.setObjectName("actionEnregistrer_3")
        self.actionExporter_en_facture = QtWidgets.QAction(MainWindow)
        self.actionExporter_en_facture.setObjectName("actionExporter_en_facture")
        self.actionA_propos_de_FACTURINGO = QtWidgets.QAction(MainWindow)
        self.actionA_propos_de_FACTURINGO.setObjectName("actionA_propos_de_FACTURINGO")
        self.actionLire_la_docu_mentation = QtWidgets.QAction(MainWindow)
        self.actionLire_la_docu_mentation.setObjectName("actionLire_la_docu_mentation")
        self.menuFichier.addAction(self.actionNouveau)
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addSeparator()
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionEnregistrer_3)
        self.menuFichier.addAction(self.actionExporter_en_facture)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menuEdition.addAction(self.actionArri_re)
        self.menuEdition.addAction(self.actionAvancer)
        self.menuEdition.addSeparator()
        self.menuEdition.addAction(self.actionCopier)
        self.menuEdition.addAction(self.actionCouper)
        self.menuEdition.addAction(self.actionColler)
        self.menuEdition.addSeparator()
        self.menuAide.addAction(self.actionContacter_le_developpeur)
        self.menuAide.addSeparator()
        self.menuAide.addAction(self.actionA_propos_de_FACTURINGO)
        self.menuAide.addAction(self.actionLire_la_docu_mentation)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuEdition.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FACTURINGO"))
        self.groupBox.setTitle(_translate("MainWindow", "ADRESSE DU CLIENT"))
        self.btn_reset_clt_values.setText(_translate("MainWindow", "EFFACER LES CHAMPS"))
        self.btn_reset_clt_values.setShortcut(_translate("MainWindow", "Ctrl+Shift+W"))
        self.nomLabel.setText(_translate("MainWindow", "Nom : "))
        self.nomLineEdit.setPlaceholderText(_translate("MainWindow", "Ex : FACTURINGO client "))
        self.bPLabel.setText(_translate("MainWindow", "BP :  "))
        self.bPSpinBox.setSpecialValueText(_translate("MainWindow", "---"))
        self.telLabel.setText(_translate("MainWindow", "Tel : "))
        self.telSpinBox.setPrefix(_translate("MainWindow", "(+237)"))
        self.faxLabel.setText(_translate("MainWindow", "Email :"))
        self.emailLineEdit.setPlaceholderText(_translate("MainWindow", "Ex : facturingoclient@gmail.com"))
        self.modeDePayementLabel.setText(_translate("MainWindow", "Mode de payement :"))
        self.modeDePayementComboBox.setItemText(0, _translate("MainWindow", "Espèce"))
        self.modeDePayementComboBox.setItemText(1, _translate("MainWindow", "Bancaire"))
        self.modeDePayementComboBox.setItemText(2, _translate("MainWindow", "MTN MOMO"))
        self.modeDePayementComboBox.setItemText(3, _translate("MainWindow", "Oange Money"))
        self.lb_alert_nom.setText(_translate("MainWindow", "Un client doit avoir un nom !!!"))
        self.lb_alert_num.setText(_translate("MainWindow", "Format du numero incorrect !!!"))
        self.lb_alert_email.setText(_translate("MainWindow", "Format de l\'email incorrect !!!"))
        self.btn_open_database.setText(_translate("MainWindow", "     OUVRIR LA BASE DE DONNEES     "))
        self.btn_open_database.setShortcut(_translate("MainWindow", "Ctrl+Shift+X"))
        self.btn_save.setText(_translate("MainWindow", "     ENREGISTRER     "))
        self.btn_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.btn_export.setText(_translate("MainWindow", "     EXPORTER COMME FACTURE     "))
        self.btn_export.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.groupBox_3.setTitle(_translate("MainWindow", "NOUVEL ACHAT"))
        self.btn_ajouter_achat.setText(_translate("MainWindow", "AJOUTER L\'ACHAT"))
        self.btn_ajouter_achat.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.articleLabel_2.setText(_translate("MainWindow", "Désignation : "))
        self.quantitLabel.setText(_translate("MainWindow", "Quantité : "))
        self.prixLabel.setText(_translate("MainWindow", "Prix : "))
        self.prixSpinBox.setSuffix(_translate("MainWindow", " FCFA"))
        self.prixTotalLabel.setText(_translate("MainWindow", "Prix Total : "))
        self.prixTotalSpinBox.setSuffix(_translate("MainWindow", " FCFA"))
        self.label.setText(_translate("MainWindow", "Observation : "))
        self.obs_edit.setPlaceholderText(_translate("MainWindow", "Observation sur l \'article"))
        self.groupBox_2.setTitle(_translate("MainWindow", "ACHATS"))
        self.btn_rein.setText(_translate("MainWindow", "REINITIALISER LES ACHATS"))
        self.btn_rein.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.table_achats.setSortingEnabled(True)
        item = self.table_achats.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Désignation"))
        item = self.table_achats.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantité"))
        item = self.table_achats.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prix"))
        item = self.table_achats.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Prix Total"))
        item = self.table_achats.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Observation"))
        __sortingEnabled = self.table_achats.isSortingEnabled()
        self.table_achats.setSortingEnabled(False)
        self.table_achats.setSortingEnabled(__sortingEnabled)
        self.menuFichier.setTitle(_translate("MainWindow", "&Fichier"))
        self.menuEdition.setTitle(_translate("MainWindow", "&Edition"))
        self.menuAide.setTitle(_translate("MainWindow", "&A Propos"))
        self.actionNouveau.setText(_translate("MainWindow", "&Nouveau client"))
        self.actionNouveau.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOuvrir.setText(_translate("MainWindow", "&Ouvrir facture"))
        self.actionOuvrir.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionEnregistrer.setText(_translate("MainWindow", "Enregistrer"))
        self.actionEnregistrer_2.setText(_translate("MainWindow", "Enregistrer sous"))
        self.actionQuitter.setText(_translate("MainWindow", "&Quitter"))
        self.actionQuitter.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionArri_re.setText(_translate("MainWindow", "&Retour"))
        self.actionArri_re.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionAvancer.setText(_translate("MainWindow", "&Avancer"))
        self.actionAvancer.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionCopier.setText(_translate("MainWindow", "&Copier"))
        self.actionCopier.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionCouper.setText(_translate("MainWindow", "Co&uper"))
        self.actionCouper.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionColler.setText(_translate("MainWindow", "Co&l&ler"))
        self.actionColler.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionContacter_le_developpeur.setText(_translate("MainWindow", "Contacter le &developpeur"))
        self.actionEnregistrer_3.setText(_translate("MainWindow", "&Enregistrer"))
        self.actionExporter_en_facture.setText(_translate("MainWindow", "Exporter en &facture"))
        self.actionA_propos_de_FACTURINGO.setText(_translate("MainWindow", "A propos de &FACTURINGO"))
        self.actionLire_la_docu_mentation.setText(_translate("MainWindow", "Lire la docu&mentation"))