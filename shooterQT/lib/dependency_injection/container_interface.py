"""Imported modules/packages"""
from abc import ABC
from typing import Any, Type, Union


class ContainerInterface(ABC):
    """
    Container interface
    """

    def get(self, name: Union[Type, Any]) -> Any:
        """
        Get service by name

        :param name:
        :return:
        """

    def set(self, name: Type, obj: object) -> "ContainerInterface":
        """
        Get service by name

        :param obj:
        :param name:
        :return:
        """

    def alias(self, alias: Union[Type, Any], name: Union[Type, Any]):
        """
        Add alias

        :param alias:
        :param name:
        :return:
        """

    def set_parameter(self, name: str, value: Any) -> "ContainerInterface":
        """
        Add parameter

        :param name:
        :param value:
        :return:
        """

    def afficher_list_instance(self) -> None:
        """

        :return:
        """
