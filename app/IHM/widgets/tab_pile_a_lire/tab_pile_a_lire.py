from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from app.Metier.user import User
from app.IHM.widgets.item_lecture_volume.item_lecture_volume import ItemLectureVolume
from app.IHM.widgets.tab_pile_a_lire.tab_pile_a_lire_ui import Ui_PileALire
from shooterQT.lib.dependency_injection.container import Container


class TabPileALire(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        c: Container = Container()

        self.ui = Ui_PileALire()
        self.ui.setup_ui(self, QVBoxLayout)
        user: User = c.get('me')
        req_collection = c.get('req_collection')

        self.ui.info_lecture.tome_lus = 815
        self.ui.info_lecture.tome_a_lire_en_possession = 950
        self.ui.info_lecture.tome_a_lire_hor_possession = 380
        self.ui.info_lecture.tome_total_possession = user.possessions_count

        self.add_item()

    def add_item(self):
        size = QSize(732, 123)
        it1 = ItemLectureVolume()
        it1.set_image_url("https://images-eu.ssl-images-amazon.com/images/I/51MFd4E-XfL._SY210_.jpg")
        it1.set_name("7th garden")
        it1.set_info(8, 8)
        self.ui.scroll_pile_a_lire_layout.addWidget(it1)

        it2 = ItemLectureVolume()
        it2.set_image_url("https://m.media-amazon.com/images/I/51n9LPduz1L._SY210_.jpg")
        it2.set_name("7th Tim Loop: This Villainess Enjoys a Carefree Life")
        it2.set_info(4, 5)
        self.ui.scroll_pile_a_lire_layout.addWidget(it2)
        it3 = ItemLectureVolume()
        it3.set_image_url("https://m.media-amazon.com/images/I/51arK-x7dlS._SY210_.jpg")
        it3.set_name("A Certain Scientific Railgun")
        it3.set_info(0, 1)
        self.ui.scroll_pile_a_lire_layout.addWidget(it3)
        it4 = ItemLectureVolume()
        it4.set_image_url("https://m.media-amazon.com/images/I/51U3PjmXfQL._SY210_.jpg")
        it4.set_name("A Couple of Cukoos")
        it4.set_info(3, 7)
        self.ui.scroll_pile_a_lire_layout.addWidget(it4)
        it5 = ItemLectureVolume()
        it5.set_image_url("https://m.media-amazon.com/images/I/51arK-x7dlS._SY210_.jpg")
        it5.set_name("A Certain Scientific Railgun")
        it5.set_info(0, 1)
        self.ui.scroll_pile_a_lire_layout.addWidget(it5)
        it6 = ItemLectureVolume()
        it6.set_image_url("https://m.media-amazon.com/images/I/51U3PjmXfQL._SY210_.jpg")
        it6.set_name("A Couple of Cukoos")
        it6.set_info(3, 7)
        self.ui.scroll_pile_a_lire_layout.addWidget(it6)
