# -*- coding: utf-8 -*-

################################################################################
## main_form generated from reading UI file 'info_lecture_volume_wigetUEuMql.ui'
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
        main_form.resize(699, 160)
        main_form.setMinimumSize(QSize(699, 141))
        main_form.setMaximumSize(QSize(699, 160))
        main_form.setStyleSheet(u"""
                QWidget  {
                        background-color:  #FFF;
                }
                
                #lecture_progress_bar
                {
                    background: #e0e0e0;
                    color: #000;
                    border-radius: 9px;
                }
                
                #lecture_progress_bar::chunk
                {
                    background-color: #3d5afe;
                    border-radius: 9px;
                }
        """)
        self.main_layout = QVBoxLayout(main_form)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(9, 0, 9, 0)
        self.vertical_spacer_20 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.main_layout.addItem(self.vertical_spacer_20)

        self.label_horizontal_layout = QHBoxLayout()
        self.label_horizontal_layout.setSpacing(0)
        self.label_horizontal_layout.setObjectName(u"label_horizontal_layout")
        self.tome_lus_vertical_layout = QVBoxLayout()
        self.tome_lus_vertical_layout.setObjectName(u"tome_lus_vertical_layout")
        self.value_tome_lus_label = QLabel(main_form)
        self.value_tome_lus_label.setObjectName(u"value_tome_lus_label")
        FONT_42 = QFont()
        FONT_42.setFamily(u"Helvetica")
        FONT_42.setPointSize(42)
        FONT_42.setBold(False)
        FONT_42.setWeight(50)
        self.value_tome_lus_label.setFont(FONT_42)

        self.tome_lus_vertical_layout.addWidget(self.value_tome_lus_label, 0, Qt.AlignLeft)

        self.name_tome_lus_label = QLabel(main_form)
        self.name_tome_lus_label.setObjectName(u"name_tome_lus_label")
        FONT_26 = QFont()
        FONT_26.setFamily(u"Helvetica")
        FONT_26.setPointSize(26)
        self.name_tome_lus_label.setFont(FONT_26)

        self.tome_lus_vertical_layout.addWidget(self.name_tome_lus_label, 0, Qt.AlignLeft)


        self.label_horizontal_layout.addLayout(self.tome_lus_vertical_layout)

        self.tome_a_lire_vertical_layout = QVBoxLayout()
        self.tome_a_lire_vertical_layout.setObjectName(u"tome_a_lire_vertical_layout")
        self.value_tome_a_lire_label = QLabel(main_form)
        self.value_tome_a_lire_label.setObjectName(u"value_tome_a_lire_label")
        FONT_42 = QFont()
        FONT_42.setFamily(u"Helvetica")
        FONT_42.setPointSize(42)
        self.value_tome_a_lire_label.setFont(FONT_42)
        self.value_tome_a_lire_label.setLayoutDirection(Qt.LeftToRight)

        self.tome_a_lire_vertical_layout.addWidget(self.value_tome_a_lire_label, 0, Qt.AlignRight)

        self.name_tome_a_lire_label = QLabel(main_form)
        self.name_tome_a_lire_label.setObjectName(u"name_tome_a_lire_label")
        self.name_tome_a_lire_label.setFont(FONT_26)

        self.tome_a_lire_vertical_layout.addWidget(self.name_tome_a_lire_label, 0, Qt.AlignRight)


        self.label_horizontal_layout.addLayout(self.tome_a_lire_vertical_layout)


        self.main_layout.addLayout(self.label_horizontal_layout)

        self.vertical_spacer_15 = QSpacerItem(15, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.main_layout.addItem(self.vertical_spacer_15)

        self.lecture_progress_bar = QProgressBar(main_form)
        self.lecture_progress_bar.setObjectName(u"lecture_progress_bar")
        self.lecture_progress_bar.setMinimumSize(QSize(681, 18))
        self.lecture_progress_bar.setMaximumSize(QSize(681, 18))
        FONT_26 = QFont()
        FONT_26.setFamily(u"Helvetica")
        FONT_26.setPointSize(15)
        self.lecture_progress_bar.setFont(FONT_26)
        self.lecture_progress_bar.setMaximum(100)
        self.lecture_progress_bar.setValue(46)
        self.lecture_progress_bar.setAlignment(Qt.AlignCenter)
        self.lecture_progress_bar.setTextVisible(True)
        self.lecture_progress_bar.setOrientation(Qt.Horizontal)

        self.main_layout.addWidget(self.lecture_progress_bar)

        self.vertical_spacer_20_1 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.main_layout.addItem(self.vertical_spacer_20_1)


        self.retranslateUi(main_form)

        QMetaObject.connectSlotsByName(main_form)
    # setupUi

    def retranslateUi(self, main_form):
        main_form.setWindowTitle(QCoreApplication.translate("main_form", u"main_form", None))
        self.value_tome_lus_label.setText(QCoreApplication.translate("main_form", u"810", None))
        self.name_tome_lus_label.setText(QCoreApplication.translate("main_form", u"TOMES LUS", None))
        self.value_tome_a_lire_label.setText(QCoreApplication.translate("main_form", u"948", None))
        self.name_tome_a_lire_label.setText(QCoreApplication.translate("main_form", u"TOMES \u00c0 LIRE", None))
    # retranslateUi

