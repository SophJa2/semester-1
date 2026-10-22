"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Sophia Jacob
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
StateColour = list(states.keys())
values = list(states.values())

systime = 0
maxtime = int(input("Max time : "))  # read an integer number of steps (>0)
ColourIndex = 0
ColourCounter = 0

while systime < maxtime+1:
    if ColourCounter < values[ColourIndex]-1:
        state = StateColour[ColourIndex]
        ColourCounter +=1
    else:
        ColourIndex += 1
        ColourCounter = 0
    if ColourIndex == 4:
        ColourIndex = 0

    print(f"Time {systime:03} State {state}")
    systime += 1

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14