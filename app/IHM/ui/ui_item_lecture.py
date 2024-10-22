# -*- coding: utf-8 -*-

################################################################################
## main_form generated from reading UI file 'item_lectureRiPlNt.ui'
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
        main_form.resize(732, 123)
        main_form.setMinimumSize(QSize(732, 123))
        main_form.setMaximumSize(QSize(732, 123))
        font = QFont()
        font.setFamily(u"Helvetica")
        main_form.setFont(font)
        main_form.setStyleSheet(u"""
                QWidget {
                    background: #FFF;
                }
                
                #item_progress_bar
                {
                    background: #e0e0e0;
                    color: #000;
                    border-radius: 5px;
                }
                
                #item_progress_bar::chunk
                {
                    background-color: #3d5afe;
                    border-radius: 5px;
                }
                
                #name_serie_label
                {
                    color: #1c1c1e;
                }
                
                #details_label
                {
                    color: #cf000a;
                }
                
                #details_label
                {
                    borde-colr: #000;
                	border-bottom: 1px;
                }
        """)
        
        self.main_layout = QHBoxLayout(main_form)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(9, 0, 9, 0)
        self.image_label = QLabel(main_form)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMinimumSize(QSize(70, 105))
        self.image_label.setMaximumSize(QSize(70, 105))
        self.image_label.setText(u"")
        self.image_label.setPixmap(QPixmap(u":/img/img/logo.png"))
        self.image_label.setScaledContents(True)

        self.main_layout.addWidget(self.image_label)

        self.horizontalSpacer = QSpacerItem(18, 18, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.main_layout.addItem(self.horizontalSpacer)

        self.info_vertical_layout = QVBoxLayout()
        self.info_vertical_layout.setObjectName(u"info_vertical_layout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.info_vertical_layout.addItem(self.verticalSpacer_4)

        self.name_serie_label = QLabel(main_form)
        self.name_serie_label.setObjectName(u"name_serie_label")
        self.name_serie_label.setMaximumSize(QSize(16777215, 20))
        self.name_serie_label.setSizeIncrement(QSize(0, 20))
        FONT_17 = QFont()
        FONT_17.setFamily(u"Helvetica")
        FONT_17.setPointSize(17)
        self.name_serie_label.setFont(FONT_17)

        self.info_vertical_layout.addWidget(self.name_serie_label)

        self.verticalSpacer = QSpacerItem(4, 4, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.info_vertical_layout.addItem(self.verticalSpacer)

        self.details_label = QLabel(main_form)
        self.details_label.setObjectName(u"details_label")
        self.details_label.setMinimumSize(QSize(0, 20))
        self.details_label.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamily(u"Helvetica")
        font2.setPointSize(14)
        self.details_label.setFont(font2)

        self.info_vertical_layout.addWidget(self.details_label)

        self.verticalSpacer_2 = QSpacerItem(4, 4, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.info_vertical_layout.addItem(self.verticalSpacer_2)

        self.item_progress_bar = QProgressBar(main_form)
        self.item_progress_bar.setObjectName(u"item_progress_bar")
        self.item_progress_bar.setMinimumSize(QSize(585, 10))
        self.item_progress_bar.setMaximumSize(QSize(585, 10))
        self.item_progress_bar.setValue(24)
        self.item_progress_bar.setAlignment(Qt.AlignCenter)
        self.item_progress_bar.setTextVisible(False)

        self.info_vertical_layout.addWidget(self.item_progress_bar)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.info_vertical_layout.addItem(self.verticalSpacer_3)

        self.line = QFrame(main_form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.info_vertical_layout.addWidget(self.line)


        self.main_layout.addLayout(self.info_vertical_layout)

        self.horizontalSpacer_2 = QSpacerItem(13, 13, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.main_layout.addItem(self.horizontalSpacer_2)

        self.label = QScrollArea(main_form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(10, 20))
        self.label.setMaximumSize(QSize(10, 20))
        self.label.setPixmap(QPixmap(u":/img/img/logo.png"))
        self.label.setScaledContents(True)

        self.main_layout.addWidget(self.label)


        self.retranslateUi(main_form)

        QMetaObject.connectSlotsByName(main_form)
    # setupUi

    def retranslateUi(self, main_form):
        main_form.setWindowTitle(QCoreApplication.translate("main_form", u"main_form", None))
        self.name_serie_label.setText(QCoreApplication.translate("main_form", u"17-21", None))
        self.details_label.setText(QCoreApplication.translate("main_form", u"0 / 1 tome", None))
        self.label.setText("")
    # retranslateUi

