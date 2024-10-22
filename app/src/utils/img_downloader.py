import time

from PyQt5.QtCore import Qt, QByteArray, QBuffer, QRectF, QObject, QRect, QPoint
from PyQt5.QtGui import QPixmap, QImage, QPainter, QBrush, QBitmap, QPainterPath, QRegion, QPen
from PyQt5.QtNetwork import QNetworkRequest

from PIL import Image, ImageDraw, ImageQt

from app.src.utils.const import SIZE_IMAGE_NEWS_ITEM


class ImgDownloader(QObject):
    def __init__(self, parent, req: QNetworkRequest):
        self.req = req
        super(ImgDownloader, self).__init__(parent)

    def set_image(self, img_binary):

        pixmap = QPixmap()
        pixmap.loadFromData(img_binary)
        pixmap.scaled(SIZE_IMAGE_NEWS_ITEM, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        # rounded_pixmap = QPixmap(pixmap.size())
        # rounded_pixmap.fill(Qt.transparent)

        # Créer un QPainter pour dessiner sur le nouveau pixmap
        # painter = QPainter(rounded_pixmap)
        # painter.setRenderHint(QPainter.Antialiasing)
        #
        # # Définir les dimensions et le radius
        # radius = 9  # Border-radius de 9 pixels
        # rect = QRect(0, 0, pixmap.width(), pixmap.height())
        #
        # # Dessiner le pixmap sur le rectangle arrondi
        # painter.setClipRect(rect)  # Limiter le dessin à l'intérieur du rectangle
        # painter.drawPixmap(0, 0, pixmap)  # Dessiner le pixmap
        #
        # # Dessiner un rectangle arrondi pour le fond
        # painter.setBrush(QBrush(Qt.transparent))  # Couleur de fond
        # painter.drawRoundedRect(rect, radius, radius)
        #
        # # Dessiner un bord de 1 pixel
        # border_pen = QPen(Qt.white, 9)  # Couleur du bord et épaisseur
        # painter.setPen(border_pen)
        # painter.drawRoundedRect(rect, radius, radius)
        #
        # painter.end()





        self.parent().setPixmap(pixmap)

    def start_fetch(self, net_mgr):
        self.fetch_task = net_mgr.get(self.req)
        self.fetch_task.finished.connect(self.resolve_fetch)

    def resolve_fetch(self):

        the_reply = self.fetch_task.readAll()
        self.set_image(the_reply)

