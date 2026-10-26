# Week 1.5, Session 1: Task 3
import math

class Point:
    A Point in 2D space.
    """

    # Add constructor here"""
    def __init__(self,x_coordinate,y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinateass

    # Add distance() method here
    def distance(self):

        distance = math.sqrt(self.x**2 + self.y**2)
        return distance

    # Add distance_to() method here
    # (This will need a parameter representing another point)

    def distance_to(self,newX,newY):

        distance = math.sqrt((self.x-newX)**2 + (self.y-newY)**2)
        
        return distance


# Finally, add code here to demonstrate use of Point
p = Point(3,4)
print(p.distance())
print(p.distance_to(0,0))