#!/usr/bin/python3
"""Defines a class Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""
    
    def __init__(self, size):
        """Initialize a new square instance.
        
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size


if __name__ == "__main__":
    my_square = Square(5)
    print(my_square)
    print(my_square.area())