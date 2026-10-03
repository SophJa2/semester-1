"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
Valid = True
try:
    MonthlySaved = int(input("Enter he amount of money you will save every month: "))
except TypeError:
    print("Invalid amount")
    Valid = False
except ValueError:
    print("Invalid amount")
    Valid = False
 

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

if Valid == True:
    YearlySaved = MonthlySaved * 12
    print(f"You have save {YearlySaved} this year")

    # Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
    # print this out in the format £X.XX (to two decimal places).

    TotalAmount = YearlySaved + YearlySaved*0.008
    print(f"{TotalAmount:.2f}")
    