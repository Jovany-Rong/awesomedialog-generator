# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playerwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PlayerWindow(object):
    def setupUi(self, PlayerWindow):
        if not PlayerWindow.objectName():
            PlayerWindow.setObjectName(u"PlayerWindow")
        PlayerWindow.resize(800, 600)
        self.centralwidget = QWidget(PlayerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbSpeakerName = QLabel(self.centralwidget)
        self.lbSpeakerName.setObjectName(u"lbSpeakerName")

        self.verticalLayout.addWidget(self.lbSpeakerName)

        self.labelContent = QLabel(self.centralwidget)
        self.labelContent.setObjectName(u"labelContent")

        self.verticalLayout.addWidget(self.labelContent)

        self.widgetSelections = QWidget(self.centralwidget)
        self.widgetSelections.setObjectName(u"widgetSelections")

        self.verticalLayout.addWidget(self.widgetSelections)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCopy = QPushButton(self.centralwidget)
        self.btnCopy.setObjectName(u"btnCopy")

        self.horizontalLayout.addWidget(self.btnCopy)

        self.btnExport = QPushButton(self.centralwidget)
        self.btnExport.setObjectName(u"btnExport")

        self.horizontalLayout.addWidget(self.btnExport)


        self.verticalLayout.addLayout(self.horizontalLayout)

        PlayerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PlayerWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        PlayerWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PlayerWindow)
        self.statusbar.setObjectName(u"statusbar")
        PlayerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PlayerWindow)

        QMetaObject.connectSlotsByName(PlayerWindow)
    # setupUi

    def retranslateUi(self, PlayerWindow):
        PlayerWindow.setWindowTitle(QCoreApplication.translate("PlayerWindow", u"\u5bf9\u8bdd\u64ad\u653e\u5668", None))
        self.lbSpeakerName.setText(QCoreApplication.translate("PlayerWindow", u"TextLabel", None))
        self.labelContent.setText(QCoreApplication.translate("PlayerWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("PlayerWindow", u"\u5267\u60c5\u8bb0\u5f55", None))
        self.btnCopy.setText(QCoreApplication.translate("PlayerWindow", u"\u590d\u5236", None))
        self.btnExport.setText(QCoreApplication.translate("PlayerWindow", u"\u5bfc\u51fa", None))
    # retranslateUi

