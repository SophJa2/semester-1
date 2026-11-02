# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name,birth):
        """
        This method initilises the name of the person and their date of birth
        """
        if not isinstance(name,str):
            raise TypeError
        if not isinstance(birth,date):
            raise TypeError
        if len(name) <=0:
            raise ValueError
        
        self.name = name
        self.birth = birth

    def initials(self):
        """
        This method creates the initialized name for the person
        """

    def is_birthday(self):
        """
        This method checks if it is the persons birthday today
        """
        if self.birth == date.today():
            return True
        else:
            return False

print(date.today())