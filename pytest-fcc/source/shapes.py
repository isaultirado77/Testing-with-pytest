import math
from abc import ABC, abstractmethod

class Shape(ABC): 
    @abstractmethod
    def area(self) -> float: 
        pass

    @abstractmethod
    def perimeter(self) -> float: 
        pass

class Circle(Shape):
    def __init__(self, r: float):
        self.radius = r

    def area(self): 
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape): 
	pass
