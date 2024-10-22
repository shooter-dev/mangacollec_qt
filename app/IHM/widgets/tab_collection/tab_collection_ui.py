from typing import Any

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout

from app.src.utils.const import STYLE_SCROLL_BAR
from app.src.utils.debug import widget_taille
from app.IHM.widgets.info_collection.info_collection import InfoCollection
from shooterQT.lib.ui_interface import UiInterface


class Ui_Collection(UiInterface):
    def init(self, main_form: QWidget):
        size = QSize(732,429)
        main_form.setMinimumSize(size)
        main_form.setMaximumSize(size)
        main_form.setObjectName("Ui_TabCollection")
        widget_taille(main_form)
        # main_form.setStyleSheet(f"""
        #     QScrollBar:vertical {{
        #         background: rgba(0, 0, 0,0);
        #         border: 1px solid  {STYLE_COLOR_BORDER};
        #         border-radius: 7px;
        #         width: 15px;
        #     }}
        #     
        #     QScrollBar:handle:vertical {{
        #         background: {STYLE_COLOR_TEXT_DETAIL};
        #         border: 1px solid  #000;
        #         width: 10px;
        #         border-radius: 6px;
        #         max-height: 18px;
        #     }}
        #     
        #     QScrollBar:sub-line:vertical {{
        #         background: rgba(0, 0, 0,0);
        #         border-radius: 6px;
        #         height: 8px;
        #     }}
        #     
        #     QScrollBar:add-line:vertical {{
        #         background: rgba(0, 0, 0,0);
        #         border-radius: 7px;
        #     }}
        #     
        #     QScrollBar:add-page:vertical,
        #     QScrollBar:sub-page:vertica {{
        #     }}
        # """)

    def create_widgets(self, main_form: QWidget) -> Any:
        self.scroll_collection = QScrollArea(main_form)
        self.setObjectName("scroll_collection")

        self.scroll_collection_widget = QWidget(main_form)
        self.setObjectName("scroll_collection_widget")

        self.info_collection = InfoCollection(main_form)

        #self.info_lecture = InfoLectureVolume(main_form)

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.scroll_collection.setMinimumSize(QSize(732, 386))
        self.scroll_collection.setMaximumSize(QSize(732,386))
        self.scroll_collection.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_collection.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_collection.setWidgetResizable(True)
        self.scroll_collection.verticalScrollBar().setMinimumWidth(15)
        self.scroll_collection.verticalScrollBar().setMaximumWidth(15)
        self.scroll_collection.setStyleSheet(STYLE_SCROLL_BAR)

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_collection_layout = QVBoxLayout()

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.scroll_collection_widget.setLayout(self.scroll_collection_layout)
        self.scroll_collection.setWidget(self.scroll_collection_widget)

        self.scroll_collection_layout.addWidget(self.info_collection)

    def setup_connections(self, main_form: QWidget) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass