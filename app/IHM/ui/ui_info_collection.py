# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_collectionwzBpuf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_InfoCollection(object):
    def setupUi(self, InfoCollection):
        if not InfoCollection.objectName():
            InfoCollection.setObjectName(u"InfoCollection")
        InfoCollection.resize(732, 108)
        InfoCollection.setMinimumSize(QSize(732, 108))
        InfoCollection.setMaximumSize(QSize(732, 108))
        self.main_layout = QHBoxLayout(InfoCollection)
        self.main_layout.setObjectName(u"main_layout")
        self.label_layout = QFormLayout()
        self.label_layout.setObjectName(u"label_layout")
        self.label_layout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_layout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_layout.setHorizontalSpacing(0)
        self.label_layout.setVerticalSpacing(0)
        self.value_tome = QLabel(InfoCollection)
        self.value_tome.setObjectName(u"value_tome")
        font = QFont()
        font.setFamily(u"Helvetica")
        font.setPointSize(42)
        self.value_tome.setFont(font)

        self.label_layout.setWidget(0, QFormLayout.LabelRole, self.value_tome)

        self.value_edition = QLabel(InfoCollection)
        self.value_edition.setObjectName(u"value_edition")
        font1 = QFont()
        font1.setFamily(u"Helvetica")
        font1.setPointSize(26)
        self.value_edition.setFont(font1)

        self.label_layout.setWidget(1, QFormLayout.LabelRole, self.value_edition)

        self.tome_label = QLabel(InfoCollection)
        self.tome_label.setObjectName(u"tome_label")
        self.tome_label.setFont(font1)

        self.label_layout.setWidget(0, QFormLayout.FieldRole, self.tome_label)

        self.edition_label = QLabel(InfoCollection)
        self.edition_label.setObjectName(u"edition_label")
        font2 = QFont()
        font2.setFamily(u"Helvetica")
        font2.setPointSize(16)
        self.edition_label.setFont(font2)

        self.label_layout.setWidget(1, QFormLayout.FieldRole, self.edition_label)


        self.main_layout.addLayout(self.label_layout)

        self.stat_button = QPushButton(InfoCollection)
        self.stat_button.setObjectName(u"stat_button")
        self.stat_button.setMinimumSize(QSize(57, 43))
        self.stat_button.setMaximumSize(QSize(57, 43))
        icon = QIcon()
        icon.addFile(u"../../assets/img/stat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stat_button.setIcon(icon)
        self.stat_button.setIconSize(QSize(14, 14))

        self.main_layout.addWidget(self.stat_button, 0, Qt.AlignRight|Qt.AlignTop)


        self.retranslateUi(InfoCollection)

        QMetaObject.connectSlotsByName(InfoCollection)
    # setupUi

    def retranslateUi(self, InfoCollection):
        InfoCollection.setWindowTitle(QCoreApplication.translate("InfoCollection", u"Form", None))
        self.value_tome.setText(QCoreApplication.translate("InfoCollection", u"1384", None))
        self.value_edition.setText(QCoreApplication.translate("InfoCollection", u"352", None))
        self.tome_label.setText(QCoreApplication.translate("InfoCollection", u"TOMES", None))
        self.edition_label.setText(QCoreApplication.translate("InfoCollection", u"Editions", None))
        self.stat_button.setText(QCoreApplication.translate("InfoCollection", u"STAT", None))
    # retranslateUi

