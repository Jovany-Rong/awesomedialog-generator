# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogSelectDialog(object):
    def setupUi(self, DialogSelectDialog):
        if not DialogSelectDialog.objectName():
            DialogSelectDialog.setObjectName(u"DialogSelectDialog")
        DialogSelectDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(DialogSelectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableDialogs = QTableView(DialogSelectDialog)
        self.tableDialogs.setObjectName(u"tableDialogs")

        self.verticalLayout.addWidget(self.tableDialogs)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnOpen = QPushButton(DialogSelectDialog)
        self.btnOpen.setObjectName(u"btnOpen")

        self.horizontalLayout.addWidget(self.btnOpen)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DialogSelectDialog)

        QMetaObject.connectSlotsByName(DialogSelectDialog)
    # setupUi

    def retranslateUi(self, DialogSelectDialog):
        DialogSelectDialog.setWindowTitle(QCoreApplication.translate("DialogSelectDialog", u"\u9009\u62e9\u5bf9\u8bdd", None))
        self.btnOpen.setText(QCoreApplication.translate("DialogSelectDialog", u"\u6253\u5f00", None))
    # retranslateUi

