# -*- coding: utf-8 -*-

################################################################################
## main_form generated from reading UI file 'designerMYVBpR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_form(object):
    def setupUi(self, main_form):
        if not main_form.objectName():
            main_form.setObjectName(u"main_form")
        main_form.resize(732, 429)
        main_form.setMinimumSize(QSize(732, 429))
        main_form.setMaximumSize(QSize(732, 429))
        self.verticalLayout = QVBoxLayout(main_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(main_form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(681, 44))
        self.font_12 = QFont()
        self.font_12.setPointSize(22)
        self.font_12.setBold(False)
        self.font_12.setWeight(50)
        self.font_12.setKerning(True)
        self.pushButton.setFont(self.font_12)
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.mention_legale_label = QLabel(main_form)
        self.mention_legale_label.setObjectName(u"mention_legale_label")
        self.font_121 = QFont()
        self.font_121.setPointSize(12)
        self.mention_legale_label.setFont(self.font_121)

        self.verticalLayout.addWidget(self.mention_legale_label, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.name_version_label = QLabel(main_form)
        self.name_version_label.setObjectName(u"button")
        self.name_version_label.setFont(self.font_121)

        self.verticalLayout.addWidget(self.name_version_label, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.retranslateUi(main_form)

        QMetaObject.connectSlotsByName(main_form)
    # setupUi

    def retranslateUi(self, main_form):
        main_form.setWindowTitle(QCoreApplication.translate("main_form", u"main_form", None))
        self.pushButton.setText(QCoreApplication.translate("main_form", u"Se d\u00e9connecter", None))
        self.mention_legale_label.setText(QCoreApplication.translate("main_form", u"Mention l\u00e9gales", None))
        self.name_version_label.setText(QCoreApplication.translate("main_form", u"MangacollecQT v2.10.0 (101)", None))
    # retranslateUi

