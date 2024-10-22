# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_pageXsknmJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(732, 429)
        Form.setMinimumSize(QSize(732, 429))
        Form.setMaximumSize(QSize(732, 429))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(681, 44))
        font = QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label = QLabel(Form)
        self.label.setObjectName(u"button")
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Se d\u00e9connecter", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Mention l\u00e9gales", None))
        self.label.setText(QCoreApplication.translate("Form", u"MangacollecQT v2.10.0 (101)", None))
    # retranslateUi

