# coding:utf-8
from typing import Union

from PyQt5.QtCore import QSize, QEvent, Qt
from PyQt5.QtGui import QPainter, QColor, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QFrame, QSplashScreen, QVBoxLayout, QLabel



class SplashScreen(QSplashScreen):
    def __init__(self, pix: str, size: QSize, win: QWidget):
        super(QSplashScreen, self).__init__()

        self.win = win

        self.setMinimumSize(size)
        self.setMaximumSize(size)

        self.setPixmap(QPixmap(pix))

        self.show()

    def start_splash(self):
        print('Start ...')

    def finish_splash(self):
        self.finish(self.win)
        print('Finish ...')
