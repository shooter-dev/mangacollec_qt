"""Imported modules/packages"""
import os

import sys
from abc import ABC

from PyQt5.QtCore import QSize
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtWidgets import QApplication, QSplashScreen
from dotenv import load_dotenv

from app.IHM.components.splash_screen import SplashScreen
from shooterQT.lib.dependency_injection.container import ContainerInterface, Container
from shooterQT.lib.main_page import MainPage
from shooterQT.lib.router.router import Router
from shooterQT.lib.router.router_interface import RouterInterface


class Kernel(ABC):
    """
    Kernel class
    """

    def __init__(self):
        super().__init__()
        load_dotenv(".env")
        load_dotenv(f".env.{os.getenv('APP_ENV')}")
        self.app = QApplication(sys.argv)
        self.__container: ContainerInterface = Container()

    def run(self):
        """
        Run app

        :return:
        """
        window = MainPage()

        splash_screen: QSplashScreen = SplashScreen(
            './app/IHM/resource/images/logo.png',
            QSize(800, 480),
            window
        )

        splash_screen.start_splash()

        #router: Router = Router(window.view_stacked)
        router: Router = self.__container.get(Router)
        router.staked_widget = window.view_stacked
        network = QNetworkAccessManager()

        self.__container.set(Router, router)
        self.__container.set(QNetworkAccessManager, network)

        self.build(self.__container)
        self.routing(self.__container.get(RouterInterface))
        self.start(self.__container.get(RouterInterface))

        splash_screen.finish_splash()

        window.show()

        self.__container.afficher_list_instance()
        try:
            sys.exit(self.app.exec_())
        except SystemExit:
            print('Closing Window...')
            raise

    def start(self, router: RouterInterface):
        """
        Start app

        :return:
        """
        # router.generate("app_home")

    def build(self, container: ContainerInterface):
        """
        Build container

        :return:
        """
        self.win = MainPage()

    def routing(self, router: RouterInterface):
        """
        Define routes

        :return:
        """
        # router.add(Route("app_home", AppController, "home"))