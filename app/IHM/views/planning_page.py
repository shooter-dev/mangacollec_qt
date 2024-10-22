from cProfile import label
from typing import Any, Type

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from app.src.utils.const import SIZE_PAGE_MIN
from shooterQT.lib.abstract_page import AbstractPage
from shooterQT.lib.page_interface import PageInterface


class PlanningPage(PageInterface, AbstractPage):

    def init_page(self):
        self.setMinimumSize(SIZE_PAGE_MIN)
        self.setMaximumSize(SIZE_PAGE_MIN)

    def setup_ui(self) -> None:
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self) -> Any:
        self.label: QLabel = QLabel(self)
        #print(type(self.ui))


    def modify_widgets(self) -> Any:
        self.label.setText("Planning Page")

    def create_layouts(self) -> Any:
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

    def widgets_to_layouts(self) -> Any:
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.label)

    def update_page(self):
        print('Planning Page update')


