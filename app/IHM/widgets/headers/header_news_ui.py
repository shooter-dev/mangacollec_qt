from typing import Any

from PyQt5.QtCore import Qt, QSize, QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from app.src.utils.const import FONT_16, FONT_18
from app.IHM.widgets.headers.size_delegate_combo_box_publisher import SizeDelegateComboBoxPublisher

from shooterQT.lib.ui_interface import UiInterface


class HeaderNewsUI(UiInterface):
    def init(self, main_form: QWidget):
        size = QSize(732, 51)
        main_form.setObjectName("HeaderNewsUI")
        main_form.setMinimumSize(size)
        main_form.setMaximumSize(size)
        main_form.setStyleSheet(u"""
            #HeaderNewsUI {
                border-width: 1px;
                border-bottom-color: black;
                border-bottom-style: solid;
            }
        """)

    def create_widgets(self, main_form: QWidget) -> Any:

        # self.font_16 = QFont()
        # self.font_16.setPointSize(16)
        # self.font_16.setFamily(U"Helvetica")
        # self.font_16.setBold(False)
        # self.font_16.setWeight(50)

        # self.font_18 = QFont()
        # self.font_18.setPointSize(18)
        # self.font_18.setFamily(U"Helvetica")
        # self.font_18.setBold(True)
        # self.font_18.setWeight(75)

        self.name_page_label = QLabel(main_form)
        self.name_page_label.setObjectName(u"name_page_label")

        self.publisher_combo_box = QComboBox(main_form)
        self.publisher_combo_box.setObjectName(u"publisher_combo_box")

    def modify_widgets(self, main_form: QWidget) -> Any:

        self.__update_name_page_label()

        self.__update_publisher_combo_box()

    def __update_publisher_combo_box(self):
        size = QSize(223, 28)
        self.publisher_combo_box.setMinimumSize(size)
        self.publisher_combo_box.setMaximumSize(size)
        self.publisher_combo_box.setFont(FONT_16)
        self.publisher_combo_box.font().bold()
        delegate = SizeDelegateComboBoxPublisher(self.publisher_combo_box)
        self.publisher_combo_box.setMaxVisibleItems(5)

        self.publisher_combo_box.setItemDelegate(delegate)
        self.publisher_combo_box.setStyleSheet(u"""
            #publisher_combo_box {
                font-size: 17px;               /* Taille de la police */
                background-color: #FFF;   /* Couleur de fond */
                color: darkblue;               /* Couleur du texte */
                border: 1px solid blue;        /* Bordure du ComboBox */
            }
            #publisher_combo_box::drop-down {
                border: none;                   /* Largeur de la flèche */
            }
            #publisher_combo_box::down-arrow {
                image: url(:/icons/icons/red/arrow-combo-box.svg);    /* Remplacez par le chemin de votre image de flèche */
                width: 28px;
                height: 28px;
                margin-right: 28px;
            }
        """)

        self.publisher_combo_box.addItem("")

    def __add_item_publisher_combo_box(self):
        icon = QIcon()
        icon.addFile(u":/img/img/logo.png", QSize(), QIcon.Disabled, QIcon.Off)


    def __update_name_page_label(self):
        self.name_page_label.setMinimumSize(QSize(0, 21))
        self.name_page_label.setMaximumSize(QSize(300, 21))
        self.name_page_label.setFont(FONT_18)

    def create_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.setContentsMargins(-1, 0, -1, 0)

    def widgets_to_layouts(self, main_form: QWidget) -> Any:
        self.main_layout.addWidget(self.name_page_label, 0, Qt.AlignLeft | Qt.AlignVCenter)

        self.main_layout.addWidget(self.publisher_combo_box, 0, Qt.AlignRight|Qt.AlignVCenter)

    def retranslate_ui(self, main_form: QWidget) -> Any:
        self.name_page_label.setText(QCoreApplication.translate("HeaderNews", u"Nouveaut\u00e9s", None))
        self.publisher_combo_box.setItemText(0, QCoreApplication.translate("HeaderNews", u"Editeurs", None))

        self.publisher_combo_box.setCurrentText(QCoreApplication.translate("HeaderNews", u"Editeurs", None))
