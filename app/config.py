"""Module for easily accessing configuration parameters from 'config.yaml'."""

from pathlib import Path

import yaml


class ConfigDict(dict):
    """A dictionary subclass that allows attribute-style access to its items."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(f"'ConfigDict' object has no attribute '{name}'")

class Config:
    """Class for loading and accessing configuration parameters from a YAML file."""
    def __init__(self, root_path=Path(__file__).parent.parent):
        """Initializes the Config object by loading parameters from 'config.yaml'."""
        config_path = root_path / "config.yaml"
        with open(config_path, "r", encoding="utf-8") as file:
            yaml_params = yaml.safe_load(file) or {}
        self.__params = self.__dict_to_configdict(yaml_params)

    def __dict_to_configdict(self, d):
        """Converts a nested dictionary into a nested ConfigDict."""
        for k, v in d.items():
            if isinstance(v, dict):
                d[k] = self.__dict_to_configdict(v)
        return ConfigDict(d)

    def __getattr__(self, attr):
        try:
            return getattr(self.__params, attr)
        except AttributeError:
            raise AttributeError(f"Configuration parameter '{attr}' not found")

    def __getitem__(self, key):
        return self.__params[key]

config = Config()
