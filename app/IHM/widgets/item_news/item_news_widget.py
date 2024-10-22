from PyQt5 import QtNetwork
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from app.Metier.news_item_model import NewsItemModel
from app.src.utils.img_downloader import ImgDownloader
from app.IHM.widgets.item_news.item_news_ui_widget import ItemNewsUiWidget
from shooterQT.lib.dependency_injection.container import Container


class ItemNewsWidget(QWidget):
    def __init__(self, item_news: NewsItemModel, parent=None):
        super(ItemNewsWidget, self).__init__(parent)

        c: Container = Container()

        self.ui = ItemNewsUiWidget()
        self.ui.setup_ui(self, QVBoxLayout)
        size: QSize = QSize(238, 391)
        self.setMinimumSize(size)
        self.setMaximumSize(size)

        self.item_news = item_news

        if len(item_news.serie_name) > 20:
            self.ui.name_serie_label.setText(item_news.serie_name[:24] + '...')
        else:
            self.ui.name_serie_label.setText(item_news.serie_name)

        self.ui.name_tome_label.setText(item_news.numero_volume)

        if item_news.is_sponsor:
            self.ui.sponso_label.setText('SPONSORIS\u00c9')
        self.ui.sponso_label.setText('')



        download_queue = c.get(QNetworkAccessManager)

        req = QtNetwork.QNetworkRequest(QUrl(item_news.url_volume))
        downloader = ImgDownloader(self.ui.image_volume_label, req)
        downloader.start_fetch(download_queue)

        #self.manager.finished.connect(self.on_finished)



        # pix = QPixmap()
        # pix.loadFromData(requests.get(item_news.url_volume).content)
        # pix.scaled(SIZE_IMAGE_NEWS_ITEM)
        # self.ui.image_volume_label.setPixmap(pix)