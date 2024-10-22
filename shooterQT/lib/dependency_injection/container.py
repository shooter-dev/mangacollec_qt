"""Imported modules/packages"""
import importlib
import inspect
import os
from types import ModuleType
from typing import Any, Dict, List, Type, Union


from shooterQT.lib.dependency_injection.container_interface import ContainerInterface



class ContainerMeta(type):
    _instances = {}

    def __call__(cls):

        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]


class Container(metaclass=ContainerMeta):
    """
    Container class
    """

    __instances: Dict[Union[Type, Any], Any] = {}
    __alias: Dict[Union[Type, Any], str] = {}
    __parameters: Dict[str, Any] = {}

    def __init__(self):
        self.__instances["container"] = self
        self.alias(ContainerInterface, Container)
        #self.set_parameter("templating_directory", os.path.join(os.getcwd(), "templates"))

        from shooterQT.lib.router.router import Router
        from shooterQT.lib.router.router_interface import RouterInterface
        self.alias(RouterInterface, Router)

    @staticmethod
    def get_type(name: Union[Type, str]) -> str:
        """
        Get type from class

        :param name:
        :return:
        """
        if isinstance(name, str):
            return name
        return f"{inspect.getmodule(name).__name__}.{name.__name__}"

    @staticmethod
    def get_instance(type_: str, args: List[Any]) -> object:
        """
        Create an instance

        :param type_:
        :param args:
        :return:
        """
        module: ModuleType = importlib.import_module(type_[0: type_.rfind(".")])
        return getattr(module, type_[type_.rfind(".") + 1:])(*args)

    def set(self, name: Type, obj: object) -> "Container":
        self.__instances[Container.get_type(name)] = obj
        return self

    def get(self, name: Union[Type, str]) -> Any:
        #self.afficher_list_instance()
        if name in self.__parameters:
            print("param: ", self.__parameters)
            return self.__parameters[name]

        service_id: str = self.get_type(name)

        if service_id in self.__alias:
            return self.get(self.__alias[Container.get_type(name)])

        if service_id not in self.__instances:
            args: List[Any] = []
            if len(inspect.signature(name.__init__).parameters) > 1:
                print(inspect.signature(name.__init__).parameters)
                for arg, type_ in inspect.signature(name.__init__).parameters.items():
                    if arg in ["self", "args", "kwargs"]:
                        continue
                    args.append(self.get(type_.annotation if type_.annotation.__name__ != "str" else arg))
            self.__instances[service_id] = Container.get_instance(service_id, args)
        return self.__instances[service_id]

    def alias(self, alias: Union[Type, Any], name: Union[Type, Any]):
        self.__alias[Container.get_type(alias)] = name
        return self

    def set_parameter(self, name: str, value: Any) -> "Container":
        self.__parameters[name] = value
        return self

    def afficher_list_instance(self):
        print("INSTANCES")
        for key, value in self.__instances.items():
            print('------------------------------')
            print(f"Clé : {key}, Valeur : {value}")
        print('******************************')
        print("PARAMETERS")
        for key, value in self.__parameters.items():
            print('------------------------------')
            print(f"Clé : {key}, Valeur : {value}")
        print('******************************')
