# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'textimporter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ImportFromTextDialog(object):
    def setupUi(self, ImportFromTextDialog):
        if not ImportFromTextDialog.objectName():
            ImportFromTextDialog.setObjectName(u"ImportFromTextDialog")
        ImportFromTextDialog.resize(600, 300)
        self.horizontalLayout_9 = QHBoxLayout(ImportFromTextDialog)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnSelect = QPushButton(ImportFromTextDialog)
        self.btnSelect.setObjectName(u"btnSelect")

        self.horizontalLayout.addWidget(self.btnSelect)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(ImportFromTextDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.lbFilePath = QLabel(ImportFromTextDialog)
        self.lbFilePath.setObjectName(u"lbFilePath")

        self.verticalLayout_2.addWidget(self.lbFilePath)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(ImportFromTextDialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.cbCoding = QComboBox(ImportFromTextDialog)
        self.cbCoding.addItem("")
        self.cbCoding.addItem("")
        self.cbCoding.setObjectName(u"cbCoding")

        self.horizontalLayout_3.addWidget(self.cbCoding)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(ImportFromTextDialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.cbSeperate = QComboBox(ImportFromTextDialog)
        self.cbSeperate.addItem("")
        self.cbSeperate.addItem("")
        self.cbSeperate.setObjectName(u"cbSeperate")

        self.horizontalLayout_4.addWidget(self.cbSeperate)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(ImportFromTextDialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.cbSpeaker = QComboBox(ImportFromTextDialog)
        self.cbSpeaker.addItem("")
        self.cbSpeaker.addItem("")
        self.cbSpeaker.setObjectName(u"cbSpeaker")

        self.horizontalLayout_5.addWidget(self.cbSpeaker)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(ImportFromTextDialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.editIsSelect = QLineEdit(ImportFromTextDialog)
        self.editIsSelect.setObjectName(u"editIsSelect")

        self.horizontalLayout_6.addWidget(self.editIsSelect)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(ImportFromTextDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.textBrowser = QTextBrowser(ImportFromTextDialog)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.btnImport = QPushButton(ImportFromTextDialog)
        self.btnImport.setObjectName(u"btnImport")

        self.horizontalLayout_8.addWidget(self.btnImport)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)

        self.retranslateUi(ImportFromTextDialog)

        QMetaObject.connectSlotsByName(ImportFromTextDialog)
    # setupUi

    def retranslateUi(self, ImportFromTextDialog):
        ImportFromTextDialog.setWindowTitle(QCoreApplication.translate("ImportFromTextDialog", u"\u4ece\u6587\u672c\u6587\u4ef6\u5bfc\u5165", None))
        self.btnSelect.setText(QCoreApplication.translate("ImportFromTextDialog", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("ImportFromTextDialog", u"\u6587\u4ef6\u8def\u5f84", None))
        self.lbFilePath.setText(QCoreApplication.translate("ImportFromTextDialog", u"null", None))
        self.label_3.setText(QCoreApplication.translate("ImportFromTextDialog", u"\u7f16\u7801\u683c\u5f0f", None))
        self.cbCoding.setItemText(0, QCoreApplication.translate("ImportFromTextDialog", u"UTF-8", None))
        self.cbCoding.setItemText(1, QCoreApplication.translate("ImportFromTextDialog", u"gb2312", None))

        self.label_4.setText(QCoreApplication.translate("ImportFromTextDialog", u"\u5206\u5272\u6807\u8bc6", None))
        self.cbSeperate.setItemText(0, QCoreApplication.translate("ImportFromTextDialog", u"\u6362\u884c", None))
        self.cbSeperate.setItemText(1, QCoreApplication.translate("ImportFromTextDialog", u"\u6362\u4e24\u884c", None))

        self.label_5.setText(QCoreApplication.translate("ImportFromTextDialog", u"\u8bf4\u8bdd\u4eba\u6807\u8bc6", None))
        self.cbSpeaker.setItemText(0, QCoreApplication.translate("ImportFromTextDialog", u"\u3010\u8bf4\u8bdd\u4eba\u3011", None))
        self.cbSpeaker.setItemText(1, QCoreApplication.translate("ImportFromTextDialog", u"\u8bf4\u8bdd\u4eba\uff1a", None))

        self.label_6.setText(QCoreApplication.translate("ImportFromTextDialog", u"\u9009\u9879\u6807\u8bc6", None))
        self.editIsSelect.setText(QCoreApplication.translate("ImportFromTextDialog", u"${select}", None))
        self.label.setText(QCoreApplication.translate("ImportFromTextDialog", u"\u5185\u5bb9\u9884\u89c8", None))
        self.btnImport.setText(QCoreApplication.translate("ImportFromTextDialog", u"\u5bfc\u5165", None))
    # retranslateUi

