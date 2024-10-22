from typing import Any

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedWidget

from app.src.utils.const import STYLE_COLOR_BACKGROUND, STYLE_COLOR_BORDER
from app.IHM.widgets.left_menu.left_menu import LeftMenu


class MainPage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setObjectName('app_main')
        size = QSize(800, 480)
        self.setMaximumSize(size)
        self.setMinimumSize(size)
        self.setStyleSheet(f"""
            background-color: {STYLE_COLOR_BACKGROUND};
            
            border: 1px solid {STYLE_COLOR_BORDER};
            
        """)

        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.widget_to_layout()
        self.setup_connections()

    def create_widgets(self) -> Any:
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName(u"centralWidget")

        self.menu_left = LeftMenu(self)
        self.menu_left.setObjectName(u"menu_left")

        self.view_stacked = QStackedWidget(self)
        self.view_stacked.setObjectName(u"view_stacked")

    def modify_widgets(self) -> Any:
        pass

    def create_layouts(self) -> Any:
        self.main_layout = QHBoxLayout(self.centralWidget)
        self.main_layout.setObjectName(u"horizontalLayout")
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

    def widget_to_layout(self) -> Any:
        self.setCentralWidget(self.centralWidget)

        self.main_layout.addWidget(self.menu_left)
        self.main_layout.addWidget(self.view_stacked)

    def setup_connections(self) -> Any:
        #self.menu_left.button_home_menu.clicked.connect(lambda: self.home_page())
        pass

    def home_page(self):
        self.router.call_page('home')
