from typing import Any

from PyQt5.QtWidgets import QVBoxLayout

from app.IHM.widgets.headers.header_news import HeaderNewsWidget
from app.IHM.widgets.view_list_item_news_widget import ViewListItemNewsWidget
from shooterQT.lib.abstract_page import AbstractPage
from shooterQT.lib.page_interface import PageInterface


class NewsPage(PageInterface, AbstractPage):

    def setup_ui(self) -> None:
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self) -> Any:
        self.header: HeaderNewsWidget = HeaderNewsWidget(self)
        self.item_news = ViewListItemNewsWidget(self)


    def modify_widgets(self) -> Any:
        pass

    def create_layouts(self) -> Any:
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

    def widgets_to_layouts(self) -> Any:
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.header)
        self.main_layout.addWidget(self.item_news)

    def update_page(self):
        print('News Page update')


