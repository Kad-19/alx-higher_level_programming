#!/usr/bin/python3
"""
    Class rectangle that implements base
"""
from models.base import Base


class Rectangle(Base):
    """
        class rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initiaizes the instance of the class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            getter for width
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter for width
            Args:
                value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
            getter for height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter for height
            Args:
                value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
            getter for x
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter for x
            Args:
                value (int): value to be set
        """

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
            getter for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter for y
            Args:
                value (int): vlue to be set
        """

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            returns area
            Returns: area
        """
        return (self.height * self.width)

    def display(self):
        """
            prints the rectangle with '#'
        """
        rectangle = ""

        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ('#' * self.width) + '\n'
        print(rectangle, end="")

    def __str__(self):
        """
            returns string fromat of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            updates the attributes of the rectangle
            Args:
                *args - variable number of arguments
                **kwargs - variable number of key worded arguments
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            returns the dictionary repr of a rect
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
