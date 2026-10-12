# Week 1.3, Session 1: Task 3b

fruit = ['apple','pear','banana','orange']

while fruit:
	if len(fruit) != 0:
		print(fruit.pop())
	else:
		print("This list is now empty")


# Add an else clause with a message that the list is now empty