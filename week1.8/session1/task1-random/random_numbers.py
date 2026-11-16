import random

# Get user to input how many random numbers they want
numRandom = int(input("How many random numbers: "))
# Generate this many random numbers
Nums = []
for i in range(0,numRandom):
    print(i)
    Nums.append(random.randint(1,100))

print(Nums)
# Write the random numbers to a file named random.txt, one number per line
with open("random.txt","w") as file:
    for i in range(numRandom):
        file.write(f"{Nums[i]}\n")