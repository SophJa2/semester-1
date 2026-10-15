# Worksheet 1.2: Task 2 Solution

from util import read_numbers

count = int(input("Enter the number of float numbers in the sequence "))

numbers = read_numbers()
print(numbers)
if len(numbers) == 0:
    sys.exit("no numbers provided")

if count % 2 == 0:
    median = numbers[(len(numbers)//2)-1] + (numbers[(len(numbers)//2)] - numbers[(len(numbers)//2 - 1)])/2
else:
    median = numbers[len(numbers)//2]

print(f"Minimun = {min(numbers)}\nMaximum = {max(numbers)}\nMean = {sum(numbers)/count}\nMedian = {median}\n")
