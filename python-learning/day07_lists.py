# Day 7: Lists
# A list is a collection of items

# Create a list
fruits = ["apple", "banana", "orange", "mango"]
print(fruits)

# Access items (index starts at 0)
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # mango (last item)

# Add items to list
fruits.append("grape")
print(fruits)

# Remove items
fruits.remove("banana")
print(fruits)

# List length
print(f"Number of fruits: {len(fruits)}")

# Loop through list
print("All fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# List with numbers
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")

# List slicing
first_three = numbers[0:3]  # Items from index 0 to 2
print(f"First three: {first_three}")

# TODO: Create a list of your favorite movies and:
# 1. Print the second movie
# 2. Add a new movie
# 3. Loop through and print all movies
