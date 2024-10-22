from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtSvg import QSvgRenderer


def svg_to_pixmap(svg_filename: str, width: int, height: int, color: QColor) -> QPixmap:
    renderer = QSvgRenderer(svg_filename)
    pixmap = QPixmap(width, height)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    renderer.render(painter) # this is the destination, and only its alpha is used!
    painter.setCompositionMode(
        painter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), color)
    painter.end()
    return pixmap