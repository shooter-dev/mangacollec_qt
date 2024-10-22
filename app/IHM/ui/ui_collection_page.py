# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'collection_pagecEWWse.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(732, 429)
        Form.setMinimumSize(QSize(732, 429))
        Form.setMaximumSize(QSize(732, 429))
        Form.setStyleSheet(u"""QTabWidget::pane {{ /* The tab widget frame */
    border-top: 2px solid #C2C7CB;
    position: absolute;
    top: -0.5em;
}}

QTabWidget::tab-bar {{
    alignment: center;
}}

/* Style the tab using the tab sub-control. Note that
    it reads QTabBar _not_ QTabWidget */
QTabBar::tab {{
    background: #D3D3D3;
    border: 1px solid #C4C4C3;
    border-bottom-color: #C2C7CB; /* same as the pane color */
    border-radius: 17px;
    width:132px;
	min-height: 34px;
    margin: 6px
}}
QTabWidget::tab-bar:left {{
    padding: 6px
}}

QTabWidget::tab-bar:right {{
    padding: 6px
}}

QTabBar::tab:selected, QTabBar::tab:hover {{
    background: #BBB;
}}

QTabBar::tab:selected {{
    border-color: #CF000A;
	background-color: #CF000A;
}}""")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")

        self.tab = QWidget()
        self.tab.setObjectName(u"tab")

        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tabWidget.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab_5, "")

        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")

        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")

        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),   QCoreApplication.translate("Form", u"PILE A LIRE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"COLLECTION", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"CONPLETER", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"ENVIES", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"PRETS", None))
    # retranslateUi

