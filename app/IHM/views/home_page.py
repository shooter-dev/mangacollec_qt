from cProfile import label
from typing import Any

from PyQt5.QtCore import QObject, QSize
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

from app.src.utils.const import SIZE_PAGE_MIN
from app.src.utils.pages_utils import PagesUtils
from shooterQT.lib.abstract_page import AbstractPage
from shooterQT.lib.page_interface import PageInterface


class HomePage(PageInterface, AbstractPage):


    def init_page(self):
        self.setMinimumSize(SIZE_PAGE_MIN)
        self.setMaximumSize(SIZE_PAGE_MIN)

    def create_widgets(self) -> Any:
        self.button: QPushButton = QPushButton(self)
        #print(type(self.ui))


    def modify_widgets(self) -> Any:
        self.button.setText(f"Home Page w: {self.width()} h: {self.height()} min: {self.minimumSize()} max: {self.maximumSize()}")

    def create_layouts(self) -> Any:
        self.main_layout = QVBoxLayout()

    def widgets_to_layouts(self) -> Any:
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.button)

    def setup_connections(self) -> Any:
        self.button.clicked.connect(self.on_button_home_clicked)


    def on_button_home_clicked(self):
        self._router.call('panier', {
            "test": "coucou ça marche",
            "number": 23
        })
        print('ça marche')

    def update_page(self):
        print('Home Page update')