from typing import Any

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout

from app.src.utils.const import STYLE_SCROLL_BAR
from app.src.utils.debug import widget_taille
from app.IHM.widgets.info_lecture_volume.info_lecture_volume import InfoLectureVolume
from shooterQT.lib.ui_interface import UiInterface


class Ui_PileALire(UiInterface):
    def init(self, main_form: QWidget):
        size = QSize(732,429)
        main_form.setMinimumSize(size)
        main_form.setMaximumSize(size)
        main_form.setObjectName("Ui_PileALire")
        widget_taille(main_form)
        main_form.setStyleSheet(U"""
        
        """)

    def create_widgets(self, main_form: QWidget) -> Any:
        self.scroll_pile_a_lire = QScrollArea(main_form)
        self.setObjectName("scroll_pile_a_lire")

        self.scroll_pile_a_lire_widget = QWidget(main_form)
        self.setObjectName("scroll_pile_a_lire_widget")

        self.info_lecture = InfoLectureVolume(main_form)

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.scroll_pile_a_lire.setMinimumSize(QSize(732, 386))
        self.scroll_pile_a_lire.setMaximumSize(QSize(732,386))
        self.scroll_pile_a_lire.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_pile_a_lire.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_pile_a_lire.setWidgetResizable(True)

        self.scroll_pile_a_lire.verticalScrollBar().setMinimumWidth(15)
        self.scroll_pile_a_lire.verticalScrollBar().setMaximumWidth(15)
        self.scroll_pile_a_lire.verticalScrollBar().setStyleSheet(STYLE_SCROLL_BAR)

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_pile_a_lire_layout = QVBoxLayout()

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.scroll_pile_a_lire_widget.setLayout(self.scroll_pile_a_lire_layout)
        self.scroll_pile_a_lire.setWidget(self.scroll_pile_a_lire_widget)

        self.scroll_pile_a_lire_layout.addWidget(self.info_lecture)

    def setup_connections(self, main_form: QWidget) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass