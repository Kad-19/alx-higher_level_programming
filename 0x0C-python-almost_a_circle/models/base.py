#!/usr/bin/python3
"""Defines a base model class"""


class Base:
    """Represents the base model
        for all the other classes

    Attributes:
        __nb_objects (int): number of instances.
    """
    def __init__(self, id=None):
        """Initialize base.

        Args:
            id(int): The identity of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
