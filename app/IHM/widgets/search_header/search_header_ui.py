from typing import Any

from PyQt5.QtCore import QSize, QCoreApplication, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton

from app.src.utils.const import STYLE_COLOR_BORDER, STYLE_COLOR_READ, FONT_16, STYLE_COLOR_PRIMARY
from shooterQT.lib.ui_interface import UiInterface


class Ui_SearchHeader(UiInterface):
    def init(self, main_form: QWidget):
        size = QSize(732, 51)
        main_form.setMinimumSize(size)
        main_form.setMaximumSize(size)
        main_form.setObjectName("Ui_SearchHeader")
        main_form.setStyleSheet(f"""
            #search_line_edit {{
                border: 1px solid { STYLE_COLOR_BORDER };
                border-radius: 16px;
                padding-left: 38px;
                padding-right: 38px;
            }}

            #search_line_edit:focus {{
                border: 2px solid { STYLE_COLOR_READ };
                border-radius: 5px;
            }}
        """)

    def create_widgets(self, main_form: QWidget) -> Any:
        self.search_line_edit = QLineEdit(main_form)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.trie_button = QPushButton(main_form)
        self.trie_button.setObjectName(u"trie_button")

    def modify_widgets(self, main_form: QWidget) -> Any:
        self.trie_button.setMinimumSize(QSize(32, 34))
        self.trie_button.setMaximumSize(QSize(32, 34))
        self.trie_button.setIcon(QIcon("app/assets/img/trie.png"))
        self.trie_button.setIconSize(QSize(32, 32))

        self.search_line_edit.setMinimumSize(QSize(652, 32))
        self.search_line_edit.setMaximumSize(QSize(652, 32))

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(12, 9, 18, 9)
        pass

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.addWidget(self.search_line_edit, 0, Qt.AlignLeft|Qt.AlignVCenter)
        self.main_layout.addWidget(self.trie_button, 0, Qt.AlignRight | Qt.AlignVCenter)

    def setup_connections(self, main_form: QWidget) -> Any:
        pass

    def retranslate_ui(self, main_form: QWidget) -> Any:
        pass