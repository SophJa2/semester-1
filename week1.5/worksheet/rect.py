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
        try:
            if height <= 0 or width <= 0:
                raise ValueError
        except TypeError:
            print("Values should be integers")
        except ValueError:
            print("Values should be larger than 0")

        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False
        
    def area(self):
        area = height * width
        return area
    
    def perimeter(self):
        perimeter = height * 2 + width * 2
        return perimeter


r = Rectangle()