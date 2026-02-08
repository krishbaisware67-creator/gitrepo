# Day 8: Dictionaries
# A dictionary stores data as key-value pairs

# Create a dictionary
person = {
    "name": "Krish",
    "age": 20,
    "city": "Bangalore",
    "country": "India"
}

print(person)

# Access values using keys
print(person["name"])    # Krish
print(person["age"])     # 20

# Add new key-value pair
person["email"] = "krish@example.com"
print(person)

# Update a value
person["age"] = 21
print(person)

# Remove a key-value pair
del person["country"]
print(person)

# Loop through dictionary
print("Person details:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Get all keys
print(f"Keys: {person.keys()}")

# Get all values
print(f"Values: {person.values()}")

# Check if key exists
if "name" in person:
    print("Name exists!")

# Dictionary with different data types
student = {
    "name": "Alice",
    "grades": [85, 90, 88],
    "active": True
}

print(student)

# TODO: Create a dictionary for a book with:
# title, author, pages, year
# Print each detail
# Update the year
