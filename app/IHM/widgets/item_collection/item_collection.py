from PyQt5 import QtNetwork
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from app.Metier.item_collection import ItemCollection
from app.src.utils.img_downloader import ImgDownloader
from app.IHM.widgets.item_collection.item_collection_ui import Ui_ItemCollection
from shooterQT.lib.dependency_injection.container import Container


class ItemCollection(QWidget):
    _item: ItemCollection = None
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ItemCollection()
        self.ui.setup_ui(self, QHBoxLayout)
        self.__c: Container = Container()

    def set_image_item_url(self,image_label: QPixmap, url: str):
        download_queue = self.__c.get(QNetworkAccessManager)

        req = QtNetwork.QNetworkRequest(QUrl(url))
        downloader = ImgDownloader(image_label, req)
        downloader.start_fetch(download_queue)

    @property
    def item(self) -> ItemCollection:
        return self._item

    @item.setter
    def item(self, item: ItemCollection) -> None:
        self.ui.name_serie_label = item.name
        self.ui.info_label.setText(f"{item.nb_tome} / {item.nb_tome_total} {item.status if '• ' + item.status else ''}")
        for url in item.list_url_volume:
            pixmap = QPixmap()
            self.ui.tome_item_layout.addWidget(pixmap)
            self.set_image_item_url(pixmap, url)
