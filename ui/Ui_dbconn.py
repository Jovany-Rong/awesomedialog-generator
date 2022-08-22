# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dbconn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DbDialog(object):
    def setupUi(self, DbDialog):
        if not DbDialog.objectName():
            DbDialog.setObjectName(u"DbDialog")
        DbDialog.resize(400, 300)
        self.verticalLayout_3 = QVBoxLayout(DbDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DbDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(DbDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(DbDialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(DbDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(DbDialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(DbDialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cbDbType = QComboBox(DbDialog)
        self.cbDbType.addItem("")
        self.cbDbType.setObjectName(u"cbDbType")

        self.verticalLayout_2.addWidget(self.cbDbType)

        self.editHost = QLineEdit(DbDialog)
        self.editHost.setObjectName(u"editHost")

        self.verticalLayout_2.addWidget(self.editHost)

        self.spinPort = QSpinBox(DbDialog)
        self.spinPort.setObjectName(u"spinPort")
        self.spinPort.setMinimum(1)
        self.spinPort.setMaximum(65535)
        self.spinPort.setValue(3306)

        self.verticalLayout_2.addWidget(self.spinPort)

        self.editDatabase = QLineEdit(DbDialog)
        self.editDatabase.setObjectName(u"editDatabase")

        self.verticalLayout_2.addWidget(self.editDatabase)

        self.editUsername = QLineEdit(DbDialog)
        self.editUsername.setObjectName(u"editUsername")

        self.verticalLayout_2.addWidget(self.editUsername)

        self.editPassword = QLineEdit(DbDialog)
        self.editPassword.setObjectName(u"editPassword")
        self.editPassword.setEchoMode(QLineEdit.Password)
        self.editPassword.setReadOnly(False)

        self.verticalLayout_2.addWidget(self.editPassword)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnTest = QPushButton(DbDialog)
        self.btnTest.setObjectName(u"btnTest")

        self.horizontalLayout.addWidget(self.btnTest)

        self.btnSave = QPushButton(DbDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(DbDialog)

        QMetaObject.connectSlotsByName(DbDialog)
    # setupUi

    def retranslateUi(self, DbDialog):
        DbDialog.setWindowTitle(QCoreApplication.translate("DbDialog", u"\u6570\u636e\u5e93\u8fde\u63a5\u914d\u7f6e", None))
        self.label.setText(QCoreApplication.translate("DbDialog", u"\u8fde\u63a5\u7c7b\u578b", None))
        self.label_2.setText(QCoreApplication.translate("DbDialog", u"\u670d\u52a1\u5668", None))
        self.label_3.setText(QCoreApplication.translate("DbDialog", u"\u7aef\u53e3", None))
        self.label_4.setText(QCoreApplication.translate("DbDialog", u"\u6570\u636e\u5e93", None))
        self.label_5.setText(QCoreApplication.translate("DbDialog", u"\u7528\u6237\u540d", None))
        self.label_6.setText(QCoreApplication.translate("DbDialog", u"\u5bc6\u7801", None))
        self.cbDbType.setItemText(0, QCoreApplication.translate("DbDialog", u"MySQL", None))

        self.btnTest.setText(QCoreApplication.translate("DbDialog", u"\u6d4b\u8bd5", None))
        self.btnSave.setText(QCoreApplication.translate("DbDialog", u"\u4fdd\u5b58", None))
    # retranslateUi

