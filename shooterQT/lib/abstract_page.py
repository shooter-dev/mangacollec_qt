"""Imported modules/packages"""
from abc import ABC, abstractmethod
from typing import Callable, Dict, Any, List

from PyQt5.QtWidgets import QWidget

from app.src.utils.pages_utils import PagesUtils


class AbstractPage(QWidget):
    """
    Abstract controller
    """
    _params: Dict[str, Any] = {}

    def __init__(
        self, parent, *args, **kwargs
    ):
        QWidget.__init__(self, parent)

        #self.afficher_param(args, kwargs, parent)

        self._container: "ContainerInterface" = kwargs["container"]
        self._router: "RouterInterface" = kwargs["router"]

        self.init_page()

        #self.setStyleSheet(PagesUtils.generer_random_color_hex())

        self.setup_ui()

    def afficher_param(self, args, kwargs, parent):
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
        print(f"PARENT: {parent.objectName()}")
        print(f"PAGE: {self.__class__.__name__}")
        print(f"List KWARGS")
        for key, kwarg in kwargs.items():
            print(f"KEY: {key} : KWARG{kwarg}")
            print('----------------------')
        print(f"List ARGS")
        for arg in args:
            print(f"ARG: {arg}")
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

    def get_param(self, name: str) -> Any:
        result = None
        try:
            result = self._params[name]
        except Exception as e:
            print(e)
            return ''
        return result

    @abstractmethod
    def init_page(self):
        pass

    @abstractmethod
    def update_page(self):
        pass
