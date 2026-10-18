"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Sophia Jacob
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input("Max time : "))  # read an integer number of steps (>0)
time = 0

while time != (maxtime + 1):
    if time < 4:
        state = "red"
    elif time < 7:
        state = "red_amber"
    elif time < 12:
        state = "green"
    else:
        state = "amber"

    print(f"Time {systime:03} State {state}")
    systime += 1
    time += 1
    if time == 15:
        time = 0
        maxtime -= 15

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14