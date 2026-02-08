# Day 6: Functions
# A function is a reusable block of code

# Simple function
def greet():
    print("Hello, World!")

greet()  # Call the function

# Function with parameters (inputs)
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Krish")
greet_person("Alice")

# Function with return value
def add(a, b):
    result = a + b
    return result

sum_result = add(5, 3)
print(f"5 + 3 = {sum_result}")

# Function with multiple parameters
def multiply(x, y):
    return x * y

print(f"4 * 7 = {multiply(4, 7)}")

# Function with default value
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # Uses default exponent=2
print(power(5, 3))   # Uses exponent=3

# TODO: Create your own function that:
# 1. Takes two numbers as input
# 2. Returns their average
# 3. Call it with different numbers
