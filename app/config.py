"""Easily accessing `config.yaml` files through a simple 'config' object"""

from pathlib import Path

import yaml


class ConfigDict(dict):
    """
    The ConfigDict class is a subclass of the built-in dict class in Python.
    It allows attribute-style access to its keys.

    Example:
        config_dict = ConfigDict({"key": "value"})
        print(config_dict.key)  # Outputs: value
    """

    def __getattr__(self, name):
        """
        A special method in Python classes that allows the
        class to handle undefined attribute references.

        Parameters: name (str): The name of the
        attribute whose value is being requested.

        Returns:
            Any: The value of the attribute 'name' if it exists in the
            dictionary, raises an AttributeError otherwise.

        Raises:
            AttributeError: If 'name' does not exist
            as a key in the dictionary.
        """
        try:
            return self[name]
        except KeyError as exc:
            raise exc


class Config:
    """
    The Config class is used to load configuration parameters from a YAML file.

    Attributes:
        __params (ConfigDict): A dictionary-like object that
        stores the configuration parameters.
    """

    def __init__(self, root_path=Path(__file__).parents[1]):
        """
        The constructor for Config class.

        Parameters:
            root_path (str): The root path where the config.yaml file
            is located. Defaults to the current directory.
        """
        config_path = f"{root_path}/config.yaml"
        with open(config_path, "r", encoding="utf-8") as file:
            yaml_params = yaml.safe_load(file)
        self.__params = self.__dict_to_configdict(yaml_params)

    def __dict_to_configdict(self, d: dict):
        """
        A private method that converts a dictionary into a ConfigDict object.

        Parameters:
            d (dict): The dictionary to be converted.

        Returns:
            ConfigDict: The converted ConfigDict object.
        """
        for k, v in d.items():
            if isinstance(v, dict):
                d[k] = self.__dict_to_configdict(v)
        return ConfigDict(d)

    def __getattr__(self, attr):
        """
        A special method in Python classes that allows the
        class to handle undefined attribute references.

        Parameters:
            attr (str): The name of the attribute
            whose value is being requested.

        Returns:
            Any: The value of the attribute 'attr' if it exists,
            raises an AttributeError otherwise.
        """
        return getattr(self.__params, attr)

    def __getitem__(self, key):
        """
        A special method in Python classes that allows the
        class instances to use the indexing operator.

        Parameters: key (str): The key/index whose
        corresponding value is being requested.

        Returns:
            Any: The value corresponding to 'key' in the __params attribute.
        """
        return self.__params[key]


config = Config()
"""
An instance of the Config class. This instance
can be imported in other modules to
use the configuration parameters.
"""
