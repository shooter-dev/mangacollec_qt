from typing import Any

from PyQt5.QtWidgets import QVBoxLayout, QWidget, QTabWidget

from app.src.utils.const import SIZE_PAGE_MIN, STYLE_COLOR_PRIMARY, STYLE_COLOR_STATE_HOVER
from app.IHM.widgets.search_header.search_header import SearchHeader
from app.IHM.widgets.tab_collection.tab_collection import TabCollection
from app.IHM.widgets.tab_pile_a_lire.tab_pile_a_lire import TabPileALire
from shooterQT.lib.abstract_page import AbstractPage
from shooterQT.lib.page_interface import PageInterface


class CollectionPage(PageInterface, AbstractPage):


    def init_page(self):
        self.setMinimumSize(SIZE_PAGE_MIN)
        self.setMaximumSize(SIZE_PAGE_MIN)
        self.setObjectName("CollectionPage")
        self.setStyleSheet(f"""
            QTabWidget::pane {{ /* The tab widget frame */
                border-top: 2px solid #C2C7CB;
                position: absolute;
                top: -0.5em;
            }}
            
            QTabWidget::tab-bar {{
                alignment: center;
            }}
            
            /* Style the tab using the tab sub-control. Note that
                it reads QTabBar _not_ QTabWidget */
            QTabBar::tab {{
                background: #D3D3D3;
                border: 1px solid #C4C4C3;
                border-bottom-color: #C2C7CB; /* same as the pane color */
                border-radius: 17px;
                width:132px;
                min-height: 34px;
                margin: 6px
            }}
            QTabWidget::tab-bar:left {{
                padding: 6px
            }}
            
            QTabWidget::tab-bar:right {{
                padding: 6px
            }}
            
            QTabBar::tab:selected, QTabBar::tab:hover {{
                background: { STYLE_COLOR_STATE_HOVER };
            }}
            
            QTabBar::tab:selected {{
                border-color: { STYLE_COLOR_PRIMARY };
                background-color: #CF000A;
            }}
            
            #QWidget {{
                border: 1px solid { STYLE_COLOR_PRIMARY };
                background-color: #CF000A;
            }}
        """)

    def create_widgets(self) -> Any:
        self.header = SearchHeader(self)
        self.header.setObjectName("SearchHeader")

        self.tabWidget = QTabWidget()
        self.tabWidget.setObjectName(u"tabWidget")

        self.tab_pile_a_lire = TabPileALire()
        self.tab_pile_a_lire.setObjectName(u"tab_pile_a_lire")

        self.tab_collection = TabCollection()
        self.tab_collection.setObjectName(u"tab_collection")

        self.tab_completer = QWidget()
        self.tab_completer.setObjectName(u"tab_completer")

        self.tab_envies = QWidget()
        self.tab_envies.setObjectName(u"tab_envies")

        self.tab_prets = QWidget()
        self.tab_prets.setObjectName(u"tab_prets")

    def modify_widgets(self) -> Any:
        self.tabWidget.addTab(self.tab_pile_a_lire, u"PILE A LIRE")
        self.tabWidget.addTab(self.tab_collection, u"COLLECTION")
        self.tabWidget.addTab(self.tab_completer, u"CONPLETER")
        self.tabWidget.addTab(self.tab_envies, u"ENVIES")
        self.tabWidget.addTab(self.tab_prets, u"PRETS")

        self.tabWidget.setCurrentIndex(0)

    def create_layouts(self) -> Any:
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

    def widgets_to_layouts(self) -> Any:
        self.setLayout(self.main_layout)

        self.main_layout.addWidget(self.header)
        self.main_layout.addWidget(self.tabWidget)


    def update_page(self):
        print('Collection Page update')


