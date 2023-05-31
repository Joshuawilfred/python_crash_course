#!/usr/bin/python3
"""Square cont.."""



class Square:
    """Within the square class"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square"""
        if type(value) is not int:
            raise TypeError("Err: size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print square using #"""
        for i in range(self.size):
            print("#" * self.size)

        if not self.size:
            print()
