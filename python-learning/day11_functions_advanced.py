# Day 11: Advanced Functions
# Topics: parameters, *args, **kwargs, lambda, map/filter, docstrings

def greet(name, /, greeting='Hello', *, punct='!'):
    """Example of positional-only, default and keyword-only args."""
    print(f"{greeting}, {name}{punct}")

greet("Krish")
greet("Alice", greeting="Hi", punct=".")

# *args and **kwargs
def show(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

show(1, 2, 3, a=10, b=20)

# Return functions (closures) and lambda
def make_multiplier(n):
    return lambda x: x * n

times3 = make_multiplier(3)
print(times3(5))  # 15

# map, filter, list comprehensions
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Squares:", squares)
print("Evens:", evens)

# Equivalent with comprehensions
squares2 = [x**2 for x in nums]
evens2 = [x for x in nums if x % 2 == 0]
print("Squares2:", squares2)
print("Evens2:", evens2)

# Docstring example
def average(*values):
    """Return the average of given numeric values. Returns 0 for no input."""
    if not values:
        return 0
    return sum(values) / len(values)

print("Average:", average(3, 4, 5))

# Exercises (do these, edit the file to implement)
# 1) Write a function `concat(*parts, sep=' ')` that joins strings.
# 2) Write a function `apply_all(func, items)` that returns [func(x) for x in items].
# 3) Use a lambda and map to uppercase a list of names.
# 4) Add docstrings to your functions and print them with help(func).
