# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if not isinstance(width,int):
            raise TypeError
        if not isinstance(height,int):
            raise TypeError
        if height <=0 or width <=0:
            raise ValueError

        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    
    def is_square(self):

        """
        This method checks if the rectangle is a square
        """

        if self.width == self.height:
            return True
        else:
            return False
        
    def area(self):
        """
        This method calculates the area of the rectangle
        """
        
        self.area = self.height * self.width
        return self.area
    
    def perimeter(self):
        """
        This method calculates the perimeter of the rectange
        """
        
        self.perimeter = self.height * 2 + self.width * 2
        return self.perimeter


