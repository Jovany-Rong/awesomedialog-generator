# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 609)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionConnection = QAction(MainWindow)
        self.actionConnection.setObjectName(u"actionConnection")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widgetCategory = QWidget(self.centralwidget)
        self.widgetCategory.setObjectName(u"widgetCategory")
        self.verticalLayout_2 = QVBoxLayout(self.widgetCategory)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableDialogIndex = QTableView(self.widgetCategory)
        self.tableDialogIndex.setObjectName(u"tableDialogIndex")

        self.verticalLayout_2.addWidget(self.tableDialogIndex)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAdd = QPushButton(self.widgetCategory)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnDel = QPushButton(self.widgetCategory)
        self.btnDel.setObjectName(u"btnDel")

        self.horizontalLayout_2.addWidget(self.btnDel)

        self.btnReorder = QPushButton(self.widgetCategory)
        self.btnReorder.setObjectName(u"btnReorder")

        self.horizontalLayout_2.addWidget(self.btnReorder)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.widgetCategory)

        self.widgetDetail = QWidget(self.centralwidget)
        self.widgetDetail.setObjectName(u"widgetDetail")
        self.verticalLayout_3 = QVBoxLayout(self.widgetDetail)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widgetDetail)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lbId = QLabel(self.widgetDetail)
        self.lbId.setObjectName(u"lbId")

        self.horizontalLayout_4.addWidget(self.lbId)

        self.label = QLabel(self.widgetDetail)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.spinIndex = QSpinBox(self.widgetDetail)
        self.spinIndex.setObjectName(u"spinIndex")

        self.horizontalLayout_4.addWidget(self.spinIndex)

        self.label_2 = QLabel(self.widgetDetail)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.cbSelect = QComboBox(self.widgetDetail)
        self.cbSelect.addItem("")
        self.cbSelect.addItem("")
        self.cbSelect.addItem("")
        self.cbSelect.setObjectName(u"cbSelect")
        self.cbSelect.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.cbSelect)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.widgetDetail)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.spinSameLevel = QSpinBox(self.widgetDetail)
        self.spinSameLevel.setObjectName(u"spinSameLevel")

        self.horizontalLayout_3.addWidget(self.spinSameLevel)

        self.btnSameAdd = QPushButton(self.widgetDetail)
        self.btnSameAdd.setObjectName(u"btnSameAdd")

        self.horizontalLayout_3.addWidget(self.btnSameAdd)

        self.btnSameDel = QPushButton(self.widgetDetail)
        self.btnSameDel.setObjectName(u"btnSameDel")

        self.horizontalLayout_3.addWidget(self.btnSameDel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.widgetDetail)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.spinNextIndex = QSpinBox(self.widgetDetail)
        self.spinNextIndex.setObjectName(u"spinNextIndex")

        self.horizontalLayout_5.addWidget(self.spinNextIndex)

        self.btnNextAdd = QPushButton(self.widgetDetail)
        self.btnNextAdd.setObjectName(u"btnNextAdd")

        self.horizontalLayout_5.addWidget(self.btnNextAdd)

        self.btnNextDel = QPushButton(self.widgetDetail)
        self.btnNextDel.setObjectName(u"btnNextDel")

        self.horizontalLayout_5.addWidget(self.btnNextDel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.widgetDetail)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.editName = QLineEdit(self.widgetDetail)
        self.editName.setObjectName(u"editName")

        self.horizontalLayout_6.addWidget(self.editName)

        self.label_9 = QLabel(self.widgetDetail)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.cbPosition = QComboBox(self.widgetDetail)
        self.cbPosition.addItem("")
        self.cbPosition.addItem("")
        self.cbPosition.setObjectName(u"cbPosition")

        self.horizontalLayout_6.addWidget(self.cbPosition)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.widgetDetail)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.editNameIndex = QLineEdit(self.widgetDetail)
        self.editNameIndex.setObjectName(u"editNameIndex")

        self.horizontalLayout_7.addWidget(self.editNameIndex)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.line = QFrame(self.widgetDetail)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.widgetDetail)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.textContent = QTextEdit(self.widgetDetail)
        self.textContent.setObjectName(u"textContent")

        self.verticalLayout_3.addWidget(self.textContent)


        self.horizontalLayout.addWidget(self.widgetDetail)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widgetFunction = QWidget(self.centralwidget)
        self.widgetFunction.setObjectName(u"widgetFunction")

        self.verticalLayout.addWidget(self.widgetFunction)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuConfig = QMenu(self.menubar)
        self.menuConfig.setObjectName(u"menuConfig")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuConfig.addAction(self.actionConnection)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AwesomeDialog Generator - \u7edd\u7edd\u5b50\u5267\u60c5\u7f16\u8f91\u5668", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.actionConnection.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btnDel.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btnReorder.setText(QCoreApplication.translate("MainWindow", u"\u6392\u5e8f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u552f\u4e00ID", None))
        self.lbId.setText(QCoreApplication.translate("MainWindow", u"random string", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5f62\u5f0f", None))
        self.cbSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5bf9\u8bdd(\u975e\u7ed3\u5c3e)", None))
        self.cbSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
        self.cbSelect.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5bf9\u8bdd(\u7ed3\u5c3e)", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5e76\u5217\u7f16\u53f7", None))
        self.btnSameAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btnSameDel.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u7f16\u53f7", None))
        self.btnNextAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btnNextDel.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u7269\u540d\u79f0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u4f4d\u7f6e", None))
        self.cbPosition.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5de6", None))
        self.cbPosition.setItemText(1, QCoreApplication.translate("MainWindow", u"\u53f3", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u7269\u5934\u50cf", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5bb9", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menuConfig.setTitle(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
    # retranslateUi

