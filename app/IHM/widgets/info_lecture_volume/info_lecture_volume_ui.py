from typing import Any

from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QProgressBar

from app.src.utils.const import SPACER_20_V, FONT_42, FONT_26, SPACER_15_V, FONT_16, FONT_12
from shooterQT.lib.ui_interface import UiInterface


class InfoLectureVolumeUI(UiInterface):
    def init(self, main_form: QWidget):
        size = QSize(708, 141)
        main_form.setMinimumSize(size)
        main_form.setMaximumSize(size)
        main_form.setStyleSheet(u"""
                        QWidget  {
                                background-color:  #FFF;
                        }

                        #lecture_progress_bar
                        {
                            background: #e0e0e0;
                            color: #FFF;
                            border-radius: 9px;
                        }

                        #lecture_progress_bar::chunk
                        {
                            background-color: #3d5afe;
                            border-radius: 9px;
                        }
                """)

    def create_widgets(self, main_form: QWidget) -> Any:
        self.value_tome_lus_label = QLabel(main_form)
        self.value_tome_lus_label.setObjectName(u"value_tome_lus_label")

        self.name_tome_lus_label = QLabel(main_form)
        self.name_tome_lus_label.setObjectName(u"name_tome_lus_label")

        self.value_tome_a_lire_label = QLabel(main_form)
        self.value_tome_a_lire_label.setObjectName(u"value_tome_a_lire_label")

        self.name_tome_a_lire_label = QLabel(main_form)
        self.name_tome_a_lire_label.setObjectName(u"name_tome_a_lire_label")

        self.lecture_progress_bar = QProgressBar(main_form)
        self.lecture_progress_bar.setObjectName(u"lecture_progress_bar")

    def modify_widgets(self, main_form: QWidget) -> Any:

        self.value_tome_lus_label.setFont(FONT_42)

        self.name_tome_lus_label.setFont(FONT_26)

        self.value_tome_a_lire_label.setFont(FONT_42)

        self.name_tome_a_lire_label.setFont(FONT_26)

        self.value_tome_a_lire_label.setLayoutDirection(Qt.LeftToRight)

        # self.lecture_progress_bar.setMinimumSize(QSize(681, 18))
        # self.lecture_progress_bar.setMaximumSize(QSize(681, 18))
        self.lecture_progress_bar.setFont(FONT_12)
        self.lecture_progress_bar.setMaximum(100)
        self.lecture_progress_bar.setValue(46)
        self.lecture_progress_bar.setAlignment(Qt.AlignCenter)
        self.lecture_progress_bar.setTextVisible(True)
        self.lecture_progress_bar.setOrientation(Qt.Horizontal)


    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(18, 20, 18, 20)

        self.label_horizontal_layout = QHBoxLayout()
        self.label_horizontal_layout.setSpacing(0)
        self.label_horizontal_layout.setObjectName(u"label_horizontal_layout")

        self.tome_lus_vertical_layout = QVBoxLayout()
        self.tome_lus_vertical_layout.setObjectName(u"tome_lus_vertical_layout")

        self.tome_a_lire_vertical_layout = QVBoxLayout()
        self.tome_a_lire_vertical_layout.setObjectName(u"tome_a_lire_vertical_layout")

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        #self.main_layout.addItem(SPACER_20_V)

        self.tome_lus_vertical_layout.addWidget(self.value_tome_lus_label, 0, Qt.AlignLeft)
        self.tome_lus_vertical_layout.addWidget(self.name_tome_lus_label, 0, Qt.AlignLeft)

        self.label_horizontal_layout.addLayout(self.tome_lus_vertical_layout)

        self.tome_a_lire_vertical_layout.addWidget(self.value_tome_a_lire_label, 0, Qt.AlignRight)
        self.tome_a_lire_vertical_layout.addWidget(self.name_tome_a_lire_label, 0, Qt.AlignRight)

        self.label_horizontal_layout.addLayout(self.tome_a_lire_vertical_layout)
        self.main_layout.addLayout(self.label_horizontal_layout)

        self.main_layout.addItem(SPACER_15_V)
        self.main_layout.addWidget(self.lecture_progress_bar)

        #self.main_layout.addItem(SPACER_20_V)


    def setup_connections(self, main_form: QWidget) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        main_form.setWindowTitle(QCoreApplication.translate("main_form", u"main_form", None))
        self.value_tome_lus_label.setText(QCoreApplication.translate("main_form", u"810", None))
        self.name_tome_lus_label.setText(QCoreApplication.translate("main_form", u"TOMES LUS", None))
        self.value_tome_a_lire_label.setText(QCoreApplication.translate("main_form", u"948", None))
        self.name_tome_a_lire_label.setText(QCoreApplication.translate("main_form", u"TOMES \u00c0 LIRE", None))
