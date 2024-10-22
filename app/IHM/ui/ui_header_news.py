# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'header_newsQjIlgt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_HeaderNews(object):
    def setupUi(self, HeaderNews):
        if not HeaderNews.objectName():
            HeaderNews.setObjectName(u"HeaderNews")
        HeaderNews.resize(714, 51)
        HeaderNews.setMinimumSize(QSize(714, 51))
        HeaderNews.setMaximumSize(QSize(714, 51))
        HeaderNews.setStyleSheet(u"border-width: 2px;\n"
"	border-bottom-color: black;\n"
"    border-bottom-style: solid;")
        self.main_layout = QHBoxLayout(HeaderNews)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(-1, 0, -1, 0)
        self.name_page_label = QLabel(HeaderNews)
        self.name_page_label.setObjectName(u"name_page_label")
        self.name_page_label.setMinimumSize(QSize(0, 21))
        self.name_page_label.setMaximumSize(QSize(16777215, 21))
        font = QFont()
        font.setFamily(u"Helvetica")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name_page_label.setFont(font)

        self.main_layout.addWidget(self.name_page_label, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.publisher_combo_box = QComboBox(HeaderNews)
        icon = QIcon()
        icon.addFile(u":/img/img/logo.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.publisher_combo_box.addItem(icon, "")
        self.publisher_combo_box.addItem("")
        self.publisher_combo_box.addItem("")
        self.publisher_combo_box.addItem("")
        self.publisher_combo_box.addItem("")
        self.publisher_combo_box.addItem("")
        self.publisher_combo_box.addItem("")
        self.publisher_combo_box.addItem("")
        self.publisher_combo_box.addItem("")
        self.publisher_combo_box.addItem("")
        self.publisher_combo_box.setObjectName(u"publisher_combo_box")
        self.publisher_combo_box.setMinimumSize(QSize(100, 28))
        self.publisher_combo_box.setMaximumSize(QSize(223, 28))
        font1 = QFont()
        font1.setFamily(u"Helvetica")
        font1.setPointSize(17)
        font1.setBold(False)
        font1.setWeight(50)
        self.publisher_combo_box.setFont(font1)
        self.publisher_combo_box.setLayoutDirection(Qt.LeftToRight)
        self.publisher_combo_box.setAutoFillBackground(True)
        self.publisher_combo_box.setStyleSheet(u"#publisher_combo_box {\n"
"	border: 1px solid #000;\n"
"	border-radius: 4px;\n"
"	padding-left:10px;\n"
"}\n"
"\n"
"#publisher_combo_box::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"#publisher_combo_box::drop-arrow {	\n"
"	image: url(:/icons/icons/red/arrow-down.svg);\n"
"	width: 28px;\n"
"	height 14px;\n"
"	margin-right: 15px;\n"
"}\n"
"\n"
"#publisher_combo_box:on {\n"
"	border: 4px solid #000;\n"
"}\n"
"\n"
"#publisher_combo_box QListView {\n"
"	font-size: 17px;\n"
"	border: 1px solid rgba(0, 0,0,10%);\n"
"	padding: 5px;\n"
"	background-color: #FFF;\n"
"	outline: 0px;\n"
"\n"
"	width: 280px;\n"
"}\n"
"\n"
"#publisher_combo_box QListView::item {\n"
"	padding-left: 10px;\n"
"	background-color: #FFF;\n"
"	font-size: 17px;\n"
"	width: 28px;\n"
"	height 14px;\n"
"}\n"
"\n"
"#publisher_combo_box QListView::item:hover {\n"
"	background-color: #BBB;\n"
"}\n"
"\n"
"#publisher_combo_box QListView::item:selected {\n"
"	background-color: #BBB;\n"
"}\n"
"\n"
"")
        self.publisher_combo_box.setMaxVisibleItems(9)
        self.publisher_combo_box.setIconSize(QSize(20, 16))

        self.main_layout.addWidget(self.publisher_combo_box, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.retranslateUi(HeaderNews)

        self.publisher_combo_box.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(HeaderNews)
    # setupUi

    def retranslateUi(self, HeaderNews):
        HeaderNews.setWindowTitle(QCoreApplication.translate("HeaderNews", u"Form", None))
        self.name_page_label.setText(QCoreApplication.translate("HeaderNews", u"Nouveaut\u00e9s", None))
        self.publisher_combo_box.setItemText(0, QCoreApplication.translate("HeaderNews", u"Editeurs", None))
        self.publisher_combo_box.setItemText(1, QCoreApplication.translate("HeaderNews", u"Akata", None))
        self.publisher_combo_box.setItemText(2, QCoreApplication.translate("HeaderNews", u"Ankama", None))
        self.publisher_combo_box.setItemText(3, QCoreApplication.translate("HeaderNews", u"Asuka", None))
        self.publisher_combo_box.setItemText(4, QCoreApplication.translate("HeaderNews", u"Auto-Edition", None))
        self.publisher_combo_box.setItemText(5, QCoreApplication.translate("HeaderNews", u"Black Blox", None))
        self.publisher_combo_box.setItemText(6, QCoreApplication.translate("HeaderNews", u"Bookmark", None))
        self.publisher_combo_box.setItemText(7, QCoreApplication.translate("HeaderNews", u"Clair de Lune", None))
        self.publisher_combo_box.setItemText(8, QCoreApplication.translate("HeaderNews", u"Crunchyroll/Kaz\u00e9", None))
        self.publisher_combo_box.setItemText(9, QCoreApplication.translate("HeaderNews", u"Delcourt/Tonkam", None))

        self.publisher_combo_box.setCurrentText(QCoreApplication.translate("HeaderNews", u"Editeurs", None))
    # retranslateUi

