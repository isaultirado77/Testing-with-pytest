import pytest
import source.shapes as shapes


def test_area(my_rectangle): 
	rectangle = shapes.Rectangle(10., 20.)
	assert my_rectangle.area() == 10. * 20.


def test_perimeter(my_rectangle): 
	rectangle = shapes.Rectangle(10., 20.)
	assert my_rectangle.perimeter() == (2 * 10.) + (2 * 20.)


def test_not_eq(other_rectangle, my_rectangle): 
	assert my_rectangle != other_rectangle

