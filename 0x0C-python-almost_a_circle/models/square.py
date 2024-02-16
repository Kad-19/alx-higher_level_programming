#!/usr/bin/python3
"""
    class square that impelements rectangle
"""
from model.rectangle import Rectangle


class Square(Rectangle):
    """
        class square that implements rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            square constructor
        """
        super.__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            returns the size of the sqare
            Returns: width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            setter for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
            Overloading str function
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)
