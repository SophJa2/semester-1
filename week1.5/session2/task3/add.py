# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum
from money import Money

money1 = Money(2,8)
money2 = Money(5,20)

print(money1.__add__(money2))