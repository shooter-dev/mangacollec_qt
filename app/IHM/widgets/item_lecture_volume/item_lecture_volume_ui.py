from typing import Any

from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QProgressBar, QFrame

from app.src.utils.const import FONT_17, SPACER_4_V, FONT_14, SPACER_18_H, SPACER_13_H
from app.src.utils.pages_utils import PagesUtils
from app.IHM.widgets.menu.lectureitemcontextmenu import LectureItemContextMenu
from shooterQT.lib.ui_interface import UiInterface


class ItemLectureVolumeUI(UiInterface):
    def init(self, main_form: QWidget):
        size = QSize(708, 123)
        main_form.setMinimumSize(size)
        main_form.setMaximumSize(size)
        main_form.setObjectName("ItemLectureVolumeUI")
        main_form.setCursor(QCursor(Qt.PointingHandCursor))
        main_form.setStyleSheet(f"""
            QWidget {{
                background-color: {PagesUtils.generer_random_color_hex()};
            }}
    
            #progress_bar
            {{
                background: #e0e0e0;
                color: #000;
                border-radius: 4px;
            }}
    
            #progress_bar::chunk
            {{
                background-color: #3d5afe;
                border-radius: 4px;
            }}
    
            #name_serie_label
            {{
                color: #1c1c1e;
            }}
    
            #details_label
            {{
                color: #cf000a;
            }}
            Line {{
                background-color: #000;
            }}
        """)

    def create_widgets(self, main_form: QWidget) -> Any:
        self.image_label = QLabel(main_form)
        self.image_label.setObjectName(u"image_label")

        self.name_serie_label = QLabel(main_form)
        self.name_serie_label.setObjectName(u"name_serie_label")

        self.details_label = QLabel(main_form)
        self.details_label.setObjectName(u"details_label")

        self.progress_bar = QProgressBar(main_form)
        self.progress_bar.setObjectName(u"progress_bar")

        self.line = QFrame(main_form)
        self.line.setObjectName(u"line")

        self.label_ico = QLabel(main_form)
        self.label_ico.setObjectName(u"label")

        self.menu_lecture_item = LectureItemContextMenu(main_form)




    def modify_widgets(self, main_form: QWidget) -> Any:
        self.image_label.setMinimumSize(QSize(70, 105))
        self.image_label.setMaximumSize(QSize(70, 105))
        self.image_label.setScaledContents(True)

        self.name_serie_label.setMinimumSize(QSize(585, 20))
        self.name_serie_label.setMaximumSize(QSize(585, 20))
        self.name_serie_label.setFont(FONT_17)

        self.details_label.setMinimumSize(QSize(585, 20))
        self.details_label.setMaximumSize(QSize(585, 20))
        self.details_label.setFont(FONT_14)

        self.progress_bar.setMinimumSize(QSize(585, 10))
        self.progress_bar.setMaximumSize(QSize(585, 10))
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setTextVisible(False)

        self.line.setMinimumSize(QSize(585, 1))
        self.line.setMaximumSize(QSize(585, 1))
        self.line.setFrameShape(QFrame.NoFrame)
        self.line.setFrameShadow(QFrame.Plain)

        self.label_ico.setMinimumSize(QSize(10, 20))
        self.label_ico.setMaximumSize(QSize(10, 20))
        self.label_ico.setPixmap(QPixmap(u":/img/img/logo.png"))
        self.label_ico.setScaledContents(True)

        main_form.setContextMenuPolicy(Qt.CustomContextMenu)

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(9, 0, 9, 0)

        self.info_vertical_layout = QVBoxLayout()
        self.info_vertical_layout.setObjectName(u"info_vertical_layout")

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addItem(SPACER_18_H)

        self.info_vertical_layout.addItem(SPACER_4_V)
        self.info_vertical_layout.addWidget(self.name_serie_label)
        self.info_vertical_layout.addItem(SPACER_4_V)
        self.info_vertical_layout.addWidget(self.details_label)
        self.info_vertical_layout.addItem(SPACER_4_V)
        self.info_vertical_layout.addWidget(self.progress_bar)

        self.info_vertical_layout.addItem(SPACER_4_V)

        self.info_vertical_layout.addWidget(self.line)

        self.main_layout.addLayout(self.info_vertical_layout)

        self.main_layout.addItem(SPACER_13_H)

        self.main_layout.addWidget(self.label_ico)

    def retranslate_ui(self, main_form: QWidget) -> Any:
        main_form.setWindowTitle(QCoreApplication.translate("main_form", u"main_form", None))
        self.name_serie_label.setText(QCoreApplication.translate("main_form", u"17-21", None))
        self.details_label.setText(QCoreApplication.translate("main_form", u"0 / 1 tome", None))
        self.label_ico.setText("")