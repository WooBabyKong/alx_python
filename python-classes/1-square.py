#!/usr/bin/python3
"""Module documentation"""

class Square:
    """Square class with private size attribute"""

    def __init__(self, size=0):
        """Class constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size