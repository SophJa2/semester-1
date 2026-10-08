# Worksheet 1.2: Task 2 Solution

from util import read_numbers

count = int(input("Enter the number of float numbers in the sequence "))

numbers = read_numbers()
print(numbers)
if len(numbers) == 0:
    sys.exit("no numbers provided")

total = 0
maximum = 0
minimum = 0
