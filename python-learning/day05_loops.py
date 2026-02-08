# Day 5: Loops (repeat code)
# Do the same thing multiple times

# For loop - repeat a specific number of times
print("For Loop:")
for i in range(5):
    print(f"Count: {i}")

# For loop with list
print("\nLooping through a list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loop - repeat while condition is true
print("\nWhile Loop:")
count = 0
while count < 3:
    print(f"Count is {count}")
    count = count + 1

# range() creates a sequence
# range(5) = 0, 1, 2, 3, 4
# range(1, 5) = 1, 2, 3, 4
# range(0, 10, 2) = 0, 2, 4, 6, 8

# TODO: Print numbers from 1 to 10 using a loop!
