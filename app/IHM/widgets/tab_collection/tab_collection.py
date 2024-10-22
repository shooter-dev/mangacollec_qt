from typing import Any, List

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QVBoxLayout
from app.mangacollec import MangaCollec

from app.IHM.widgets.item_lecture_volume.item_lecture_volume import ItemLectureVolume
from app.IHM.widgets.tab_collection.tab_collection_ui import Ui_Collection
from app.ui_widget import UIWidget


class TabCollection(UIWidget):

    def init(self):

        self.ui = Ui_Collection()
        self.layout = QVBoxLayout

        api: MangaCollec = self._container.get(MangaCollec)
        collection = api.get_v2_collection_by_username("shooterdev")
        self._container.set_parameter("possessions", collection)


        print("possessions", len(collection["possessions"]))
        print("reads", len(collection["reads"]))
        print("read_editions", len(collection["read_editions"]))
        print("volumes", len(collection["volumes"]))

        collec = sorted(collection["reads"], key=lambda x: x['created_at'])

        for read in collec:
            volume = self.search(collection["volumes"], read['volume_id'])
            edition = self.search(collection["editions"], volume['edition_id'])
            serie = self.search(collection["series"], edition['series_id'])
            print(f"read le {read['created_at']} {volume['number']} {edition['title']} {serie['title']}")

        #self.add_item()

    def search(self, data: List, id: str):
        return next((item for item in data if item['id'] == id), None)

    def setup_connections(self) -> Any:
        pass
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
