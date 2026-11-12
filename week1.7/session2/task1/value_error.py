# Week 1.7, Session 2: Task 1 - ValueError

# Run this program and observe what happens

user_profile = {"username": "alice99", "role": "admin"}

for key in user_profile: #cant ask for two values in a for loop
	print(f"{key} : {user_profile[key]}")