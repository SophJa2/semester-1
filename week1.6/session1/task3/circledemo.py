# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

from shapes import Shape,Circle
from point import Point

p = Point(1,6)
c = Circle(2.5,p,"blue")
print(c.__str__())
print(c.Area())
print(c.Perimeter())
