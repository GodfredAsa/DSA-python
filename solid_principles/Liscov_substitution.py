


"""
Liskov Substitution Principle (LSP)

Subtypes must be substitutable for their base types.
For example, if you have a piece of code that works with a Shape class, 
then you should be able to substitute that class with any of its subclasses, 
such as Circle or Rectangle, without breaking the code.
Shape becomes the type that you can substitute through polymorphism with either Rectangle or Square, 
which are now siblings rather than a parent and a child. 
Notice that both concrete shape types have distinct sets of attributes, 
different initializer methods, and could potentially implement even more separate behaviors. 
The only thing that they have in common is the ability to calculate their area.

With this implementation in place, 
you can use the Shape type interchangeably with its Square and 
Rectangle subtypes when you only care about their common behavior:
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2


def get_total_area(shapes: 'Rectangle' or 'Square'): # type: ignore
    return sum(shape.calculate_area() for shape in shapes)

print(get_total_area([Rectangle(10, 5), Square(5)]))
