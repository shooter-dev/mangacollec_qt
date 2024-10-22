from PyQt5.QtWidgets import QWidget, QHBoxLayout

from app.IHM.widgets.search_header.search_header_ui import Ui_SearchHeader


class QtUiTools:
    pass


class SearchHeader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_SearchHeader()
        self.ui.setup_ui(self,QHBoxLayout)
