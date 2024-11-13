
import os

filename = 'example.txt'

# Create and write 
with open(filename, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a file handling example.\n")

# Read 
with open(filename, 'r') as file:
    content = file.read()
    print("File Content:")
    print(content)

# Append 
with open(filename, 'a') as file:
    file.write("Appending a new line.\n")

# Read the update
with open(filename, 'r') as file:
    updated_content = file.read()
    print("Updated File Content:")
    print(updated_content)

# Check 
if os.path.exists(filename):
    print(f"{filename} exists.")

# Delete 
os.remove(filename)

# Check if the file was deleted
if not os.path.exists(filename):
    print(f"{filename} has been deleted.")