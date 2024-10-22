import random
from abc import abstractmethod
from typing import Any


class PageInterface:
    """
    Page interface
    """

    def setup_ui(self) -> Any:
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.widgets_to_layouts()
        self.setup_connections()
        self.retranslate_ui()

    @abstractmethod
    def create_widgets(self) -> Any:
        pass

    @abstractmethod
    def modify_widgets(self) -> Any:
        pass

    @abstractmethod
    def create_layouts(self) -> Any:
        pass

    @abstractmethod
    def widgets_to_layouts(self) -> Any:
        pass

    @abstractmethod
    def setup_connections(self) -> Any:
        pass

    @abstractmethod
    def retranslate_ui(self) -> Any:
        pass

