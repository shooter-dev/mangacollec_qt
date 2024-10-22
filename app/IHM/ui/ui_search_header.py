# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_headereuWPAH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Search(object):
    def setupUi(self, Search):
        if not Search.objectName():
            Search.setObjectName(u"Search")
        Search.resize(732, 51)
        Search.setMinimumSize(QSize(732, 51))
        Search.setMaximumSize(QSize(732, 51))
        Search.setStyleSheet(u"#search_line_edit {\n"
"	border: 1px solid rgb(224, 224, 224);\n"
"	border-radius: 17px;\n"
"	padding-left: 38px;\n"
"	padding-right: 38px;\n"
"}\n"
"\n"
"#search_line_edit:focus {\n"
"	border: 2px solid #3d5afe;\n"
"	border-radius: 5px;\n"
"}")
        self.main_layout = QHBoxLayout(Search)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(12, 8, 18, 8)

        self.search_line_edit = QLineEdit(Search)
        self.search_line_edit.setObjectName(u"search_line_edit")
        self.search_line_edit.setMinimumSize(QSize(652, 34))
        self.search_line_edit.setMaximumSize(QSize(652, 34))

        font = QFont()
        font.setFamily(u"Helvetica")
        font.setPointSize(16)

        self.search_line_edit.setFont(font)
        self.search_line_edit.setClearButtonEnabled(True)

        self.main_layout.addWidget(self.search_line_edit, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.trie_button = QPushButton(Search)
        self.trie_button.setObjectName(u"trie_button")
        self.trie_button.setMinimumSize(QSize(32, 32))
        self.trie_button.setMaximumSize(QSize(32, 32))

        icon = QIcon()
        icon.addFile(u"../../../../../../Downloads/trie.png", QSize(), QIcon.Normal, QIcon.Off)

        self.trie_button.setIcon(icon)
        self.trie_button.setIconSize(QSize(32, 32))

        self.main_layout.addWidget(self.trie_button, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.retranslateUi(Search)

        QMetaObject.connectSlotsByName(Search)
    # setupUi

    def retranslateUi(self, Search):
        Search.setWindowTitle(QCoreApplication.translate("Search", u"Form", None))
        self.search_line_edit.setPlaceholderText(QCoreApplication.translate("Search", u"Rechercher dans la collection", None))
        self.trie_button.setText("")
    # retranslateUi

