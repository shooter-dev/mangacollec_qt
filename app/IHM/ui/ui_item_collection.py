# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_collectionThNvGp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_main_form(object):
    def setupUi(self, main_form):
        if not main_form.objectName():
            main_form.setObjectName(u"main_form")
        main_form.resize(732, 192)
        main_form.setMinimumSize(QSize(732, 192))
        main_form.setMaximumSize(QSize(732, 192))
        main_form.setStyleSheet(u"#QWidget {\n"
"	\n"
"	background-color: #FFF;\n"
"}\n"
"\n"
"#body {\n"
"	\n"
"	background-color: rgb(237, 237, 237);\n"
"}\n"
"\n"
"#name_serie_label {\n"
"	color: rgb(211, 30, 38);\n"
"}\n"
"\n"
"#info_label {\n"
"	color: rgb(119, 119, 119);\n"
"}")
        self.main_layout = QVBoxLayout(main_form)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.body = QWidget(main_form)
        self.body.setObjectName(u"body")

        self.body_layout = QVBoxLayout(self.body)
        self.body_layout.setSpacing(0)
        self.body_layout.setObjectName(u"body_layout")

        self.name_serie_label = QLabel(self.body)
        self.name_serie_label.setObjectName(u"name_serie_label")
        self.name_serie_label.setMinimumSize(QSize(0, 20))
        self.name_serie_label.setMaximumSize(QSize(16777215, 20))

        font = QFont()
        font.setFamily(u"Helvetica")
        font.setPointSize(17)

        self.name_serie_label.setFont(font)

        self.body_layout.addWidget(self.name_serie_label)

        self.info_label = QLabel(self.body)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setMinimumSize(QSize(0, 17))
        self.info_label.setMaximumSize(QSize(16777215, 17))

        self.body_layout.addWidget(self.info_label)

        self.tome_item_layout = QHBoxLayout()
        self.tome_item_layout.setSpacing(0)
        self.tome_item_layout.setObjectName(u"tome_item_layout")
        self.tome_item_layout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.tome_image_item_label = QLabel(self.body)
        self.tome_image_item_label.setObjectName(u"tome_image_item_label")
        self.tome_image_item_label.setMinimumSize(QSize(76, 114))
        self.tome_image_item_label.setMaximumSize(QSize(76, 114))
        self.tome_image_item_label.setBaseSize(QSize(76, 114))
        self.tome_image_item_label.setPixmap(QPixmap(u"../../assets/img/logo.png"))
        self.tome_image_item_label.setScaledContents(True)

        self.tome_item_layout.addWidget(self.tome_image_item_label, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.item_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tome_item_layout.addItem(self.item_spacer)


        self.body_layout.addLayout(self.tome_item_layout)


        self.main_layout.addWidget(self.body)


        self.retranslateUi(main_form)

        QMetaObject.connectSlotsByName(main_form)
    # setupUi

    def retranslateUi(self, main_form):
        main_form.setWindowTitle(QCoreApplication.translate("main_form", u"Form", None))
        self.name_serie_label.setText(QCoreApplication.translate("main_form", u"7th garden", None))
        self.info_label.setText(QCoreApplication.translate("main_form", u"8 / 8 \u2022 Edition en cours", None))
        self.tome_image_item_label.setText("")
    # retranslateUi

