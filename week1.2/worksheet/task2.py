# Worksheet 1.2: Task 2 Solution

from util import read_numbers

count = int(input("Enter the number of float numbers in the sequence "))

numbers = read_numbers()
print(numbers)
if len(numbers) == 0:
    sys.exit("no numbers provided")
elif len(numbers) != count:

if count % 2 == 0:
    median = numbers[round((count/2))] + ((numbers[round((count/2))] - numbers[round((count/2))-1])/2)
elif count == 1:
    median = numbers[0]
else:
    median = numbers[round((count/2))]

print(f"Minimun = {min(numbers)}\nMaximum = {max(numbers)}\nMean = {sum(numbers)/count}\nMedian = {median}\n")
