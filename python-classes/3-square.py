#!/usr/bin/python3
"""Module documentation"""

class Square:
    """Square class with private size attribute"""

    def __init__(self, size=0):
        """Class constructor"""
        self.size = size  # Utilizing the setter method for size

    @property
    def size(self):
        """Getter method to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2