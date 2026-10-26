# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
class Point:
    def __init__(self,x_coordinate,y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

class Circle:
    def __init__(self,radius,point):
        self.radius = radius
        self.x_centre = point.x
        self.y_centre = point.y

    def area(self):
        area = (self.radius**2)*math.pi
        return area

    def perimeter(self):
        perimeter = 2 * self.radius * math.pi
        return perimeter

