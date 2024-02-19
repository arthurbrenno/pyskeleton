"""Dependency injection application module"""

from typing import List, Tuple

from injector import Injector

from app.settings import Settings

interfaces_to_implementations: List[Tuple] = [
    (Settings, Settings)
]


def bind_interfaces_to_implementations(instance: Injector, interface_list: list) -> None:
    """Bind interfaces to implementations using a list of tuples.

    Args:
        instance (Injector): The injector instance for the application.
        interface_list (list): List of tuples, where each tuple
        contains interface and implementation classes.
    """
    for interface, implementation in interface_list:
        instance.binder.bind(interface, to=implementation)


def get_injector() -> Injector:
    """Get the injector for the application.

    Returns:
        Injector: The injector instance for the application.
    """
    _instance: Injector = Injector(auto_bind=True)

    bind_interfaces_to_implementations(instance=_instance,
                                       interface_list=interfaces_to_implementations)
    return _instance


global_injector: Injector = get_injector()
"""Global injector for the entire application."""
