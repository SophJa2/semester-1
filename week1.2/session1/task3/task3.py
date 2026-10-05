# Week 1.2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
print(fruit.index("banana"))
# Display how many times "cherry" occurs

# Display how many times "strawberry" occurs
def find(find):
    count = 0
    for i in range (len(fruit)):
        if fruit[i-1] == find:
            count += 1
    print(count)


fruitfind = "cherry"
find(fruitfind)

fruitfind = "strawberry"
find(fruitfind)
# Unpack tuple into variables
(first,second,third) = fruit
print(first)