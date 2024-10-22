import sys
from cProfile import label
from typing import Any, Type

from PyQt5.QtCore import QObject, QSize, Qt, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton

from app.src.utils.const import SIZE_PAGE_MIN, FONT_12
from app.src.utils.pages_utils import PagesUtils
from shooterQT.lib.abstract_page import AbstractPage
from shooterQT.lib.page_interface import PageInterface
from shooterQT.lib.ui_interface import UiInterface


class AccountPage(PageInterface, AbstractPage):

    def init(self, main_form: QWidget):
        main_form.setMinimumSize(SIZE_PAGE_MIN)
        main_form.setMaximumSize(SIZE_PAGE_MIN)

    def create_widgets(self) -> Any:


        self.deconnection_button = QPushButton(self)
        self.deconnection_button.setObjectName(u"deconnection_button")

        self.mention_legale_label = QLabel(self)
        self.mention_legale_label.setObjectName(u"mention_legale_label")

        self.name_version_label = QLabel(self)
        self.name_version_label.setObjectName(u"name_version_label")


    def modify_widgets(self) -> Any:
        self.deconnection_button.setMinimumSize(QSize(681, 44))
        self.deconnection_button.setFont(FONT_12)

        self.mention_legale_label.setFont(FONT_12)

        self.name_version_label.setFont(FONT_12)


    def create_layouts(self) -> Any:
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

    def widgets_to_layouts(self) -> Any:
        self.setLayout(self.main_layout)

        self.main_layout.addWidget(self.deconnection_button, 0, Qt.AlignHCenter)
        self.main_layout.addWidget(self.mention_legale_label, 0, Qt.AlignHCenter)
        self.main_layout.addWidget(self.name_version_label, 0, Qt.AlignHCenter)



    def setup_connections(self) -> Any:
        self.deconnection_button.triggered.connect(self.on_action_exit_triggered)

    def retranslate_ui(self) -> Any:
        self.setWindowTitle(QCoreApplication.translate("main_form", u"main_form", None))
        self.deconnection_button.setText(QCoreApplication.translate("main_form", u"Se d\u00e9connecter", None))
        self.mention_legale_label.setText(QCoreApplication.translate("main_form", u"Mention l\u00e9gales", None))
        self.name_version_label.setText(QCoreApplication.translate("main_form", u"MangacollecQT v2.10.0 (101)", None))

    # retranslateUi

    def update_page(self):
        print('Search Page update')

    def on_action_exit_triggered(self):
        sys.exit()


