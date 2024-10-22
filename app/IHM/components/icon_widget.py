# coding:utf-8
from typing import Union

from PyQt5.QtCore import pyqtProperty
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtWidgets import QWidget


class IconWidget(QWidget):
    """ Icon widget

    Constructors
    ------------
    * IconWidget(`parent`: QWidget = None)
    * IconWidget(`icon`: QIcon | str | FluentIconBase, `parent`: QWidget = None)
    """

    def __init__(self, icon: QIcon, parent=None):
        super().__init__(parent)
        self.setIcon(icon)

    def getIcon(self):
        return self._icon

    def setIcon(self, icon: QIcon):
        self._icon = icon
        self.update()

    def paintEvent(self, e):
        # painter = QPainter(self)
        # painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        # # drawIcon(self._icon, painter, self.rect())
        # # self._icon.fluentIcon.render(painter, rect, **attributes)
        painter = QPainter(self)

        # Convertir l'icône en pixmap à une taille spécifique (par exemple, 100x100)
        pixmap = self._icon.pixmap(100, 100)

        # Dessiner l'image (le pixmap) à une position définie (ex: 50, 50)
        painter.drawPixmap(50, 50, pixmap)

        painter.end()

    icon = pyqtProperty(QIcon, getIcon, setIcon)