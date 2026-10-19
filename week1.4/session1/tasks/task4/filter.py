# Week 4, Session 1: 

# Your are given the function filter_positive_numbers with a docstring.
# Can you identify the inconsistency between the docstring and the implementation?

# Your task is to update the docstring to reflect what the function does.


def filter_positive_numbers(numbers):
    posInts = [num for num in numbers if num > 0]
    return posInts

nums = []
num = int(input())
while num != "":
    nums.append(num)
    num = int(input()
filter_positive_numbers(nums)