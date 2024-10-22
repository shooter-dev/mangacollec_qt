from typing import Any

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout

from shooterQT.lib.ui_interface import UiInterface


class Ui_ItemCollection(UiInterface):
    def init(self, main_form: QWidget):
        size = QSize(732, 192)
        main_form.setMinimumSize(size)
        main_form.setMaximumSize(size)
        main_form.setStyleSheet(u"""
            #QWidget {
                
                background-color: #FFF;
            }
            
            #body {
                
                background-color: rgb(237, 237, 237);
            }
            
            #name_serie_label {
                color: rgb(211, 30, 38);
            }
            
            #info_label {
                color: rgb(119, 119, 119);
        }""")

    def create_widgets(self, main_form: QWidget) -> Any:
        self.body = QWidget(main_form)
        self.body.setObjectName(u"body")

        self.name_serie_label = QLabel(self.body)
        self.name_serie_label.setObjectName(u"name_serie_label")

        self.info_label = QLabel(self.body)
        self.info_label.setObjectName(u"info_label")

        self.tome_image_item_label = QLabel(self.body)
        self.tome_image_item_label.setObjectName(u"tome_image_item_label")

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.tome_image_item_label.setMinimumSize(QSize(76, 114))
        self.tome_image_item_label.setMaximumSize(QSize(76, 114))
        self.tome_image_item_label.setPixmap(QPixmap(u"../../assets/img/logo.png"))
        self.tome_image_item_label.setScaledContents(True)

    def create_layouts(self, main_form: QWidget) -> Any:
        self.body_layout = QVBoxLayout(self.body)
        self.body_layout.setObjectName(u"body_layout")
        self.body_layout.setSpacing(0)

        self.tome_item_layout = QHBoxLayout()
        self.tome_item_layout.setObjectName(u"tome_item_layout")
        self.tome_item_layout.setSpacing(0)

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.body_layout.addWidget(self.name_serie_label)
        self.body_layout.addWidget(self.info_label)
        self.tome_item_layout.addWidget(self.tome_image_item_label, 0, Qt.AlignVCenter)

        self.body_layout.addLayout(self.tome_item_layout)

        self.main_layout.addWidget(self.body)


    def setup_connections(self, main_form: QWidget) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass