import re

import sys
from abc import abstractmethod
from typing import Any

from PyQt5 import uic
from PyQt5.QtCore import QMetaObject, QObject, QSize
from PyQt5.QtWidgets import QWidget, QApplication, QBoxLayout, QVBoxLayout


class UicInterface(QObject):
    """
    Page interface
    """
    def __init__(self, win, parent=None):
        super(UicInterface, self).__init__(parent)

        self.ui = uic.loadUi(f'app/src/ui/{self.class_name_to_snake_case(self.__class__.__name__)}.ui', win)

    def class_name_to_snake_case(self, class_name) -> str:
        # Trouver les majuscules suivies par des minuscules ou d'autres majuscules
        snake_case = re.sub(r'(?<!^)([A-Z][a-z]+)', r'_\1', class_name)
        # Gérer les séquences de majuscules comme dans 'HTMLParser'
        snake_case = re.sub(r'([a-z])([A-Z])', r'\1_\2', snake_case)
        return snake_case.lower()