# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated

        if not isinstance(pounds,int) or not isinstance(pence,int):
            raise TypeError("pounds and pence should be integers")
        if pounds < -1 or pence < 0 or pence > 99:
            raise ValueError("pounds should be an integer and pence should be btw 0 and 99")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')
        return f"£{self.pounds}.{self.pence:02d}" 

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        if not isinstance(other, Money): #checks whether other is a money object
            #isinstance can be used to check if its an object
            raise ValueError("the addition should include an int")


        pence = other.pence + self.pence
        if pence > 99:
            pound = str(pence)
            pound = pound[0]
            pence = pence - pound
            self.pounds = self.pounds + other.pounds + pound
        else:
            self.pounds = self.pounds + other.pounds
        self.pence = pence
        return f"£{self.pounds}.{self.pence}" 

