from abc import abstractmethod
from typing import Any

from PyQt5.QtWidgets import QWidget, QLayout, QBoxLayout

from shooterQT.lib.dependency_injection.container import Container
from shooterQT.lib.dependency_injection.container_interface import ContainerInterface
from shooterQT.lib.ui_interface import UiInterface


class UIWidget(QWidget):
    ui: UiInterface = None
    layout: QBoxLayout = None

    def __init__(self, parent=None):
        super(UIWidget, self).__init__(parent)

        self._container: Container = Container()

        self.init()

        self.ui.setup_ui(self, layout=self.layout)

        self.setup_connections()

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def setup_connections(self) -> Any:
        pass
