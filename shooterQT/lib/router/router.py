"""Imported modules/packages"""
from typing import Dict, List, Any, Tuple, Type

from PyQt5.QtWidgets import QWidget, QStackedWidget

from shooterQT.lib.abstract_page import AbstractPage
from shooterQT.lib.dependency_injection.container import ContainerInterface
from shooterQT.lib.router.route import Route
from shooterQT.lib.router.router_interface import RouterInterface


class Router(RouterInterface):
    """
    Router
    """
    __pages: Dict[str, Tuple[int, QWidget]] = {}
    list_pages_name: List[str] = []

    def __init__(self, container: ContainerInterface, view_stacked: QStackedWidget):
        self.__container: ContainerInterface = container
        self.staked_widget = view_stacked

    def add(self, name: str, page: AbstractPage):

        page_instance = page(self.staked_widget, container= self.__container, router=self)
        index = self.staked_widget.addWidget(page_instance)
        self.__pages[name] = (index, page_instance)
        self.list_pages_name.append(name)

    def call(self, name: str, params = None) -> bool:
        print(f"Call {name} page avec comme params : [{params}]")
        if name in self.__pages:
            index, page_instance = self.__pages[name]
            page_instance: AbstractPage
            self.staked_widget.setCurrentIndex(index)
            if params:
                page_instance._params = params
            else: page_instance.param = {}

            page_instance.update_page()
            menu: "LeftMenu" = self.__container.get("menu_lecture_item")
            menu.on_change_index(name)

            return True
            # self.header_widget.name_page_label.setText(name)

            # Démarrer un thread pour exécuter page_update()
        #getattr(container.get(self.controller), self.action)(*params)
        else:
            print(f"Page '{name}' not found")
            return False
        pass
