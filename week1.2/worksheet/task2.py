# Worksheet 1.2: Task 2 Solution

count = int(input("Enter the amount of values yo want to enter"))
numbers = []

for i in range(count):
    try:
        num = float(input("Enter a number: "))
    except NonZeroError:
        sys.exit("no numbers provided")
    numbers.append(num)

