"""Imported modules/packages"""
from abc import ABC
from typing import List, Any, Type

from PyQt5.QtWidgets import QWidget

from shooterQT.lib.abstract_page import AbstractPage
from shooterQT.lib.router.route import Route


class RouterInterface(ABC):
    """
    Router interface
    """

    def add(self,name: str, page: Type[AbstractPage]) -> "Any":
        """
        Add route to collection

        :param route:
        :return:
        """

    def call(self, name: str, params: List[Any] = None):
        """
        Search route by name and call it

        :param name:
        :param params:
        :return:
        """
