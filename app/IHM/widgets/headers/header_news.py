from PyQt5.QtWidgets import QWidget, QHBoxLayout

from app.IHM.widgets.headers.header_news_ui import HeaderNewsUI
from shooterQT.lib.dependency_injection.container import Container


class HeaderNewsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = HeaderNewsUI()
        self.ui.setup_ui(self, QHBoxLayout)
        self.__container = Container()

        self.add_publisher_to_combo_box()

    def add_publisher_to_combo_box(self):
        publishers = self.__container.get('req_publishers')['publishers']
        publishers = sorted(publishers, key=lambda x: x['title'])

        for publisher in publishers:
            self.add_publisher(publisher)

    def add_publisher(self, publisher):
        if not publisher['closed']:
            self.ui.publisher_combo_box.addItem(publisher['title'])




