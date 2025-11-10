"""
Scaffolder registry and initialization.

This module manages the registration of all available framework scaffolders.
To add a new framework, simply import its scaffolder here and add it to SCAFFOLDERS.
"""

from typing import Dict, Type
from .base import FrameworkScaffolder
from .react import ReactScaffolder
from .fastapi import FastAPIScaffolder
from .flutter import FlutterScaffolder


# Registry of all available framework scaffolders
# To add a new framework:
# 1. Create a new scaffolder class that extends FrameworkScaffolder
# 2. Import it above
# 3. Add it to this dictionary with a unique key
SCAFFOLDERS: Dict[str, Type[FrameworkScaffolder]] = {
    'react': ReactScaffolder,
    'fastapi': FastAPIScaffolder,
    'flutter': FlutterScaffolder,
}


def get_scaffolder(framework_key: str) -> FrameworkScaffolder:
    """
    Get a scaffolder instance for the given framework.
    
    Args:
        framework_key (str): Key identifying the framework ('react', 'fastapi', etc.)
    
    Returns:
        FrameworkScaffolder: Instance of the appropriate scaffolder
    
    Raises:
        KeyError: If framework_key is not registered
    """
    scaffolder_class = SCAFFOLDERS.get(framework_key)
    if not scaffolder_class:
        raise KeyError(f"Unknown framework: {framework_key}")
    return scaffolder_class()


def list_available_frameworks() -> list[str]:
    """
    Get list of all available framework keys.
    
    Returns:
        list[str]: List of framework keys that can be scaffolded
    """
    return list(SCAFFOLDERS.keys())


__all__ = [
    'FrameworkScaffolder',
    'ReactScaffolder',
    'FastAPIScaffolder',
    'FlutterScaffolder',
    'get_scaffolder',
    'list_available_frameworks',
    'SCAFFOLDERS',
]
