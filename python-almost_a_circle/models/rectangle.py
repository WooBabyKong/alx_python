#!/usr/bin/python3
"""Module documentation"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size (overrides Rectangle's width)"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size (overrides Rectangle's width)"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)