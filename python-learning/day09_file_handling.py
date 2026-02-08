# Day 9: File Handling
# Read and write files in Python

# Write to a file
file = open("my_file.txt", "w")  # "w" = write mode
file.write("Hello, File!\n")
file.write("This is Python learning.\n")
file.write("I'm storing data in a file!")
file.close()

print("File created and written!")

# Read from a file
file = open("my_file.txt", "r")  # "r" = read mode
content = file.read()
print("\nFile content:")
print(content)
file.close()

# Read line by line
file = open("my_file.txt", "r")
print("\nReading line by line:")
for line in file:
    print(f"  {line.strip()}")  # strip() removes \n
file.close()

# Append to a file (add without overwriting)
file = open("my_file.txt", "a")  # "a" = append mode
file.write("\nAdded this new line!")
file.close()

# Read again to see new content
file = open("my_file.txt", "r")
print("\nUpdated file content:")
print(file.read())
file.close()

# Better way: using 'with' statement (automatically closes file)
with open("my_file.txt", "r") as file:
    content = file.read()
    print("\nUsing 'with' statement:")
    print(content)

# TODO: Create a file with your learning notes
# Write 3-5 lines
# Read it back and print it
