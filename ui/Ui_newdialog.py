# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogDialog(object):
    def setupUi(self, DialogDialog):
        if not DialogDialog.objectName():
            DialogDialog.setObjectName(u"DialogDialog")
        DialogDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(DialogDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(DialogDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lbId = QLabel(DialogDialog)
        self.lbId.setObjectName(u"lbId")

        self.horizontalLayout.addWidget(self.lbId)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(DialogDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.cbDialogType = QComboBox(DialogDialog)
        self.cbDialogType.addItem("")
        self.cbDialogType.addItem("")
        self.cbDialogType.setObjectName(u"cbDialogType")

        self.horizontalLayout_3.addWidget(self.cbDialogType)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(DialogDialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.editDialogTitle = QLineEdit(DialogDialog)
        self.editDialogTitle.setObjectName(u"editDialogTitle")

        self.horizontalLayout_4.addWidget(self.editDialogTitle)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(DialogDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(DialogDialog)

        self.cbDialogType.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(DialogDialog)
    # setupUi

    def retranslateUi(self, DialogDialog):
        DialogDialog.setWindowTitle(QCoreApplication.translate("DialogDialog", u"\u65b0\u5efa/\u7f16\u8f91\u5bf9\u8bdd", None))
        self.label.setText(QCoreApplication.translate("DialogDialog", u"\u552f\u4e00ID", None))
        self.lbId.setText(QCoreApplication.translate("DialogDialog", u"random_id", None))
        self.label_2.setText(QCoreApplication.translate("DialogDialog", u"\u5bf9\u8bdd\u7c7b\u578b", None))
        self.cbDialogType.setItemText(0, QCoreApplication.translate("DialogDialog", u"\u65c1\u767d\u5f0f\u5bf9\u8bdd", None))
        self.cbDialogType.setItemText(1, QCoreApplication.translate("DialogDialog", u"\u4e92\u52a8\u5f0f\u5bf9\u8bdd", None))

        self.label_3.setText(QCoreApplication.translate("DialogDialog", u"\u5bf9\u8bdd\u6807\u9898", None))
        self.btnSave.setText(QCoreApplication.translate("DialogDialog", u"\u4fdd\u5b58", None))
    # retranslateUi

