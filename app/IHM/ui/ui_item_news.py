# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_newsZfWsKF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_ItemNewsItem(object):
    def setupUi(self, ItemNewsItem):
        if not ItemNewsItem.objectName():
            ItemNewsItem.setObjectName(u"ItemNewsItem")
        ItemNewsItem.resize(238, 391)
        ItemNewsItem.setMinimumSize(QSize(238, 391))
        ItemNewsItem.setMaximumSize(QSize(238, 391))
        ItemNewsItem.setStyleSheet(u"")
        self.main_layout = QVBoxLayout(ItemNewsItem)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(9, 9, 9, 9)
        self.image_volume_label = QLabel(ItemNewsItem)
        self.image_volume_label.setObjectName(u"image_volume_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_volume_label.sizePolicy().hasHeightForWidth())
        self.image_volume_label.setSizePolicy(sizePolicy)
        self.image_volume_label.setMinimumSize(QSize(220, 330))
        self.image_volume_label.setMaximumSize(QSize(220, 330))
        self.image_volume_label.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 9px;\n"
"border-image-repeat: stretch;\n"
"align-items: stretch;\n"
"box-sizing: border-box;\n"
"z-index: 0;\n"
"\n"
"")
        self.image_volume_label.setFrameShape(QFrame.NoFrame)
        self.image_volume_label.setFrameShadow(QFrame.Plain)
        self.image_volume_label.setTextFormat(Qt.AutoText)
        self.image_volume_label.setPixmap(QPixmap(u"../../assets/img/logo.png"))
        self.image_volume_label.setScaledContents(True)
        self.image_volume_label.setAlignment(Qt.AlignCenter)
        self.image_volume_label.setWordWrap(False)
        self.image_volume_label.setMargin(0)
        self.image_volume_label.setIndent(-1)
        self.image_volume_label.setOpenExternalLinks(False)

        self.main_layout.addWidget(self.image_volume_label, 0, Qt.AlignHCenter)

        self.vertical_spacer_4 = QSpacerItem(4, 4, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.main_layout.addItem(self.vertical_spacer_4)

        self.name_serie_label = QLabel(ItemNewsItem)
        self.name_serie_label.setObjectName(u"name_serie_label")
        self.name_serie_label.setMinimumSize(QSize(220, 20))
        self.name_serie_label.setMaximumSize(QSize(220, 20))
        font = QFont()
        font.setPointSize(17)
        self.name_serie_label.setFont(font)

        self.main_layout.addWidget(self.name_serie_label, 0, Qt.AlignHCenter)

        self.vertical_spacer_2 = QSpacerItem(2, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.main_layout.addItem(self.vertical_spacer_2)

        self.info_horizontal_layout = QHBoxLayout()
        self.info_horizontal_layout.setSpacing(9)
        self.info_horizontal_layout.setObjectName(u"info_horizontal_layout")
        self.name_tome_label = QLabel(ItemNewsItem)
        self.name_tome_label.setObjectName(u"name_tome_label")
        self.name_tome_label.setMinimumSize(QSize(0, 17))
        self.name_tome_label.setMaximumSize(QSize(16777215, 17))
        font1 = QFont()
        font1.setPointSize(14)
        self.name_tome_label.setFont(font1)

        self.info_horizontal_layout.addWidget(self.name_tome_label, 0, Qt.AlignLeft)

        self.sponso_label = QLabel(ItemNewsItem)
        self.sponso_label.setObjectName(u"sponso_label")
        self.sponso_label.setMinimumSize(QSize(0, 17))
        self.sponso_label.setMaximumSize(QSize(100, 17))
        font2 = QFont()
        font2.setPointSize(8)
        self.sponso_label.setFont(font2)
        self.sponso_label.setLayoutDirection(Qt.LeftToRight)
        self.sponso_label.setAutoFillBackground(False)
        self.sponso_label.setStyleSheet(u"border-color: rgb(28, 28, 30);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"padding-left: 4px;\n"
"padding-right: 4px;\n"
"\n"
"text-decoration-color: rgb(28, 28, 30);")
        self.sponso_label.setInputMethodHints(Qt.ImhNone)
        self.sponso_label.setFrameShadow(QFrame.Sunken)
        self.sponso_label.setScaledContents(True)
        self.sponso_label.setAlignment(Qt.AlignCenter)
        self.sponso_label.setWordWrap(False)
        self.sponso_label.setOpenExternalLinks(False)

        self.info_horizontal_layout.addWidget(self.sponso_label)


        self.main_layout.addLayout(self.info_horizontal_layout)


        self.retranslateUi(ItemNewsItem)

        QMetaObject.connectSlotsByName(ItemNewsItem)
    # setupUi

    def retranslateUi(self, ItemNewsItem):
        ItemNewsItem.setWindowTitle(QCoreApplication.translate("ItemNewsItem", u"Form", None))
        self.image_volume_label.setText("")
        self.name_serie_label.setText(QCoreApplication.translate("ItemNewsItem", u"My Love Story With Yamad...", None))
        self.name_tome_label.setText(QCoreApplication.translate("ItemNewsItem", u"Tome 1", None))
        self.sponso_label.setText(QCoreApplication.translate("ItemNewsItem", u"SPONSORIS\u00c9", None))
    # retranslateUi

