"""Dependency injection module for the application.

This module sets up the application's dependency injection framework using the Injector package. 
It allows for the central management of dependencies, ensuring that components can be easily 
replaced or mocked for testing. The global injector is configured to automatically bind interfaces 
to their implementations, promoting loose coupling and modularity.
"""

from typing import List, Tuple

from injector import Injector

from app.settings import Settings

interfaces_to_implementations: List[Tuple] = [
    # Interface to implementation mapping
    (Settings, Settings),
    # Additional mappings can be added here
]

def bind_interfaces_to_implementations(instance: Injector, interface_list: list) -> None:
    """Bind interfaces to implementations using a list of tuples.

    This function iterates over a list of (interface, implementation) tuples
    and binds them within the provided Injector instance. 
    It facilitates the configuration of the application's dependency injection.

    Args:
        instance (Injector): The injector instance for the application.
        interface_list (list): List of tuples, where each tuple contains an
        interface and its implementation class.
    """
    for interface, implementation in interface_list:
        instance.binder.bind(interface, to=implementation)

def get_injector() -> Injector:
    """Create and return the configured Injector for the application.

    This function initializes an Injector instance, binds interfaces to their
    implementations according to the `interfaces_to_implementations` list, 
    and returns the configured Injector.

    Returns:
        Injector: The configured Injector instance for the application.
    """
    _instance: Injector = Injector()
    bind_interfaces_to_implementations(_instance, interfaces_to_implementations)
    return _instance

global_injector: Injector = get_injector()
