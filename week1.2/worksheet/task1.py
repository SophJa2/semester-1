# Worksheet 1.2: Task 1 Solution
import sys

try:
    num = int(input("Enter a number between 0 and 100: "))
    if num > 100 or num < 0:
        sys.exit("Error: Grade must be an integer between 0 and 100")
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100")
except TypeError:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if num > 69:
    grade = "Distinction"
elif num > 39:
    grade = "Pass"
else:
    grade = "Fail"

print(f"{num} is a {grade}")