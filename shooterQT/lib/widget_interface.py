from abc import ABC, abstractmethod
from typing import Any


class WidgetInterface(ABC):
    """
    Page interface
    """

    def setup_ui(self) -> Any:
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.widget_to_layout()
        self.setup_connections()

    @abstractmethod
    def create_widgets(self) -> Any:
        pass

    @abstractmethod
    def modify_widgets(self) -> Any:
        pass

    @abstractmethod
    def create_layout(self) -> Any:
        pass

    @abstractmethod
    def widget_to_layout(self) -> Any:
        pass

    @abstractmethod
    def setup_connections(self) -> Any:
        pass