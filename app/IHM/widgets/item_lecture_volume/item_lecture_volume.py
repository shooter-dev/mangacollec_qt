from typing import Any

from PyQt5 import QtNetwork
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtWidgets import QHBoxLayout

from app.src.utils.img_downloader import ImgDownloader
from app.IHM.widgets.item_lecture_volume.item_lecture_volume_ui import ItemLectureVolumeUI
from app.ui_widget import UIWidget


class ItemLectureVolume(UIWidget):
    def init(self):
        self.ui: ItemLectureVolumeUI = ItemLectureVolumeUI()
        self.layout = QHBoxLayout

    def setup_connections(self) -> Any:
        self.customContextMenuRequested.connect(self.open_context_menu)

    @property
    def image(self) -> QPixmap:
        return self.ui.image_label.pixmap()

    @image.setter
    def image(self, image: QPixmap):
        self.ui.image_label.setPixmap(image)

    def set_image_url(self, url: str):
        download_queue = self._container.get(QNetworkAccessManager)

        req = QtNetwork.QNetworkRequest(QUrl(url))
        downloader = ImgDownloader(self.ui.image_label, req)
        downloader.start_fetch(download_queue)

    @property
    def name(self) -> str:
        return self.ui.name_serie_label.text()

    def set_name(self, name) -> None:
        self.ui.name_serie_label.setText(name)

    @property
    def info(self) -> str:
        return self.ui.name_serie_label.text()

    def set_info(self, tome_lu: int, volumes: int) -> None:
        self.ui.details_label.setText(f"{tome_lu} / {volumes} tome{'s' if volumes > 1 else ''}")
        self.__changed_event(tome_lu, volumes)

    def __changed_event(self, tome_lus: int, volumes: int):
        value_bar: int = int((tome_lus / volumes) * 100)
        self.ui.progress_bar.setValue(value_bar)


    def open_context_menu(self, point):
        print(f"click click {point}")
        self.ui.menu_lecture_item.exec_(QCursor.pos())