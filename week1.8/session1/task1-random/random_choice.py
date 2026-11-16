import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

#print(names)

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
Num = int(input("Enter how many: "))
RandNames = []
for i in range(Num):
    RandNames.append(names[random.randint(0,(len(names)-1))])
    print(RandNames[i])
# Display the chosen names, one per line
